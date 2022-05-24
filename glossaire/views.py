from urllib import response
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from yaml import serialize
from glossaire.models import Glossary
from glossaire.serializers import Glossaryserializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.

class WordViewSet(viewsets.ModelViewSet):
  queryset = Glossary.objects.all()
  serializer_class = Glossaryserializer

  @action(methods=['get','put','delete'],detail=True)
  def newest(self,request,*args,**kwargs):
    newest = Glossary.objects.filter(Q(French=kwargs['pk']) | Q(English=kwargs['pk']) | Q(Arabic=kwargs['pk']))
    if request.method=='GET':
      serializer=self.get_serializer_class()(newest,many=True)
      if newest.exists():
        return Response({ "success": True, "data": serializer.data[0] })
      return Response({ "success": False, "msg": 'word not found' })  
    elif request.method=='PUT':
      serializer=self.get_serializer_class()(newest,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({ "success": True, "msg": 'word updeted successfully' })
      return Response({ "success": False, "msg": 'failed to update the word' })
    elif request.method=='DELETE':
        try:
          if newest.exists():
            newest.delete()
            return Response({ "success": True, "msg": 'word deleted successfully' })
          return Response({ "success": False, "msg": 'failed to delete the word' }) 
        except newest.DoesNotExist:
          return JsonResponse('Failed to deleted .',safe=False)
    else:
      return HttpResponse("No File Found", status=400)

  # @action(methods=['put'],detail=False)
  # def newestPo(self,request):
  #   newest = Glossary.objects.get(French='hhhhh')
  #   serializer=self.get_serializer_class()(newest,data=request.data)
  #   if serializer.is_valid():
  #      serializer.save()
  #      return Response(serializer.data)
  #   return JsonResponse('Failed to Add .',safe=False)   
# @csrf_exempt

# def glossaryAPI(request,ID):
#   if request.method=='GET':
#     Mots= Glossary.objects.all(id=ID)
#     Mots_serializer = Glossaryserializer(Mots,many=True)
#     return JsonResponse(Mots_serializer.data,safe=False)
#   elif request.method=='POST':
#     Mots = JSONParser().parse(request)
#     Mots_serializer= Glossaryserializer(data=Mots)
#     if Mots_serializer.is_valid():
#       Mots_serializer.save()
#       return JsonResponse('Addes Successfully!!',safe=False)
#     return JsonResponse('Failed to Add .',safe=False)   
#   elif request.method=='PUT':
#     Indice=JSONParser().parse(request)
#     Mots=Glossary.objects.get(id=ID)
#     Mots_serializer=Glossaryserializer(Mots,data=Indice)
#     if Mots_serializer.is_valid():
#       Mots_serializer.save()
#       return JsonResponse('Updated Successfully!!',safe=False)
#     return JsonResponse('Failed to Updated .',safe=False) 
#   elif request.method=='DELETE' :
#     try:
#       Mots=Glossary.objects.get(id=ID)
#       Mots.delete()
#       return JsonResponse('Deleted Successfully!!',safe=False)
#     except Mots.DoesNotExist:
#           return JsonResponse('Failed to deleted .',safe=False)    
