import datetime
from django.db import models
from contrib.daterange import NewDateRange

from rh.models import MovimentacaoPosse, PossessionTrainee, Servidor

from contrib.daterange import NewDateRange
from contrib.utils import getLogger
from rh.afastamento.models import AfastamentoOutroOrgao
from rh.models import MovimentacaoRequisicao, Servidor
from rh.pensao.models import Pensao
from standard.models import AuditTimestampModel

log = getLogger(__name__)


                                            
                                           
class PMEmployeesCache(AuditTimestampModel):


    registration = models.CharField(
        db_index=True, max_length=50, null=True, blank=True, verbose_name="Matrícula"
    )
    name = models.CharField(
        max_length=100, verbose_name="Nome", default="", blank=False
    )
    effective_role = models.CharField(max_length=100, null=True, blank=True)
    comission_role = models.CharField(max_length=100, null=True, blank=True)

    ordinance_number_nomination = models.CharField(
        verbose_name="Número da Portaria - Nomeação",
        max_length=20,
        null=True,
        blank=True,
    )
    ordinance_year_nomination = models.CharField(
        verbose_name="Ano da Portaria - Nomeação", max_length=4, blank=True
    )
    publication_date_nomination = models.CharField(
        verbose_name="Data da publicação - Nomeação",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )

    ordinance_number_retirement = models.CharField(
        verbose_name="Número da Portaria - Aposentadoria",
        max_length=20,
        null=True,
        blank=True,
    )
    ordinance_year_retirement = models.CharField(
        verbose_name="Ano da Portaria - Aposentadoria", max_length=4, null=True, blank=True
    )
    publication_date_retirement = models.CharField(
        verbose_name="Data da publicação - Aposentadoria",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )
    workplace = models.CharField(max_length=100)
    stability = models.BooleanField(default=True)
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True, null=True)  
    is_member = models.BooleanField(default=False) 
    updated = models.BooleanField(default=False, null=True)


    class Meta:                 

        unique_together = ["registration", "month", "year"]

    def __str__(self):
        return f"{self.registration} - {self.name}"

    def get_effective_role_active(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF", data_exercicio__lte=end_date
            )
            .order_by("data_exercicio")
            .last()
        )
        if possession is not None:
            effective_role = possession.description_possession
            return effective_role
        else:
            return "N/C"

    def get_comission_role(employee, date_range):
       
        end_date = date_range.end_date
        comission_role = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )
        if (
            comission_role is not None
            and comission_role.quadro is not None
            and comission_role.quadro.cargo is not None
        ):
            comission_role = comission_role.quadro.cargo.nome
            return comission_role
        else:
            return "N/C"

    def get_workplace_name(employee, date_range):
        workplace = (
            employee.servidor_lotacao.filter(
                designacao=False, data_vigencia_inicio__lte=date_range.end_date
            )
            .order_by("data_vigencia_inicio")
            .last()
        )
        if workplace is not None and workplace.lotacao is not None:
            workplace_name = workplace.lotacao.nome
            return workplace_name
        else:
            return "N/C"

    def get_ordinance_year_nomination(employee, date_range, is_active=True):
        if is_active:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_exercicio__lte=end_date
                )
                .order_by("data_exercicio")
                .last()
            )
        else:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
                )
                .order_by("data_desligamento")
                .last()
            )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            ordinance_year = (
                publication.ano
                if ("00000" not in publication.ano and "S/N" not in publication.ano)
                else "SN"
            )
            return ordinance_year
        else:
            return "SN"

    def get_ordinance_number_nomination(employee, date_range, is_active=True):
        if is_active:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_exercicio__lte=end_date
                )
                .order_by("data_exercicio")
                .last()
            )
        else:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
                )
                .order_by("data_desligamento")
                .last()
            )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            ordinance_number = (
                publication.numero
                if (
                    "00000" not in publication.numero
                    and "S/N" not in publication.numero
                )
                else "SN"
            )
            return ordinance_number
            
        else:
            return "SN"

    def get_publication_date_nomination(employee, date_range, is_active=True):
        if is_active:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_exercicio__lte=end_date
                )
                .order_by("data_exercicio")
                .last()
            )
        else:
            end_date = date_range.end_date
            possession = (
                employee.posses.filter(
                    quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
                )
                .order_by("data_desligamento")
                .last()
            )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            date = publication.data_publicacao

            if date is not None:
                return date
            else:
                return None

        else:
            return None

    def get_ordinance_number_retire(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
            )
            .order_by("data_desligamento")
            .last()
        )

        if possession is not None and possession.desligamento is not None:
            retirement = possession.desligamento
            publication = retirement.publicacao_movimentacao

            if publication is not None:
                retire_number = (
                    publication.numero
                    if (
                        "00000" not in publication.numero
                        and "S/N" not in publication.numero
                    )
                    else "SN"
                )
                return retire_number
            else:
                return "SN"

        else:
            return "SN"

    def get_ordinance_year_retire(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
            )
            .order_by("data_desligamento")
            .last()
        )

        if possession is not None and possession.desligamento is not None:
            retirement = possession.desligamento
            publication = retirement.publicacao_movimentacao

            if publication is not None:
                retire_year = (
                    publication.ano
                    if ("00000" not in publication.ano and "S/N" not in publication.ano)
                    else "SN"
                )
                return retire_year
            else:
                return "SN"

        else:
            return "SN"

    def get_publication_date_retire(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF", data_desligamento__lte=end_date
            )
            .order_by("data_desligamento")
            .last()
        )

        if possession is not None and possession.desligamento is not None:
            publication = possession.desligamento.publicacao_movimentacao
            date = publication.data_publicacao

            if date is not None:
                return date
            else:
                return None

        else:
            return None

    def get_stability(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF", data_exercicio__lte=end_date
            )
            .order_by("data_exercicio")
            .last()
        )
        if possession is not None:
            if hasattr(possession, "estabilizacoes"):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def load(self, is_active, is_member, year_filter, month_filter):


        """Summary:Essa é uma classe com um método de classe (ou método estático) chamado load que recebe quatro parâmetros: is_active, is_member, year_filter e month_filter. 
            Esses parâmetros controlam as opções de filtragem para a busca de servidores.
            A função começa convertendo os parâmetros em inteiros usando a função int() e define duas listas de tipos de servidores: employee_types e member_types.
            A variável date_filter é inicializada com um objeto NewDateRange que representa todo o período até a data atual.
        
            Args:
            RestfulDRY(Servidor):None
        """


        is_active = int(is_active)
        is_member = int(is_member)
        year_filter = int(year_filter)
        month_filter = int(month_filter)

        employee_types = ["EFE", "EFC", "ECM"]
        member_types = ["MBR", "MCM", "MEL", "MBR2", "MEL2"]

        date_filter = NewDateRange(None, datetime.date.today())

        if year_filter and month_filter:
            date_filter = NewDateRange.from_month(year_filter, month_filter)

        active_emp = Servidor.objects.active_in(date_range=date_filter).order_by(
            "pessoa_fisica__nome"
        )
        inactive_emp = Servidor.objects.inactive_in(date_range=date_filter).order_by(
            "pessoa_fisica__nome"
        )

        if is_active == 1:  
            employees = active_emp | inactive_emp

        elif is_active == 2:
            employees = active_emp

        else:  
            employees = inactive_emp

        if is_member == 1: 
            employees = employees.filter(
                type_by_possession__in=employee_types + member_types
            )

        elif is_member == 2: 
            employees = employees.filter(type_by_possession__in=employee_types)

        else: 
            employees = employees.filter(type_by_possession__in=member_types)

        for employee in employees.order_by("pessoa_fisica__nome"):

            PMEmployeesCache.objects.update_or_create(
                registration=employee.matricula,
                month=month_filter,
                year=year_filter,
                defaults={
                    "name": employee.pessoa_fisica.nome,
                    "effective_role": self.get_effective_role_active(
                        employee, date_filter
                    ),
                    "comission_role": self.get_comission_role(employee, date_filter),
                    "ordinance_number_nomination": self.get_ordinance_number_nomination(
                        employee, date_filter, is_active=True
                    )
                    if active_emp.filter(id=employee.id).exists()
                    else self.get_ordinance_number_nomination(
                        employee, date_filter, is_active=False
                    ),
                    "ordinance_year_nomination": self.get_ordinance_year_nomination(
                        employee, date_filter, is_active=True
                    )
                    if active_emp.filter(id=employee.id).exists()
                    else self.get_ordinance_year_nomination(
                        employee, date_filter, is_active=False
                    ),
                    "publication_date_nomination": self.get_publication_date_nomination(
                        employee, date_filter, is_active=True
                    )
                    if active_emp.filter(id=employee.id).exists()
                    else self.get_publication_date_nomination(
                        employee, date_filter, is_active=False
                    ),
                    "ordinance_number_retirement": self.get_ordinance_number_retire(
                        employee, date_filter
                    )
                    if inactive_emp.filter(id=employee.id).exists()
                    else None,
                    "ordinance_year_retirement": self.get_ordinance_year_retire(
                        employee, date_filter
                    )
                    if inactive_emp.filter(id=employee.id).exists()
                    else None,
                    "publication_date_retirement": self.get_publication_date_retire(
                        employee, date_filter
                    )
                    if inactive_emp.filter(id=employee.id).exists()
                    else None,
                    "workplace": self.get_workplace_name(employee, date_filter),
                    "stability": self.get_stability(employee, date_filter),
                    "month": month_filter,
                    "year": year_filter,
                    "is_active": True
                    if active_emp.filter(id=employee.id).exists()
                    else False,
                    "is_member": True
                    if employee.type_by_possession in member_types
                    else False,
                    "updated": True,
                },
            )


class PMPensionersCache(AuditTimestampModel):

    """Summary:A classe PMPensionersCache é um modelo de banco de dados do Django que herda de AuditTimestampModel, que fornece campos adicionais para rastreamento de alterações em registros.

    Returns:
        (Pensionistas): None
    """

    name_founder = models.CharField(
        max_length=100, verbose_name="Instituidor da pensão", default="", blank=False
    )
    effective_role = models.CharField(max_length=100, null=True, blank=True)
    name_pensioner = models.CharField(
        max_length=100, verbose_name="Pensionista", default="", blank=False
    )

    ordinance_number_pension = models.CharField(
        verbose_name="Número da portaria", max_length=20, null=True, blank=True
    )
    ordinance_year_pension = models.CharField(
        verbose_name="Ano da portaria", max_length=20, null=True, blank=True
    )
    publication_date_pension = models.CharField(
        verbose_name="Data da publicação",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(null=True)
    updated = models.BooleanField(default=False, null=True)

    class Meta:

        """:Summary:Essa classe é usada para armazenar em cache informações relacionadas a pensionistas do estado, e possui vários métodos auxiliares que realizam diferentes operações.

            Args:
            type(Pensionista):métodos
        """ 

        unique_together = ["name_pensioner", "month", "year"]

    def __str__(self):
        return f"{self.name_pensioner} - {self.name_founder}"

    def get_effective_role(pension):
        if (
            pension.servidor is not None
            and pension.servidor.last_possession is not None
        ):
            employee = pension.servidor
            possession = employee.last_possession.description_possession
            return possession
        else:
            return "N/C"

    def get_ordinance_number(pension):

        if pension.publicacao is not None:
            publication = pension.publicacao
            ordinance_number = (
                publication.numero
                if (
                    "00000" not in publication.numero
                    and "S/N" not in publication.numero
                )
                else "SN"
            )
            return ordinance_number
        else:
            return "SN"

    def get_ordinance_year(pension):
        if pension.publicacao is not None:
            publication = pension.publicacao
            ordinance_year = (
                publication.ano
                if ("00000" not in publication.ano and "S/N" not in publication.ano)
                else "SN"
            )
            return ordinance_year
        else:
            return "SN"

    def get_publication_date(pension):
        if pension.publicacao is not None:
            publication = pension.publicacao
            date = publication.data_publicacao
            if date is not None:
                publication_date = date.strftime("%d/%m/%Y")
                return publication_date
            else:
                return None
        else:
            return None

    @classmethod
    def load(self, year_filter, month_filter):

        """Summary:Esta é uma função de classe chamada "load" que é definida dentro de uma classe (não fornecida no código fornecido). 
                   É um método que carrega dados de pensão em um objeto PMPensionersCache
        
            Args:
                (Pensionista):description
        """

        year_filter = int(year_filter)
        month_filter = int(month_filter)

        if month_filter and year_filter:
            date_filter = NewDateRange(None, datetime.date.today())

        pensions = Pensao.objects.actives_in(range=date_filter).filter(tipo=2)

        for pension in pensions.order_by("servidor__pessoa_fisica__nome"):
            log.info(pension)

            PMPensionersCache.objects.update_or_create(
                name_pensioner=pension.pensionista.nome,
                month=month_filter,
                year=year_filter,
                defaults={
                    "name_founder": pension.servidor.pessoa_fisica.nome
                    if pension.servidor is not None
                    else "N/C",
                    "effective_role": self.get_effective_role(pension),
                    "ordinance_number_pension": self.get_ordinance_number(pension),
                    "ordinance_year_pension": self.get_ordinance_year(pension),
                    "publication_date_pension": self.get_publication_date(pension),
                },
            )


class PMAssignedEmployeesCache(AuditTimestampModel):
    registration = models.CharField(
        db_index=True, max_length=50, null=True, blank=True, verbose_name="Matrícula"
    )
    name = models.CharField(
        max_length=100, verbose_name="Nome", default="", blank=False
    )

    original_role = models.CharField(max_length=100, null=True, blank=True)
    current_role = models.CharField(max_length=100, null=True, blank=True)
    comission_role = models.CharField(max_length=100, null=True, blank=True)

    ordinance_number_assignment = models.CharField(
        verbose_name="Número da portaria", max_length=20, null=True, blank=True
    )
    ordinance_year_assignment = models.CharField(
        verbose_name="Ano da portaria", max_length=20, null=True, blank=True
    )
    publication_date_assignment = models.CharField(
        verbose_name="Data da publicação",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )
    workplace = models.CharField(max_length=100)
    original_organ = models.CharField(max_length=100)
    target_organ = models.CharField(max_length=100)
    onus_mp = models.BooleanField(default=False)
    from_mp = models.BooleanField(default=False)
    deadline = models.CharField(
        verbose_name="Prazo", default="", max_length=10, null=True, blank=True
    )
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(null=True)
    updated = models.BooleanField(default=False, null=True)


    class Meta:
        unique_together = ["registration", "month", "year"]

    def __str__(self):
        return f"{self.registration} - {self.name}"

    def get_original_role(assignment):
        if assignment.posse_origem is not None:
            original_role = assignment.posse_origem.description_possession
            return original_role
        else:
            return "N/C"

    def get_current_role(assignment, date_range):
        end_date = date_range.end_date
        possession = (
            assignment.servidor.posses.filter(data_exercicio__lte=end_date)
            .order_by("data_exercicio")
            .last()
        )
        if possession is not None:
            current_role = possession.description_possession
            return current_role
        else:
            return "N/C"

    def get_comission_role(assignment, date_range):
        end_date = date_range.end_date
        comission_role = (
            assignment.servidor.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )
        if (
            comission_role is not None
            and comission_role.quadro is not None
            and comission_role.quadro.cargo is not None
        ):
            comission_role = comission_role.quadro.cargo.nome
            return comission_role
        else:
            return "N/C"

    def get_ordinance_number(assignment):
        if assignment.publicacao_movimentacao is not None:
            publication = assignment.publicacao_movimentacao
            ordinance_number = publication.numero
            return ordinance_number
        else:
            return "SN"

    def get_ordinance_year(assignment):
        if assignment.publicacao_movimentacao is not None:
            publication = assignment.publicacao_movimentacao
            ordinance_year = publication.ano
            return ordinance_year
        else:
            return "SN"

    def get_publication_date(assignment):
        if assignment.publicacao_movimentacao is not None:
            publication = assignment.publicacao_movimentacao
            pub_date = publication.data_publicacao
            if pub_date is not None:
                pub_date = pub_date.strftime("%d/%m/%Y")
                return pub_date
            else:
                return None
        else:
            return None

    def get_original_organ(assignment):
        if assignment.orgao_origem is not None:
            original_organ = assignment.orgao_origem.nome
            return original_organ
        else:
            return "N/C"

    def get_target_organ(assignment):
        if assignment.orgao is not None:
            return assignment.orgao.nome
        else:
            return "N/C"

    def get_workplace_name(assignment, date_range):
        workplace = (
            assignment.servidor.servidor_lotacao.filter(
                data_vigencia_inicio__lte=date_range.end_date
            )
            .order_by("data_vigencia_inicio")
            .last()
        )

        if workplace is not None and workplace.lotacao is not None:
            workplace_name = workplace.lotacao.nome
            return workplace_name
        else:
            return "N/C"

    def get_onus(assignment):
        if assignment.onus == 2:
            return True
        else:
            return False

    def get_deadline(assignment):
        if assignment.data_fim is not None:
            return assignment.data_fim.strftime("%d/%m/%Y")

    def get_act_number(collaborator, date_range):
        end_date = date_range.end_date
        possession = (
            collaborator.posses.filter(data_exercicio__lte=end_date)
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            act_number = (
                publication.numero
                if (
                    "00000" not in publication.numero
                    and "S/N" not in publication.numero
                )
                else "SN"
            )
            return act_number

        else:
            return "SN"

    def get_act_year(collaborator, date_range):
        end_date = date_range.end_date
        possession = (
            collaborator.posses.filter(data_exercicio__lte=end_date)
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            act_year = (
                publication.ano
                if ("00000" not in publication.ano and "S/N" not in publication.ano)
                else "SN"
            )
            return act_year

        else:
            return "SN"

    @classmethod
    def load(self, from_to, year_filter, month_filter):

        from_to = int(from_to)
        year_filter = int(year_filter)
        month_filter = int(month_filter)

        date_filter = NewDateRange(None, datetime.date.today())

        if year_filter and month_filter:
            date_filter = NewDateRange.from_month(year_filter, month_filter)

        from_mp = AfastamentoOutroOrgao.objects.currents_in(range=date_filter)
        to_mp = MovimentacaoRequisicao.objects.currents_in(range=date_filter)

        if from_to == 1: 

            for assignment in from_mp.order_by("servidor__pessoa_fisica__nome"):

                PMAssignedEmployeesCache.objects.update_or_create(
                    registration=assignment.servidor.matricula,
                    month=month_filter,
                    year=year_filter,
                    defaults={
                        "name": assignment.servidor.pessoa_fisica.nome,
                        "original_role": self.get_current_role(assignment, date_filter),
                        "current_role": "N/C",
                        "comission_role": self.get_comission_role(
                            assignment, date_filter
                        ),
                        "ordinance_number_assignment": self.get_ordinance_number(
                            assignment
                        ),
                        "ordinance_year_assignment": self.get_ordinance_year(
                            assignment
                        ),
                        "publication_date_assignment": self.get_publication_date(
                            assignment
                        ),
                        "original_organ": "N/C",
                        "target_organ": self.get_target_organ(assignment)
                        if from_to == 2
                        else "N/C",
                        "workplace": self.get_workplace_name(assignment, date_filter),
                        "from_mp": True,
                        "onus_mp": False if self.get_onus(assignment) == 1 else True,
                        "deadline": self.get_deadline(assignment),
                        "updated": True,
                    },
                )

            for assignment in to_mp.order_by("servidor__pessoa_fisica__nome"):

                PMAssignedEmployeesCache.objects.update_or_create(
                    registration=assignment.servidor.matricula,
                    month=month_filter,
                    year=year_filter,
                    defaults={
                        "name": assignment.servidor.pessoa_fisica.nome,
                        "original_role": self.get_original_role(assignment),
                        "current_role": self.get_current_role(assignment, date_filter),
                        "comission_role": self.get_comission_role(
                            assignment, date_filter
                        ),
                        "ordinance_number_assignment": self.get_ordinance_number(
                            assignment
                        ),
                        "ordinance_year_assignment": self.get_ordinance_year(
                            assignment
                        ),
                        "publication_date_assignment": self.get_publication_date(
                            assignment
                        ),
                        "original_organ": self.get_original_organ(assignment),
                        "target_organ": "N/C",
                        "workplace": self.get_workplace_name(assignment, date_filter),
                        "from_mp": False,
                        "onus_mp": False if self.get_onus(assignment) == 2 else True,
                        "deadline": self.get_deadline(assignment),
                        "updated": True,
                    },
                )

        else:

            if from_to == 2:  
                assignments = from_mp

            elif from_to == 3: 
                assignments = to_mp

            for assignment in assignments.order_by("servidor__pessoa_fisica__nome"):

                PMAssignedEmployeesCache.objects.update_or_create(
                    registration=assignment.servidor.matricula,
                    month=month_filter,
                    year=year_filter,
                    defaults={
                        "name": assignment.servidor.pessoa_fisica.nome,
                        "original_role": self.get_original_role(assignment)
                        if from_to == 3
                        else self.get_current_role(assignment, date_filter),
                        "current_role": self.get_current_role(assignment, date_filter)
                        if from_to == 3
                        else "N/C",
                        "comission_role": self.get_comission_role(
                            assignment, date_filter
                        ),
                        "ordinance_number_assignment": self.get_ordinance_number(
                            assignment
                        ),
                        "ordinance_year_assignment": self.get_ordinance_year(
                            assignment
                        ),
                        "publication_date_assignment": self.get_publication_date(
                            assignment
                        ),
                        "original_organ": self.get_original_organ(assignment)
                        if from_to == 3
                        else "MINISTÉRIO PÚBLICO DO ESTADO DO TOCANTINS",
                        "target_organ": self.get_target_organ(assignment)
                        if from_to == 2
                        else "MINISTÉRIO PÚBLICO DO ESTADO DO TOCANTINS",
                        "workplace": self.get_workplace_name(assignment, date_filter),
                        "from_mp": True if from_to == 2 else False,
                        "onus_mp": False
                        if (from_to == 2 and self.get_onus(assignment) == 1)
                        or (from_to == 3 and self.get_onus(assignment) == 2)
                        else True,
                        "deadline": self.get_deadline(assignment),
                        "updated": True,
                    },
                )


class PMCollaboratorsCache(AuditTimestampModel):
    name = models.CharField(
        max_length=100, verbose_name="Nome", default="", blank=False
    )
    cathegory = models.CharField(
        max_length=100, verbose_name="Categoria", default="", blank=False
    )
    workplace = models.CharField(max_length=100)
    act_number = models.CharField(
        verbose_name="Número do ato (Nomeação/Designação)",
        max_length=20,
        null=True,
        blank=True,
    )
    act_year = models.CharField(
        verbose_name="Ano do ato (Nomeação/Designação)",
        max_length=20,
        null=True,
        blank=True,
    )
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(null=True)
    updated = models.BooleanField(default=False, null=True)

    class Meta:
        unique_together = ["name", "month", "year"]

    def __str__(self):
        return f"{self.name} - {self.cathegory}"

    def get_cathegory(collaborator):
        collaborator_type = collaborator.tipo
        type_by_possession = collaborator.type_by_possession
        if collaborator_type == "V" or type_by_possession == "VOL":
            return "VOLUNTÁRIO"
        else:
            return "N/C"

    def get_workplace(collaborator, date_range):
        workplace = (
            collaborator.servidor_lotacao.filter(
                data_vigencia_inicio__lte=date_range.end_date
            )
            .order_by("data_vigencia_inicio")
            .last()
        )
        if workplace is not None and workplace.lotacao is not None:
            workplace_name = workplace.lotacao.nome
            return workplace_name
        else:
            return "N/C"

    def get_act_number(collaborator, date_range):
        end_date = date_range.end_date
        possession = (
            collaborator.posses.filter(data_exercicio__lte=end_date)
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            act_number = (
                publication.numero
                if (
                    "00000" not in publication.numero
                    and "S/N" not in publication.numero
                )
                else "SN"
            )
            return act_number

        else:
            return "SN"

    def get_act_year(collaborator, date_range):
        end_date = date_range.end_date
        possession = (
            collaborator.posses.filter(data_exercicio__lte=end_date)
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            act_year = (
                publication.ano
                if ("00000" not in publication.ano and "S/N" not in publication.ano)
                else "SN"
            )
            return act_year

        else:
            return "SN"

    @classmethod
    def load(self, year_filter, month_filter):

        year_filter = int(year_filter)
        month_filter = int(month_filter)

        date_filter = NewDateRange(None, datetime.date.today())

        if year_filter and month_filter:
            date_filter = NewDateRange.from_month(year_filter, month_filter)

        collaborators = Servidor.objects.active_in(date_range=date_filter).filter(
            type_by_possession="VOL"
        )

        for collaborator in collaborators.order_by("pessoa_fisica__nome"):

            PMCollaboratorsCache.objects.update_or_create(
                name=collaborator.pessoa_fisica.nome,
                month=month_filter,
                year=year_filter,
                defaults={
                    "cathegory": self.get_cathegory(collaborator),
                    "workplace": self.get_workplace(collaborator, date_filter),
                    "act_number": self.get_act_number(collaborator, date_filter),
                    "act_year": self.get_act_year(collaborator, date_filter),
                    "updated": True,
                },
            )

class PMEmployeesGratifComisCache(AuditTimestampModel):
    registration = models.CharField(
        db_index=True, max_length=50, null=True, blank=True, verbose_name="Matrícula"
    )
    name = models.CharField(
        max_length=100, verbose_name="Nome", default="", blank=False
    )
    bond = models.CharField(
        max_length=100, verbose_name="Vínculo", default="", blank=False
    )
    comission_role = models.CharField(max_length=100, verbose_name="Gratificação", null=True, blank=True)
    workplace = models.CharField(max_length=100, verbose_name="Lotação", default="", blank=False)
    ordinance_number_nomination = models.CharField(
        verbose_name="Número do ato (Nomeação)",
        max_length=20,
        null=True,
        blank=True,
    )
    ordinance_year_nomination = models.CharField(
        verbose_name="Ano do ato (Nomeação)",
        max_length=20,
        null=True,
        blank=True,
    )
    publication_date_nomination = models.CharField(
        verbose_name="Data da publicação - Nomeação",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(null=True)
    is_member = models.BooleanField(default=False) 
    updated = models.BooleanField(default=False, null=True)

    class Meta:
        unique_together = ["registration", "month", "year"]

    def __str__(self):
        return f"{self.registration} - {self.name}"

    def get_bond(employee, date_range):
        end_date = date_range.end_date
        if (employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="EF",
                data_exercicio__lte=end_date,
            )):
            return "CONCURSADO PARA O ÓRGÃO"
        
        elif (employee.posses.filter(
                quadro__cargo__tipo_lei_cargo="AC",
                data_exercicio__lte=end_date,
            )):
            return "CEDIDO DE OUTRO ÓRGÃO"

        else:
            return "SEM VÍNCULO"

    def get_comission_role(employee, date_range):
        end_date = date_range.end_date
        comission_role = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )
        if (
            comission_role is not None
            and comission_role.quadro is not None
            and comission_role.quadro.cargo is not None
        ):
            comission_role = comission_role.quadro.cargo.nome
            return comission_role
        else:
            return "N/C"

    def get_workplace_name(employee, date_range):
        workplace = (
            employee.servidor_lotacao.filter(
                designacao=False, data_vigencia_inicio__lte=date_range.end_date
            )
            .order_by("data_vigencia_inicio")
            .last()
        )
        if workplace is not None and workplace.lotacao is not None:
            workplace_name = workplace.lotacao.nome
            return workplace_name
        else:
            return "N/C"

    def get_ordinance_number_nomination(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            ordinance_number = (
                publication.numero
                if (
                    "00000" not in publication.numero
                    and "S/N" not in publication.numero
                )
                else "SN"
            )
            return ordinance_number
            
        else:
            return "SN"

    def get_ordinance_year_nomination(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            ordinance_year = (
                publication.ano
                if ("00000" not in publication.ano and "S/N" not in publication.ano)
                else "SN"
            )
            return ordinance_year
        else:
            return "SN"

    def get_publication_date_nomination(employee, date_range):
        end_date = date_range.end_date
        possession = (
            employee.posses.filter(
                quadro__cargo__tipo_lei_cargo__in=["FC", "CM", "EL"],
                data_exercicio__lte=end_date,
            )
            .order_by("data_exercicio")
            .last()
        )

        if possession is not None and possession.publicacao_movimentacao is not None:
            publication = possession.publicacao_movimentacao
            date = publication.data_publicacao

            if date is not None:
                return date
            else:
                return None

        else:
            return None

    @classmethod
    def load(self, is_member, year_filter, month_filter):

        employee_types = ["EFC", "ECM", "CMS", "RCM", "RFC", "EFE", "REQ", "REX"]
        member_types = ["MCM", "MEC", "MCM2", "MEC2", "MBR", "MBR2", "MAP"]

        date_filter = NewDateRange(None, datetime.date.today())

        if year_filter and month_filter:
            date_filter = NewDateRange.from_month(year_filter, month_filter)

        possessions = MovimentacaoPosse.objects.assets_in(range=date_filter).by_type(["FC", "CM", "EL"]).order_by('servidor__pessoa_fisica__nome')
        
        if is_member == 1:  
            possessions = possessions.filter(
                servidor__type_by_possession__in=employee_types + member_types
            )

        elif is_member == 2:  
            possessions = possessions.filter(servidor__type_by_possession__in=employee_types)

        elif is_member == 3:  
            possessions = possessions.filter(servidor__type_by_possession__in=member_types)

        for possession in possessions.order_by('servidor__pessoa_fisica__nome'):

            PMEmployeesGratifComisCache.objects.update_or_create(
                registration=possession.servidor.matricula,
                month=month_filter,
                year=year_filter,
                defaults={
                    'name': possession.servidor.pessoa_fisica.nome,
                    'bond': self.get_bond(possession.servidor, date_filter),
                    'is_member': True if possession.servidor.type_by_possession in member_types else False,
                    'comission_role': self.get_comission_role(possession.servidor, date_filter),
                    'workplace': self.get_workplace_name(possession.servidor, date_filter),
                    'ordinance_number_nomination': self.get_ordinance_number_nomination(possession.servidor, date_filter),
                    'ordinance_year_nomination': self.get_ordinance_year_nomination(possession.servidor, date_filter),
                    'publication_date_nomination': self.get_publication_date_nomination(possession.servidor, date_filter),
                    'month': month_filter,
                    'year': year_filter,
                    'updated': True
                },
            )


class PMTraineesCache(AuditTimestampModel): 

    """Sumary:Folha de pagamento dos estagiários

    Returns:
        type(Estagiario): _description_:Verificação dos estagiários:
                                        especialidade,nome,levelupdate
    """

    name = models.CharField(
        max_length=100, verbose_name="Nome", default="", blank=False
    )
    level = models.CharField(
        max_length=100, verbose_name="Nível", default="", blank=False
    )
    specialty = models.CharField(max_length=100, verbose_name="Especialidade", null=True, blank=True)
    deadline = models.CharField(
        verbose_name="Prazo",
        default="",
        max_length=10,
        null=True,
        blank=True,
    )
    month = models.PositiveIntegerField(verbose_name="Mês", null=True)
    year = models.PositiveIntegerField(verbose_name="Ano", null=True)
    is_mandatory = models.BooleanField(default=False) 
    updated = models.BooleanField(default=False, null=True)

    class Meta:
        unique_together = ["name", "month", "year"]

    def __str__(self):
        return f"{self.name} - {self.level}"

    def get_level(possession):
        level = possession.level
        if level == 2:
            return "ENSINO MÉDIO"

        else:
            return "ENSINO SUPERIOR"

    def get_specialty(possession):
        if possession.occupation_area is not None:
            specialty = possession.occupation_area
            return specialty if specialty != "" else "N/C"

        else:
            if possession.education_institution is not None:
                specialty = possession.educational_institution
                return specialty if specialty != "" else "N/C"

    def get_deadline(possession):
        if possession.data_desligamento:
            deadline = possession.data_desligamento
            return deadline

        else:
            return None

    @classmethod
    def load(self, year_filter, month_filter):

        date_filter = NewDateRange(None, datetime.date.today())

        if year_filter and month_filter:
            date_filter = NewDateRange.from_month(year_filter, month_filter)

        possessions = PossessionTrainee.objects.assets_in(range=date_filter).filter(level__in=[2, 4])

        for possession in possessions.order_by('servidor__pessoa_fisica__nome'):

            PMTraineesCache.objects.update_or_create(
                name=possession.servidor.pessoa_fisica.nome,
                month=month_filter,
                year=year_filter,
                defaults={
                    'level': self.get_level(possession),
                    'specialty': self.get_specialty(possession),
                    'deadline': self.get_deadline(possession),
                    'is_mandatory': True if possession.nature == 1 else False,
                    'updated': True,
                },
            )
