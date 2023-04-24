import importlib
from django.apps import AppConfig


class PeopleManagementConfig(AppConfig):
    name = "transparency.people_management"

    controllers = [
        # Aqui devem ser listados os caminhos dos controllers do app. Ex: web.api.cms.metadata
        "transparency.people_management.api.pmemployeescache",
        "transparency.people_management.api.pmpensionerscache",
        "transparency.people_management.api.pmassignedemployeescache",
        "transparency.people_management.api.pmcollaboratorscache",
        "transparency.people_management.api.pmemployeesgratifcomiscache",
        "transparency.people_management.api.pmtraineescache",
    ]

    def ready(self):
        """
        O carregamento de partes necessárias ao app.
        """
        register_statics()
        connect_signals()


def connect_signals():
    pass


def register_statics():
    """O registro dos arquivos estáticos do app deve ser feito aqui.

    Ex:

        Application = importlib.import_module('default.views').Application

        Application.register_javascript('/%(context)s/static/web/js/shortcuts.js')
        Application.register_stylesheet('/%(context)s/static/web/css/styles.css')
    """

    Application = importlib.import_module("default.views").Application

    js_paths = (
        "/%(context)s/static/transparency/people_management/employees_members/Restful.js",
        "/%(context)s/static/transparency/people_management/employees_members/Grid.js",
        #'%(context)s transparency/static/people_management/assigned_employees/Grid.js'
        "/%(context)s/static/transparency/people_management/employees_members/Window.js",
        "/%(context)s/static/transparency/people_management/employees_members/Manage.js",
        "/%(context)s/static/transparency/people_management/employees_members/PMLoadDataWindow.js",

        "/%(context)s/static/transparency/people_management/pensioners/Restful.js",
        "/%(context)s/static/transparency/people_management/pensioners/Grid.js",
        "/%(context)s/static/transparency/people_management/pensioners/Window.js",
        "/%(context)s/static/transparency/people_management/pensioners/Manage.js",
        "/%(context)s/static/transparency/people_management/pensioners/PMLoadDataWindow.js",
        
        "/%(context)s/static/transparency/people_management/assigned_employees/Restful.js",
        "/%(context)s/static/transparency/people_management/assigned_employees/Grid.js",
        "/%(context)s/static/transparency/people_management/assigned_employees/Window.js",
        "/%(context)s/static/transparency/people_management/assigned_employees/Manage.js",
        "/%(context)s/static/transparency/people_management/assigned_employees/PMLoadDataWindow.js",
        
        "/%(context)s/static/transparency/people_management/collaborators/Restful.js",
        "/%(context)s/static/transparency/people_management/collaborators/Grid.js",
        "/%(context)s/static/transparency/people_management/collaborators/Window.js",
        "/%(context)s/static/transparency/people_management/collaborators/Manage.js",
        "/%(context)s/static/transparency/people_management/collaborators/PMLoadDataWindow.js",
        
        "/%(context)s/static/transparency/people_management/employees_members_gratif_comis/Restful.js",
        "/%(context)s/static/transparency/people_management/employees_members_gratif_comis/Grid.js",
        "/%(context)s/static/transparency/people_management/employees_members_gratif_comis/Window.js",
        "/%(context)s/static/transparency/people_management/employees_members_gratif_comis/Manage.js",
        "/%(context)s/static/transparency/people_management/employees_members_gratif_comis/PMLoadDataWindow.js",
        
        "/%(context)s/static/transparency/people_management/trainees/Restful.js",
        "/%(context)s/static/transparency/people_management/trainees/Grid.js",
        "/%(context)s/static/transparency/people_management/trainees/Window.js",
        "/%(context)s/static/transparency/people_management/trainees/Manage.js",
        "/%(context)s/static/transparency/people_management/trainees/PMLoadDataWindow.js",
    
    )

    for path in js_paths:
        Application.register_javascript(path, scope="transparency")
