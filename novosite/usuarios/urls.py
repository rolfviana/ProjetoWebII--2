from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path(
        'patrimonio/cadastrar/',

        views.cadastrar_patrimonio,

        name='cadastrar_patrimonio'
    ),

    path(
        'patrimonios/',

        views.listar_patrimonios,

        name='listar_patrimonios'
    ),

    path(
        'patrimonio/scanner/',

        views.scanear_patrimonio,

        name='scanear_patrimonio'
    ),

    path(
        'editar/<int:id>/',

        views.editar_patrimonio,

        name='editar_patrimonio'
    ),

    path(
        'excluir/<int:id>/',

        views.excluir_patrimonio,

        name='excluir_patrimonio'
    ),

    path(
        'sobre/',

        views.sobre,

        name='sobre'
    ),

    path(
        'contato/',

        views.contato,

        name='contato'
    ),

]
