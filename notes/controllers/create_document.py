from notes.models import Document, Userinfo
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@csrf_exempt
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_document(request):
    data = json.loads(request.body)
    email = data["email"]
    title = data['title'],
    content = data['content'],
    img = data['img']
    try:
     email_data = Userinfo.objects.filter(email=email).get()   
     Document.objects.create(email=email_data, title=title , content=content , img=img)
     return Response({"Message" : "Notes Created Successfully"})
    except Exception as e:
        return Response({"Error" : str(e)})
        
    
    
    
   
    

        