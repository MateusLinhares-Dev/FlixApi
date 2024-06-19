from django.urls import path
#boa prática usar nesse formato
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie_detail_view'),
    #passar o id da tabela do tipo inteiro para retornar o dado especificado.
    path('movies/<int:pk>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie_create_view'),
    path('movies/stats/', views.MovieStatisView.as_view(), name='movie_stats_view')


]