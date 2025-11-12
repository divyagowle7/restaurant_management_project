from django.urls import path
from .views import MenuCategoryList

urlpatterns = [
    path('appi/menu-categories-list/',MenuCategoryList.as_view()),
]