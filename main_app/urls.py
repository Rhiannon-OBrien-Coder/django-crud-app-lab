from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coffees/', views.coffee_index, name='coffee-index'),
    path('coffees/<int:coffee_id>/', views.coffee_detail, name='coffee-detail'),
    path('coffees/create/', views.CoffeeCreate.as_view(), name='coffee-create'),
    path('coffees/<int:pk>/update/', views.CoffeeUpdate.as_view(), name='coffee-update'),
    path('coffees/<int:pk>/delete/', views.CoffeeDelete.as_view(), name='coffee-delete'),
]
