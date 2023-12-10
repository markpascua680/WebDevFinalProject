from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("restaurant/<str:restaurant_name>", views.restaurant, name="restaurant"),
    path("restaurant/create/", views.add_restaurant, name="create_restaurant"),
    path("menu_item/create/<str:restaurant_name>", views.add_menu_item, name="create_menu_item"),
]
