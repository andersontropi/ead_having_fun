from django.shortcuts import render, redirect, reverse
from .models import Aula, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario esta autenticado:
            # redireciona para a homeaulas
            return redirect('aula:dashboard')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('aula:login')
        else:
            return reverse('aula:criarconta')


class Homeaulas(LoginRequiredMixin, ListView):
    template_name = "dashboard.html"
    model = Aula
    # object_list -> lista de itens do modelo


class Detalhesaula(LoginRequiredMixin, DetailView):
    template_name = "detalhesaula.html"
    model = Aula
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        aula = self.get_object()
        aula.visualizacoes += 1
        aula.save()
        usuario = request.user
        usuario.aulas_vistos.add(aula)
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesaula, self).get_context_data(**kwargs)
        # filtrar a minha tabela de aulas pegando os aulas cuja categoria é igual a categoria do aula da página (object)
        # self.get_object()
        aulas_relacionados = Aula.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["aulas_relacionados"] = aulas_relacionados
        return context


class Pesquisaaula(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Aula

    #object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('aula:dashboard')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('aula:login')

    #def homepage(request):
     #   return render(request, "homepage.html")

# url - view - html
    #def homeaulas(request):
    #   context = {}
    #   lista_aulas = aula.objects.all()
    #   context['lista_aulas'] = lista_aulas
    #   return render(request, "homeaulas.html", context)