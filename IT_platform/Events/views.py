from django.shortcuts import render
from djoser.serializers import UserSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from unicodedata import category

from Events.models import Event
from Events.serializers import EventSerializer
from Register.models import Profile


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Index(GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    def get(self, request):
        index = EventSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'index.html', context=context)

# def index(request):
#     return render(request, 'index.html')
def test(requst):
    return render(requst, 'personal_account.html')
