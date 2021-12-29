from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('produto/', views.produto, name='produto'),
    path('produto/formulario/', views.form_produto, name='form_produto'),
    path('produto/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produto/remover/<int:pk>/', views.remover_produto, name='remover_produto'),
    path('produto/detalhes/<int:pk>/', views.detalhes_produto, name='detalhes_produto')

]
