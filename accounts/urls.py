from django.urls import path
from .views import SignUp

urlpatterns = [
    path('signin/', SignUp.as_view(), name='signin'),
]