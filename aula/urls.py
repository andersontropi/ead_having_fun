# url - view - template
from django.urls import path, reverse_lazy
from .views import Homeaulas, Homepage, Detalhesaula, Pesquisaaula, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view
#import django.urls.exceptions.NoReverseMatch
#from . import views

app_name = 'aula'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('dashboard/', Homeaulas.as_view(), name='dashboard'),
    path('aulas/<int:pk>/', Detalhesaula.as_view(), name='detalhesaula'),
    #path('detalhesaula/<int:pk>/', views.detalhesaula, name='detalhesaula'),
    path('pesquisa/', Pesquisaaula.as_view(), name='pesquisaaula'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('aula:dashboard')), name='mudarsenha'),
]