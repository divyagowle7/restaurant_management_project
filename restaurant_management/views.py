#home/views.py
from rest_framework import generics
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryList(generics.ListAPIView):
    """
    API endponit to retrieve all menu categories.
    """
    #Define the queryset to retreive all MenyCategory instances
    queryset = MenuCategory.objects.all()
    #Specify the serializer to use for MenuCategory instances
    serializer_class = MenuCategorySerializer
    