from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('menu/', views.menu_page, name='menu_page'),
    path('menu/<slug:slug>/', views.dishes_page, name='dishes_page'),
    path('menu/slug/id/', views.more_dishes_page, name='more_dishes_page'),
    path('aboutus/', views.aboutus_page, name='aboutus_page'),
    path('user/login/', views.login_page, name='login_page'),
    path('user/sign/', views.signup_page, name='signup_page'),
    path('user/logout/', views.logout_req, name='logout_req'),

]