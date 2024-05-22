from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView
    )

#Criar uma url para gerar token a partir da lib JWT
urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #dar refresh 
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #verificar se ainda é valido
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]