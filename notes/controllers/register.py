from notes.models import Userinfo
import json
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@api_view(['POST'])
@csrf_exempt
def register(request):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    data = json.loads(request.body)
    email = data['email']
    name = data['name']
    phone = data['phone']
    password = data['password']
    conf_password = data['conf_password']
    
    
    if Userinfo.objects.filter(email=email).exists():
        return Response({"Error" : "User already exist"})
    elif not re.match(pattern, email):
        return Response({'Error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
    elif not password == conf_password :
        return Response({"Error" : "Password and confirm password does not match"})
    else:
        Userinfo.objects.create(name=name , email=email , password=password , phone =phone)
        return Response({"Message" : "User created Successfully"})
    

        