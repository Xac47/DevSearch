from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),

    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),

    path('delete-review/<str:pk>/', views.delete_review, name='delete-review'),

    path('check-likes/<str:pk>/', views.check_likes, name='check-likes'),
    path('check-dislikes/<str:pk>/', views.check_dislikes, name='check-dislikes'),
]