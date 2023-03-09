from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views._login, name='login'),
    path('exit/', views.exit, name='exit'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),

    path('account/', views.account, name='account'),
    path('update-account/', views.update_account, name='update-account'),

    path('create-skill/', views.create_skill, name='create-skill'),
    path('update-skill/<str:pk>/', views.update_skill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.delete_skill, name='delete-skill'),

    path('subscription-check/<str:pk>/', views.subscription_check, name='subscription-check')
]