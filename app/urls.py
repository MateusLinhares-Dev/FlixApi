from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenereRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre_creat_list'),
    #passar o id da tabela para retornar o dado especificado.
    path('genres/<int:pk>', GenereRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),
]
