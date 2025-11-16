from django.shortcuts import render
from rest_framework import generics,viewsets,status
from .models import MenuCategory,MenuItem
from .serializers import MenuCategorySerializer,MenuItemSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.
class MenuItemPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'

class MenuCategoryList(generics.ListAPIView):
    queryset=MenuCategory.objects.filter(is_featured=True)
    serializer_class=MenuCategorySerializer

class MenuItemIngredientsView(generics.RetrieveAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    lookup_field='pk'
    
class MenuItemVieewSet(viewsets.ModelViewSet):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuItemSerializer
    pagination_class=MenuItemPagination
    permission_classes=[IsAdminUser]

    def update(self,request,pk=None):
        try:
            menu_item=self.get_object()
            serializer=self.get_seializer(menu_item,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except MenuItem.DoesNotExist:
            return Response({'error':'Menu item not found'},status=status.HTTP_400_NOT_FOUND)

            
    def get_queryset(self):
        queryset=super().get_queryset()
        search_query=self.request.query_params.get('search',None)
        if search_query:
            queryset=queryset.filter(name__icontains=search_query)
        return queryset
        