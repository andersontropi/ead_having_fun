from .models import Aula


def lista_aulas_recentes(request):
    lista_aulas = Aula.objects.all().order_by('-data_criacao')[0:8]
    if lista_aulas:
        aula_destaque = lista_aulas[0]
    else:
        aula_destaque = None
    return {"lista_aulas_recentes": lista_aulas, "aula_destaque": aula_destaque}


def lista_aulas_emalta(request):
    lista_aulas = Aula.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_aulas_emalta": lista_aulas}