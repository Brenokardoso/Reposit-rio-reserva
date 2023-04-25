# -*- coding:utf-8 -*-

import importlib
from django import apps


class AppConfig(apps.AppConfig):
    name = 'library'

    controllers = [
        'library.api.author',
        'library.api.book',
        'library.api.category',
        'library.api.bookleads',
        'library.api.bookevents',
        'library.api.carreiraestrutura',
        

        
    ]
    
    def ready(self):
        register_statics()
        # carregar qualquer outra coisa necessária ao app



def connect_signals():
   
    pass


def register_statics():
    Application = importlib.import_module('default.views').Application

    js_paths = (
        #sempre que eu mexer aqui rodar o dkrestart minifier
        "/%(context)s/static/library/author/Grid.js",
        "/%(context)s/static/library/author/Manage.js",
        "/%(context)s/static/library/author/Restful.js",
        "/%(context)s/static/library/author/Window.js",



        "/%(context)s/static/library/book/Restful.js",
        "/%(context)s/static/library/book/Window.js",
        "/%(context)s/static/library/book/Grid.js",
        "/%(context)s/static/library/book/Manage.js",



        "/%(context)s/static/library/category/Restful.js",
        "/%(context)s/static/library/category/Window.js",
        "/%(context)s/static/library/category/Grid.js",
        "/%(context)s/static/library/category/Manage.js",
 
 
 
        "/%(context)s/static/library/bookleads/Restful.js",
        "/%(context)s/static/library/bookleads/Window.js",
        "/%(context)s/static/library/bookleads/Grid.js",
        "/%(context)s/static/library/bookleads/Manage.js",
 
 
 
        "/%(context)s/static/library/bookevents/Restful.js",
        "/%(context)s/static/library/bookevents/Window.js",
        "/%(context)s/static/library/bookevents/Grid.js",
        "/%(context)s/static/library/bookevents/Manage.js",


        "/%(context)s/static/library/CarreiraEstrutura/Restful.js",
        "/%(context)s/static/library/CarreiraEstrutura/Window.js",
        "/%(context)s/static/library/CarreiraEstrutura/Grid.js",
        "/%(context)s/static/library/CarreiraEstrutura/Manage.js",







    )

    for path in js_paths:
        Application.register_javascript(path, scope='library')
