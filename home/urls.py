from django.urls import path
from .views import MenuCategoryList
from . import views

urlpatterns = [
    path('api/menu-categories-list/',MenuCategoryList.as_view()),
    path('api/menu-items/<int:pk>/ingredients/',views.MenuItemIngredientsView.as_view()),
]