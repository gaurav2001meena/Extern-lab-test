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
def show_all_doc(request):
    try:
     data = Document.objects.all().values()
     print (data)
     return Response({ "All Notes are" , data })
    except Exception as e:
        return Response({"Error" : str(e)})
        
    
    
    
   
    

        