from django.shortcuts import render,get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)
from rest_framework import serializers
from rest_framework import status
  
@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)
  
    # validating for already existing data
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def view_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_param.dict())
    else:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)

  
    # if there is something in items else raise error
    if items:
         return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
@api_view(['DELETE'])
def delete_null_values(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_param.dict())
    else:
        items = Item.objects.filter(name__isnull=True)
        items.delete()
        items = Item.objects.filter(username__isnull=True)
        items.delete()
        items = Item.objects.filter(age__isnull=True)
        items.delete()
        items = Item.objects.filter(dob__isnull=True)
        items.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        
        


    

  