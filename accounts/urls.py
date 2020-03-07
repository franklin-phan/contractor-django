from django.urls import path
from accounts.views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="accounts-signup")
]