# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMEmployeesCache

log = getLogger(__name__)


class TPMEmployeesCache(RestfulDRY):
    """Summary:Servidores e membros

    Args:
        RestfulDRY (Servidor): Quadro dos servidores e membros do MP

    Returns:
        dict str: retorna  aos parametros buscados
    """
    _model = PMEmployeesCache

    full_text_index = (
        "registration__icontains",
        "name__icontains",
        "effective_role__icontains",
        "comission_role__icontains",
        "workplace__icontains",
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {"success": True, "message": "Nada feito ainda."}

        try:

            is_active = self.request.POST.get("situacao")
            classif_employee = self.request.POST.get("tipo")
            year_filter = self.request.POST.get("ano")
            month_filter = self.request.POST.get("mes")

            self._model.load(is_active, classif_employee, year_filter, month_filter)

        except Exception as e:
            obj.update(success=False, message=str("TESTE"))
        else:
            obj.update(message="Dados gravados com sucesso.")
        self.renderer(obj)

    def json(self, args=[]):
        self.response["content-type"] = "text/javascript"
        self.response.write(
            'Ext._create("transparency.people_management.employees_members.Manage")'
        )

    def model_to_dict(self, instance):
        _dict_ = super().model_to_dict(instance)

        _dict_.update({
            'ordinance_retirement': f'{instance.ordinance_number_retirement}/{instance.ordinance_year_retirement}' if instance.ordinance_number_retirement or instance.ordinance_year_retirement else '',
        })

        return _dict_