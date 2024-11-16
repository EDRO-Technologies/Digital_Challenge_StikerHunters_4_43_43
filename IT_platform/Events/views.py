from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from Events.models import Event
from Events.serializers import EventSerializer


class EventAPIList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        return render(request, "index.html")

class EventAPICreate(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        return render(request, 'create_event.html')

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Проверка данных
        serializer.save() # Метод create
        # return Response({"post": serializer.data})
        context = {
            "data": serializer.data,
            "Success_post":"Вы успешно добавили ивент",
        }
        return render(request, 'create_event.html', context=context)

class EventAPIUpdate(UpdateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get(self, request):
        return render(request, 'eventupdate.html')


    def put(self, request):
        index = EventSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'index.html', context=context)

        def put(self, requset, *args, **kwargs):
            pk = kwargs.get("pk", None)
            if not pk:
                return Response({"error": "Method PUT not allowed"})

            try:
                instance = post.objects.get(pk=pk) # проверяем наличие записи
            except:
                return Response({"error": "Object does not exists"})

            serializer = postSerializer(data=requset.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"post": serializer.data})

class EventAPIDelete(DestroyAPIView):
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
