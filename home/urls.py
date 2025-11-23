from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryList,MenuItemViewSet,TableDetailView,AvailableTablesAPIView
from . import views

router=DefaultRouter()
router.register(r'menu-items',MenuItemViewSet)
urlpatterns = [
    path('api/menu-categories-list/',MenuCategoryList.as_view()),
    path('api/menu-items/<int:pk>/ingredients/',views.MenuItemIngredientsView.as_view()),
    path('',include(router.urls)),
    path('api/tables/<int:pk>/',TableDetailView.as_view(),name='table-detail'),
    path('api/tables/available/',AvailableTablesAPIView.as_view(),name='available_tables_api'),
]