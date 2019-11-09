from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signup/post',  views.create, name="create"),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]