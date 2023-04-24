# -*- coding: utf-8 -*-
from contrib.newrest import RestfulDRY
from contrib.utils import getLogger
from transparency.people_management.models import PMAssignedEmployeesCache

log = getLogger(__name__)


class TPMAssignedEmployeesCache(RestfulDRY): 
    """Summary:Servidores Cededidos

    Args:
        RestfulDRY (Servidores):Tipo de servidores cedidos
    """

    _model = PMAssignedEmployeesCache

    full_text_index = (
        "registration__icontains",
        "name__icontains",
        "workplace__icontains",
        "original_role__icontains",
        "current_role__icontains",
        "comission_role__icontains",
        "original_organ__icontains",
        "target_organ__icontains",
    )

    force_upper = True

    def generate_from_solicitations(self, *args):
        obj = {
            'success': True,
            'message': 'Nada feito ainda.'
        }

        try:

            from_to = self.request.POST.get('from_to')
            year_filter =  self.request.POST.get('year')
            month_filter = self.request.POST.get('month')

            if int(from_to) in [2, 3]:
                self._model.load(
                    from_to,
                    year_filter,
                    month_filter
                )

            else:
                self._model.load(
                    '2',
                    year_filter,
                    month_filter
                )
                self._model.load(
                    '3',
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
        self.response.write('Ext._create("transparency.people_management.assigned_employees.Manage")')

