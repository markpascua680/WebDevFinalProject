from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("restaurant/<str:restaurant_name>", views.restaurant, name="restaurant"),
    path("restaurant/create/", views.add_restaurant, name="create_restaurant"),
    path("menu_item/create/<str:restaurant_name>", views.add_menu_item, name="create_menu_item"),
    path("edit_menu_item/<int:menu_item_id>", views.edit_menu_item, name="edit_menu_item"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("change_password/", auth_views.PasswordChangeView.as_view(), name="change_password"),
    path("change_password/done", auth_views.PasswordChangeDoneView.as_view(), name="change_password_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=forms.MyPasswordResetForm), name='password_reset'),
]
