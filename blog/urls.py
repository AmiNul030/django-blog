from django.urls import path
from . import views

urlpatterns = [
    path('',views.Post_list,name='post_list'),
    path('post/<slug:slug>/',views.Post_detail,name='post_detail'),
]