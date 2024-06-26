"""
urls for user API.
"""

from user import views
from django.urls import path

app_name = "user"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
    path("me/", views.ManagerUserView.as_view(), name="me"),
]
one = 1
