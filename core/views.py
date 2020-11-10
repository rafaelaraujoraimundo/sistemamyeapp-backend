from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from core.carrega_modulos import carrega_modulo
from core.valida_perfil import valida_perfil


@login_required(login_url="/login/")
def index(request):
    context = {'usuario': request.user, 'segment': 'index'}

    if valida_perfil(request.user, 1):
        context['DASHBOARD'] = True
    else:
        context['DASHBOARD'] = False

    if valida_perfil(request.user, 2):
        context['CUSTOS'] = True
    else:
        context['CUSTOS'] = False
    salarioM = 24
    salarioF = 30
    idadeM = 45
    idadeF = 80
    context.update({'salarioM': salarioM, 'salarioF': salarioF, 'idadeM': idadeM, 'idadeF': idadeF})
    modulo = carrega_modulo('TODOS', request.user)
    context.update(modulo)
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

@login_required()
def pages(request):
    context = {'usuario': request.user}
   
    if valida_perfil(request.user, 1):
        context['DASHBOARD'] = True
    else:
        context['DASHBOARD'] = False

        # Valida se o usuario tem acesso ao modulo de Custos ID = 2
    if valida_perfil(request.user, 2):
        context['CUSTOS'] = True
    else:
        context['CUSTOS'] = False
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        # carrega os modulos
        modulo = {}
        load_modulo = request.path.split('/')[1]
        modulo = carrega_modulo(load_modulo, request.user)
        context.update(modulo)
        # ##################
        load_template = request.path[1:]
        context['segment'] = load_template
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


