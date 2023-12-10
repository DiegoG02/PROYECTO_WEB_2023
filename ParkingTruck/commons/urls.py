from django.urls import path
from .views import user_login, index, profile_view, registro_view  

urlpatterns = [
    path('login/', user_login, name='login'), 
    path('accounts/profile/', profile_view, name='profile'), 
    path('registro/', registro_view, name='registro'),
    path('', index, name='index'),  

]
