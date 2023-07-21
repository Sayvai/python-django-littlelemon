from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("booking/table", views.BookingView.as_view()),
    path("booking/table/<int:pk>", views.SingleBookingView.as_view()),
]
