from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_service/', views.add_service, name='add_service'),
    path('cars/<int:car_id>/assoc_show/<int:show_id>/', views.assoc_show, name='assoc_show'),
    path('shows/', views.ShowList.as_view(), name='shows_index'),
    path('shows/<int:pk>/', views.ShowDetail.as_view(), name='show_detail'),
    path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
    path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
    path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),    
]