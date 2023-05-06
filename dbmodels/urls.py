from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name="user_login"),
    path('Dashboard/',views.signin, name="signin"),
    path('admin_dash/',views.admin, name="admin"),
]