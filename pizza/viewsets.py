from rest_framework import viewsets

from .models import Pizza, Likes, Pizzeria
from .serializers import PizzaSerializer, LikeSerializer, PizzeriaSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzeriaViewSet(viewsets.ModelViewSet):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer