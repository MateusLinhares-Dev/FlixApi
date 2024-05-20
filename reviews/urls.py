from django.urls import path
#boa prática usar nesse formato
from . import views


urlpatterns = [
    path('review/', views.ReviewCreateListView.as_view(), name='review_detail_view'),
        #passar o id da tabela do tipo inteiro para retornar o dado especificado.
    path('review/<int:pk>', views.ReviewRetrivierDestroyUpdate.as_view(), name='review_create_view'),


]