import json
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from barter.models import User, Item
from barter.serializers import UserSerializer, ItemSerializer

@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            if User.objects.filter(username=data['username']).count() > 0:
                return JsonResponse(serializer.errors, status=400)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def user_signin(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body['username']
    password = body['password']
    try:
        user = User.objects.get(username=username)
    except:
        return JsonResponse({}, status=404)

    if password == user.password:
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status=400)

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_items(request, fk):
    items = Item.objects.filter(owner=fk)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
