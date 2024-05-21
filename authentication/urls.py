from django.urls import path
from rest_framework_simplejwt import TokenObtainPairView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair')

]