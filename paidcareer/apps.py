import importlib
from django.apps import AppConfig


class PaidCareerConfig(AppConfig):

    name = "paidcareer"

    controllers = [
       'paidcareer.api.pmcareermorestructure'
       
    ]

    def ready(self):
        register_statics()
        connect_signals()


def connect_signals():
    pass


def register_statics():
    
    

    Application = importlib.import_module("default.views").Application

    js_paths = (
       
       '/%(context)s/static/paidcarer/careerandstructure/Grid.js',
       '/%(context)s/static/paidcarer/careerandstructure/Manage.js',
       '/%(context)s/static/paidcarer/careerandstructure/Restful.js',
       '/%(context)s/static/paidcarer/careerandstructure/Window.js',

       

       #'/%(context)s/static/paidcarer/servidores/Grid.js',
       #'/%(context)s/static/paidcarer/servidores/Manage.js',
       #'/%(context)s/static/paidcarer/servidores/Restful.js',
       #'/%(context)s/static/paidcarer/servidores/Window.js',

       # '/%(context)s/static/paidcarer/cargoscomissionados/Grid.js',
       #'/%(context)s/static/paidcarer/cargoscomissionados/Manage.js',
       #'/%(context)s/static/paidcarer/cargoscomissionados/Restful.js',
       #'/%(context)s/static/paidcarer/cargoscomissionados/Window.js',
                     

      
   
   )

    for path in js_paths:
        Application.register_javascript(path, scope="paidcareer")
