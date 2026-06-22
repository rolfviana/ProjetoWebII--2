from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

from .models import Patrimonio


# ---------------- LOGIN ---------------- #

def login(request):

    if request.method == 'GET':

        return render(request, 'usuarios/login.html')

    email = request.POST.get('email')

    senha = request.POST.get('senha')

    user = authenticate(
        request,
        username=email,
        password=senha
    )

    if user is not None:

        login_django(request, user)

        return redirect('home')

    else:

        return HttpResponse('E-mail ou senha inválidos.')


# ---------------- CADASTRO DE USUÁRIO ---------------- #

def cadastro(request):

    if request.method == 'GET':

        return render(request, 'usuarios/cadastro.html')

    username = request.POST.get('email')

    email = request.POST.get('email')

    password = request.POST.get('senha')

    first_name = request.POST.get('nome')

    user = User.objects.filter(
        username=username
    ).first()

    if user:

        return HttpResponse(
            'Usuário já existente!'
        )

    else:

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password,

            first_name=first_name

        )

        user.save()

        return redirect('login')


# ---------------- DASHBOARD ---------------- #

def home(request):
    
    total = Patrimonio.objects.count()

    em_uso = Patrimonio.objects.filter(
        status='Em uso'
    ).count()

    manutencao = Patrimonio.objects.filter(
        status='Manutenção'
    ).count()

    inativo = Patrimonio.objects.filter(
        status='Inativo'
    ).count()

    contexto = {

        'total': total,

        'em_uso': em_uso,

        'manutencao': manutencao,

        'inativo': inativo

    }

    return render(

        request,

        'usuarios/home.html',

        contexto

    )


# ---------------- CADASTRAR PATRIMÔNIO ---------------- #

def cadastrar_patrimonio(request):

    if request.method == 'GET':

        return render(

            request,

            'usuarios/cadastrar_patrimonio.html'

        )

    Patrimonio.objects.create(

        numero_tombamento=request.POST.get('tombamento'),

        nome=request.POST.get('nome'),

        categoria=request.POST.get('categoria'),

        localizacao=request.POST.get('localizacao'),

        responsavel=request.POST.get('responsavel'),

        data_aquisicao=request.POST.get('data'),

        valor=request.POST.get('valor'),

        status=request.POST.get('status')

    )

    return redirect('listar_patrimonios')


# ---------------- LISTAR PATRIMÔNIOS ---------------- #

def listar_patrimonios(request):

    filter_by = request.GET.get('filter_by', '')
    search = request.GET.get('search', '').strip()

    filter_fields = {
        'tombamento': 'numero_tombamento',
        'nome': 'nome',
        'categoria': 'categoria',
        'localizacao': 'localizacao',
        'responsavel': 'responsavel',
        'status': 'status',
    }

    patrimonios = Patrimonio.objects.all()

    if filter_by in filter_fields and search:
        lookup = f"{filter_fields[filter_by]}__icontains"
        patrimonios = patrimonios.filter(**{lookup: search})

    return render(

        request,

        'usuarios/listar_patrimonios.html',

        {

            'patrimonios': patrimonios,
            'filter_by': filter_by,
            'search': search,
            'filter_fields': filter_fields,

        }

    )


# ---------------- SCANNER AR ---------------- #

def scanear_patrimonio(request):

    return render(

        request,

        'usuarios/scanear.html'

    )


# ---------------- PÁGINAS INSTITUCIONAIS ---------------- #

def sobre(request):

    return render(

        request,

        'usuarios/sobre.html'

    )


def contato(request):

    return render(

        request,

        'usuarios/contato.html'

    )


# ---------------- EDITAR PATRIMÔNIO ---------------- #

def editar_patrimonio(request, id):

    patrimonio = Patrimonio.objects.get(id=id)

    if request.method == 'GET':

        return render(

            request,

            'usuarios/editar_patrimonio.html',

            {

                'patrimonio': patrimonio

            }

        )

    patrimonio.numero_tombamento = request.POST.get('tombamento')

    patrimonio.nome = request.POST.get('nome')

    patrimonio.categoria = request.POST.get('categoria')

    patrimonio.localizacao = request.POST.get('localizacao')

    patrimonio.responsavel = request.POST.get('responsavel')

    patrimonio.data_aquisicao = request.POST.get('data')

    patrimonio.valor = request.POST.get('valor')
    if patrimonio.valor == "" or patrimonio.valor is None:
        patrimonio.valor = 0

    patrimonio.status = request.POST.get('status')

    patrimonio.save()

    return redirect('listar_patrimonios')


# ---------------- EXCLUIR PATRIMÔNIO ---------------- #

def excluir_patrimonio(request, id):

    patrimonio = Patrimonio.objects.get(id=id)

    patrimonio.delete()

    return redirect('listar_patrimonios')