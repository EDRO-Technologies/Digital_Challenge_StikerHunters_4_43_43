from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from Register.models import Profile
from Register.serializers import ProfileSerializer


class ProfileAPICreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request):
        return render(request, 'create_event.html')

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверка данных
        serializer.save()  # Метод create
        # return Response({"post": serializer.data})
        context = {
            "data": serializer.data,
        }
        return render(request, 'register.html', context=context)

def regitser(reqest):
    return render(reqest, 'secondauthtorization.html')
