from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r"table", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("api-token-auth/", obtain_auth_token),
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
]
