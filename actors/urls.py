from django.urls import path
#boa prática usar nesse formato
from . import views

urlpatterns = [
        path('actors/', views.ActorCreateListView.as_view(), name='actor_detail_view'),
        #passar o id da tabela para retornar o dado especificado.
        path('actors/<int:pk>', views.ActorUpdateRetrieveDestroyView.as_view(), name='actor_create_view'),


]