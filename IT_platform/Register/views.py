from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from Register.models import Profile
from Register.serializers import ProfileSerializer

class ProfileAPIList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request):
        return render(request, "register.html")

class ProfileAPICreate(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self, request):
        return render(request, 'secondauthtorization.html')

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверка данных
        serializer.save()  # Метод create
        context = {
            "data": serializer.data,
        }
        return redirect("ProfileAPIList", foo="bar")
