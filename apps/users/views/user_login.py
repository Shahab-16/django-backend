from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet



class UserLoginViewSet(ModelViewSet):

    @action(methods=["POST"],detail=False,url_path='otp')
    def otp_login(self,request):
        print("Hello Here it is otp login")
        return Response(status=status.HTTP_200_OK)