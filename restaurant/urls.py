from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r"table", views.BookingViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("menu-list", views.menu_list, name="menu-list"),
    path("menu-item/<int:pk>", views.menu_item, name="menu-item"),
    path("booking", views.booking, name="table-booking"),
    path("login", views.login, name="login"),
    path("register", views.signup, name="register"),
    path("api-token-auth", obtain_auth_token),
    path("menu", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
]
