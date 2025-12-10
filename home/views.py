from django.shortcuts import render
from rest_framework import generics,viewsets,status
from .models import MenuCategory,MenuItem,Table,ContactFormSubmission
from .serializers import MenuCategorySerializer,MenuItemSerializer,TableSerializer,ContactFormSubmissionSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.db.models import Q
from .utils import send_email
from home.utils import get_distinct_cuisines
# Create your views here.
cuisines=get_distinct_cuisines
print(cuisines)
def some_view(request):
    recipient_email="recipient@example.com"
    subject="Test Email"
    message_body="This is a test email"
    send_email(recipient_email,subject,message_body)
    
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

class TableDetailView(generics.RetrieveAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer
    lookup_field='pk'
           
class MenuItemByCategoryView(generics.ListAPIView):
    serializer_class=MenuItemSerializer
    def get_queryset(self):
        category=self.request.query_params.get('category',None)
        if category is not None:
            queryset=MenuItem.objects.filter(category_category_name=category)
        else:
            queryset=MenuItem.objects.none()
        return queryset
class AvailableTablesAPIView(generics,ListAPIView):
    queryset=Table.objects.filter(is_available=True)
    serializer_class=TableSerializer       

class ContactFormSubmissionView(generics.CreateAPIView):
    queryset=ContactFormSubmission.objects.all()
    serializer_class=ContactFormSubmissionSerializer
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer