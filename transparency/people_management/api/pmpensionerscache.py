# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMPensionersCache

log = getLogger(__name__)


class TPMPensionersCache(RestfulDRY):
    """_summary_:Pensionistas

    Args:
        RestfulDRY (Pensão): Servidores e/ou ex-Servidores que recebem penção
        
    """

    _model = PMPensionersCache

    full_text_index = (
        "name_founder__icontains",
        "name_pensioner__icontains",
        "effective_role__icontains",
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {
            'success': True,
            'message': 'Nada feito ainda.'
        }

        try:

            year_filter =  self.request.POST.get('ano')
            month_filter = self.request.POST.get('mes')

            self._model.load(
                year_filter,
                month_filter
            )

        except Exception as e:
            obj.update(
                success=False,
                message=str("TESTE")
            )
        else:
            obj.update(
                message='Dados gravados com sucesso.'
            )
        self.renderer(obj)

    def json(self, args=[]):
        self.response['content-type'] = 'text/javascript'
        self.response.write('Ext._create("transparency.people_management.pensioners.Manage")')

