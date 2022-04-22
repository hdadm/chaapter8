from django.urls import path
from .views import SignUpView
# comment to urls.py
urlpatterns = [
path("signup/", SignUpView.as_view(), name="signup"),
]