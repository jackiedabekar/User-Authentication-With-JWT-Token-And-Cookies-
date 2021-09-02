from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User

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

        return Response({
            'message': 'success'
        })
