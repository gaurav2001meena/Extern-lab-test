from notes.models import Document, Userinfo
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from notes.serializer import Documentserializer

@api_view(['POST'])
@csrf_exempt
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def doc_by_title(request):
    data = json.loads(request.body)
    title = data['title']
    try:
     if not Document.objects.filter(title=title).exists():
         return Response({"Error" : "Note does not exist"})   
     data = Document.objects.filter(title=title).values()
     
     return Response({ " Notes with title" : title , "are" : data })
    except Exception as e:
        return Response({"Error" : str(e)})
        
    
    
    
   
    

        