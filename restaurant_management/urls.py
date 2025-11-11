from django.urls import path
from .views import MenuCategoryList
urlpatterns=[
    path('menu-categories/',MenuCategoryList.as_view(),name='menu-categories'),
]