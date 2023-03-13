from rest_framework.decorators import api_view 
from rest_framework.response import Response
from notes.models import Document
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["PATCH"])
@csrf_exempt
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])


def update_document(request):
    
    data = json.loads(request.body)
    title = data['title']
    content = data['content']
    img = data['img']
   
    

    if Document.objects.filter(title=title).exists(): 
      Document.objects.filter(title=title  , content=content , img=img).update()
      return Response({"Notes Updated Successfully"})
    else:
        return Response({"Enter Correct Title"})
        
     