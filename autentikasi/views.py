from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .serializers import *
from .models import CustomUser

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        custom_user = CustomUser.objects.get(user=user)
        return Response(LoginResponseSerializer({
            "token": token.key,
            "user_id": user.id, 
            "role": custom_user.role,
            }).data)
    
class LogoutView(views.APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CustomUserView(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
# class ProfileView(viewsets.GenericViewSet):
#     serializer_class = UserSerializer
#     authentication_classes=[TokenAuthentication]
#     permission_classes=[IsAuthenticated]

#     def get_object(self):
#         # try:
#         #     custom_user = CustomUser.objects.get(user=self.request.user)
#         #     print(custom_user)
#         # except CustomUser.DoesNotExist:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         return self.request.user
    
#     def perform_update(self, serializer):
#         instance = serializer.save()
#         send_email_confirmation(user=self.request.user, modified=instance)

#     # def get(self):
#     #     print(self)
#     #     print(self.request)
#     #     print(self.request.user)
#     #     # try:
#     #     #     custom_user = CustomUser.objects.get(user=self.request.user)
#     #     #     print(custom_user)
#     #     # except CustomUser.DoesNotExist:
#     #     #     return Response(status=status.HTTP_404_NOT_FOUND)
#     #     return self.request.user
    