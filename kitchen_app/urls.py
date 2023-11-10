from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/', views.api_view, name='api_view'),
    path('', views.display_view, name='display_view'),
    # path('update-data/', views.update_data, name='update_data'),
    # path('accounts/login/',auth_views.LoginView.as_view(template_name='schair_app/login.html'),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='schair_app/logout.html'),name='logout'),

]