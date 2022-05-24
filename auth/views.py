from .serializers import RegistrationDataSerializer,AuthorizationSerializer
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth.hashers import check_password

def registrationview(request):
    serializer = RegistrationDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

def authentication(request):
    serializer = AuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    filter_query = {}
    if serializer.data.get('email'):
        filter_query['email'] = serializer.data.get('email')
    if serializer.data.get('username'):
        filter_query['username'] = serializer.data.get('username')
    user = CustomUser.objects.filter(**filter_query)
    if not user.exists():
        return Response({"message":"Cant find with email or username"})
    user = user.first()
    if not check_password(serializer.data.get('password'),user.password):
        return Response({"message":"Password is not correct"})
    return Response({'access_token':token})
