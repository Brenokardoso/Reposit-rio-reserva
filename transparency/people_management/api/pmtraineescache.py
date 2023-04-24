# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMTraineesCache

log = getLogger(__name__)

class TPMTraineesCache(RestfulDRY):
    """_Summary_:Todos os estágiarios do MP e seus contratos

    Args:
        RestfulDRY (Estagio): _description_:Quadro dos estagiários
    """

    _model = PMTraineesCache

    full_text_index = (
        "name__icontains",
        "specialty__icontains"
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {"success": True, "message": "Nada feito ainda."}

        try:

            year_filter = int(self.request.POST.get("ano"))
            month_filter = int(self.request.POST.get("mes"))

            self._model.load(year_filter, month_filter)

        except Exception as e:
            obj.update(success=False, message=str("TESTE"))
        else:
            obj.update(message="Dados gravados com sucesso.")
        self.renderer(obj)

    def json(self, args=[]):
        self.response["content-type"] = "text/javascript"
        self.response.write(
            'Ext._create("transparency.people_management.trainees.Manage")'
        )