from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import booking, menu
from .serializers import bookingSerializer, menuSerializer, userSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class menuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = menuSerializer


class singleItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer


class bookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = bookingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [permissions.IsAuthenticated]
