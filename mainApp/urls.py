from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('sell/', views.sell, name='sell'),
    path('cars/', views.cars, name='cars'),
    path('bikes/', views.bikes, name='bikes'),
    path('mobiles/', views.mobiles, name='mobiles'),
    path('applications/', views.applications, name='applications'),
    path('onlycars/',views.onlycars,name='onlycars'),
    path('onlybikes/',views.onlybikes,name='onlybikes'),
    path('onlymobiles/',views.onlymobiles,name='onlymobiles'),
    
    path('message/<int:p_id>/', views.message, name='message'),
    path('product/<str:type>/<int:p_id>/', views.details, name='details'),
    
]
