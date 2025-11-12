from django.shortcuts import render
from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer
# Create your views here.
 class MenuCategoryList(generics.ListAPIView):
    queryset=MenuCategory.objects.filter(is_featured=True)
    serializer_class=MenuCategorySerializer
