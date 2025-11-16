from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryList,MenuItemViewSet
from . import views

router=DefaultRouter()
router.register(r'menu-items',MenuItemViewSet)
urlpatterns = [
    path('api/menu-categories-list/',MenuCategoryList.as_view()),
    path('api/menu-items/<int:pk>/ingredients/',views.MenuItemIngredientsView.as_view()),
    path('',include(router.urls)),
]