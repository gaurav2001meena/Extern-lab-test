from notes.models import Userinfo
import json
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@csrf_exempt
def login(request):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    name = Userinfo.objects.get(email=email).name
    
    
    if not re.match(pattern, email):
        return Response({'Error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
    elif not Userinfo.objects.filter(email =email , password=password).exists():
        return Response({"Error" : "User does not exist" , })
    else:
        user_id = Userinfo.objects.get(email=email)
        token = RefreshToken.for_user(user_id)
        return Response({"Message" : "Login Successfull" ,"welcome" : name ,"email": email , "token" : str(token.access_token)})
   
    

        