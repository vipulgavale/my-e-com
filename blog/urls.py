from blog import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='blog-index')
]
