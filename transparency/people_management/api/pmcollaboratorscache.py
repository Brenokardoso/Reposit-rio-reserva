# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMCollaboratorsCache

log = getLogger(__name__)


class TPMCollaboratorsCache(RestfulDRY):
    """Summary:Colaboradores

    Args:
        RestfulDRY (Colaboradores): Quadro dos colaboradores
    """

    _model = PMCollaboratorsCache

    full_text_index = (
        "name__icontains",
        "cathegory__icontains",
        "workplace__icontains",
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {
            'success': True,
            'message': 'Nada feito ainda.'
        }

        try:

            year_filter =  self.request.POST.get('year')
            month_filter = self.request.POST.get('month')

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
        self.response.write('Ext._create("transparency.people_management.collaborators.Manage")')

