from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menuItemView.as_view(), name="menu-list"),
    path("menu/<int:pk>", views.singleItemView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
