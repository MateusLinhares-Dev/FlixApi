from django.urls import path
#boa prática usar nesse formato
from . import views


urlpatterns = [

    path('genres/', views.GenreCreateListView.as_view(), name='genre_creat_list'),
    #passar o id da tabela para retornar o dado especificado.
    path('genres/<int:pk>', views.GenereRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),
]
