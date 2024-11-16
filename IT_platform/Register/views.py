from django.shortcuts import render

# Create your views here.
def regitser(reqest):
    return render(reqest, 'register.html')
