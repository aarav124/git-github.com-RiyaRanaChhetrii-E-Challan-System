from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('add', views.add, name="add"),
    path('edit', views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('signin_traffic', views.signin_traffic, name="signin_traffic"),
    path('traffic_user', views.traffic_user, name="traffic_user"),
    path('add_user', views.add_user, name="add_user"),
    path('edit_user', views.edit_user, name="edit_user"),
    path('update_user/<str:id>', views.update_user, name="update_user"),
    path('pdf', views.pdf, name="pdf"),
    path('traffic_rule', views.traffic_rule, name="traffic_rule")

]