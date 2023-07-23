from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html")


def menu_list(request):
    menu = Menu.objects.all()
    context = {"menu": menu}
    return render(request, "menu_list.html", context)


def menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    context = {"menu_item": menu_item}
    return render(request, "menu_item.html", context)


def booking(request):
    return render(request, "booking.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "register.html")


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
