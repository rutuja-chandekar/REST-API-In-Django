from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Item
from .serialize import ItemSerializer
from rest_framework.response import Response



def home(request):
    itemlist = Item.objects.all()
    print(itemlist)
    return render(request, 'demoapi/itemlist.html', context= {'itemlist': itemlist})

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
    print(request.data['id'])
    delItem = Item.objects.get(id=request.data['id'])
    delItem.delete()
    return Response({'msg': 'item deleted !!'})


@api_view(['PUT'])
def updateItem(request):
    print(request.data['id'])
    item = Item.objects.get(id=request.data['id'])
    serializer = ItemSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'data updated !!'}, status = 200)
    return Response({'msg': 'user not updated !!'}, status = 400)

    
