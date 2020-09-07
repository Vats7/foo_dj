from django.contrib import admin
from django.urls import path, include
from user import views


urlpatterns = [
    path('', views.index, name='userindex'),
    #path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    #path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
]