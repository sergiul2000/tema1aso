from rest_framework.viewsets import ModelViewSet
from scrumboard.serielizers import ListSerializer, CardSerielizers
from scrumboard.models import List,Card

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerielizers