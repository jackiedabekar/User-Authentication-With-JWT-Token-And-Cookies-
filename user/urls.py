from django.urls import path
from django.urls.resolvers import URLPattern
from .views import RegisterView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register')
]