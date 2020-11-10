from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from core.carrega_modulos import carrega_modulo
from .forms import NotaFilialForm, NotaFilialFormEx

from core.valida_perfil import valida_perfil
from .models import NotaFilial


@login_required()
def notafilialCreate(request):
    context = {'usuario': request.user}
    context['DASHBOARD'] = valida_perfil(request.user, 1)
    context['CUSTOS'] = valida_perfil(request.user, 2)

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        form = NotaFilialForm(request.POST or None)
        if form.is_valid():
            modulo = {}
            notafilial = form.save(commit=False)
            notafilial.idempresa = request.user.idempresa
            notafilial.idfilial = request.user.idfilial
            notafilial.save()
            modulo = carrega_modulo('av-cadastro', request.user)
            context.update(modulo)
            load_template = 'av-cadastro/notafilial/list.html'
            html_template = loader.get_template(load_template)
            return HttpResponse(html_template.render(context, request))

        context['form'] = form
        return render(request, 'av-cadastro/notafilial/notafilial_form.html', context)


    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required()
def notafilialedit(request, id):
    notafilial = get_object_or_404(NotaFilial, id=id)
    context = {'usuario': request.user, 'DASHBOARD': valida_perfil(request.user, 1),
               'CUSTOS': valida_perfil(request.user, 2)}
    if request.method == "POST":
        form = NotaFilialForm(request.POST, instance=notafilial)
        if form.is_valid():
            form.save()
            notafilial = NotaFilial.objects.all()
            context.update({'notafilial': notafilial})
            return render(request, 'av-cadastro/notafilial/list.html', context)
    else:
        form = NotaFilialForm(instance=notafilial)
        context.update({'form': form})
        return render(request, 'av-cadastro/notafilial/notafilial_edit.html', context)


@login_required()
def notafilialdelete(request, id):
    notafilial = get_object_or_404(NotaFilial, id=id)
    context = {'usuario': request.user, 'DASHBOARD': valida_perfil(request.user, 1),
               'CUSTOS': valida_perfil(request.user, 2)}
    if request.method == "POST":
        notafilial.delete()
        notafilial = NotaFilial.objects.all()
        context.update({'notafilial': notafilial})
        return render(request, 'av-cadastro/notafilial/list.html', context)
    else:
        form = NotaFilialFormEx(instance=notafilial)
        context.update({'form': form})
        return render(request, 'av-cadastro/notafilial/notafilial_delete.html', context)
