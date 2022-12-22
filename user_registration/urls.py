from django.urls import path
from . import views

urlpatterns = [
    path ('', views.user_signup,name="user_signup"),
    path ('login/', views.user_login,name="user_login"),
    path ('profile/', views.user_profile,name="user_profile"),
    path('logout/',views.user_logout,name='user_logout'),
    path('changepass/',views.changepass1,name='user_change_pass'),
    path('userprofile/<int:id>',views.User_details,name='userdetail'),
]
