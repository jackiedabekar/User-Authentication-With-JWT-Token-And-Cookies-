from jwt import algorithms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from django.conf import settings

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User Not Found')

        # We cant compare password received in request with password
        # of user save in DB which is in Hash format, so we are using inbuilt function
        # to compare password.
        if not user.check_password(password):
            raise AuthenticationFailed('Password is incorrect')

        payload = {
            'id': user.id,
            # Token Expire Time
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            # Token Created Time
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        respone = Response()

        respone.set_cookie(key='jwt', value=token, httponly=True)

        respone.data = {
            'jwt': token
        }
        return respone

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('User is aunauthenticated')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.get(id=payload['id'])

        serialiser = UserSerializer(user)

        return Response(serialiser.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Successfully Logout'
        }
        return response