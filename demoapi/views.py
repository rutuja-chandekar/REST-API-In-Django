from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Item
from .serialize import ItemSerializer
from rest_framework.response import Response

@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteItem(request):
    delItem = Item.objects.get(id)
    delItem.delete()
    return Response({'msg': 'item deleted !!'},)

    
