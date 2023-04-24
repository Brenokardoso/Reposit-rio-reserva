# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMEmployeesGratifComisCache

log = getLogger(__name__)

class TPMEmployeesMembersGratifComisCache(RestfulDRY):
    """Summary:Servidores e membros gratificados 

    Args:
        RestfulDRY (Servidores): Cache dos servidores e mebros gratificados do MP

    Returns:
        __str__ = _description_
    """

    _model = PMEmployeesGratifComisCache

    full_text_index = (
        "registration__icontains",
        "name__icontains",
        "comission_role__icontains",
        "workplace__icontains",
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {"success": True, "message": "Nada feito ainda."}

        try:

            is_member = int(self.request.POST.get("tipo"))
            year_filter = int(self.request.POST.get("ano"))
            month_filter = int(self.request.POST.get("mes"))

            self._model.load(is_member, year_filter, month_filter)

        except Exception as e:
            obj.update(success=False, message=str("TESTE"))
        else:
            obj.update(message="Dados gravados com sucesso.")
        self.renderer(obj)

    def json(self, args=[]):
        self.response["content-type"] = "text/javascript"
        self.response.write(
            'Ext._create("transparency.people_management.employees_members_gratif_comis.Manage")'
        )

    def model_to_dict(self, instance):
        _dict_ = super().model_to_dict(instance)

        _dict_.update({
            'ordinance_nomination': f'{instance.ordinance_number_nomination}/{instance.ordinance_year_nomination}' if instance.ordinance_number_nomination or instance.ordinance_year_n else '',
        })

        return _dict_