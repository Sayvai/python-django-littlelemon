from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions, status
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


class IsManager(permissions.BasePermission):
    # override the has_permission method
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Manager").exists()


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated, IsManager]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAuthenticated, IsManager]

        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Booking.objects.filter(user=request.user)
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        booking = Booking(
            user=request.user,
            booking_date=request.data["booking_date"],
            no_of_guests=request.data["no_of_guests"],
        )
        booking.save()

        return Response(
            {"message": "Booking created successfully"},
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, *args, **kwargs):
        booking = Booking.objects.get(pk=kwargs["pk"])
        if (
            booking.user != request.user
            or not request.user.groups.filter(name="Manager").exists()
        ):
            booking.delete()
            return Response(
                {"message": "Booking deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"message": "You cannot delete this booking"},
            status=status.HTTP_403_FORBIDDEN,
        )
