from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenereRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorUpdateRetrieveDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrivierDestroyUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre_creat_list'),
    #passar o id da tabela para retornar o dado especificado.
    path('genres/<int:pk>', GenereRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),

    path('actors/', ActorCreateListView.as_view(), name='actor_detail_view'),
    #passar o id da tabela para retornar o dado especificado.
    path('actors/<int:pk>', ActorUpdateRetrieveDestroyView.as_view(), name='actor_create_view'),

    path('movies/', MovieCreateListView.as_view(), name='movie_detail_view'),
    #passar o id da tabela do tipo inteiro para retornar o dado especificado.
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie_create_view'),

    path('review/', ReviewCreateListView.as_view(), name='review_detail_view'),
    #passar o id da tabela do tipo inteiro para retornar o dado especificado.
    path('review/<int:pk>', ReviewRetrivierDestroyUpdate.as_view(), name='review_create_view'),
]
