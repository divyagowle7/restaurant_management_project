from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
# Create your views here.
class MenuItemPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'

class MenuCategoryList(generics.ListAPIView):
    queryset=MenuCategory.objects.filter(is_featured=True)
    serializer_class=MenuCategorySerializer

class MenuItemVieewSet(viewsets.ModelViewSet):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer
    pagination_class=MenuItemPagination

    def get_queryset(self):
        queryset=super().get_queryset()
        search_query=self.request.query_params.get('search',None)
        if search_query:
            queryset=queryset.filter(name__icontains=search_query)
        return queryset
        