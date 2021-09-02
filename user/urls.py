from django.urls import path
from django.urls.resolvers import URLPattern
from .views import RegisterView, LoginView, UserView, LogoutView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('user/', UserView.as_view(), name='user-view'),
    path('logout/', LogoutView.as_view(), name='user-logout')
]