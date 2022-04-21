from django.urls import path
from . import views


app_name = 'anonymous'

urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/create/', views.create_comment, name='create_comment'),
    path('<int:pk>/delete/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('<int:pk>/like/', views.like_article, name='like_article'),

]