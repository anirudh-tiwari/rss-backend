from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics, status
from .models import Link
from .serializers import LinkSerializer,CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        username=request.data['username']
        email=request.data['email']
        password=request.data['password']

        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return Response("success",status=200)

@api_view(['POST'])
def link(request):
    if request.method == "POST":
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def rss_list(request):
    # url = "https://codewithharry.com"
    case_list = [] 
    # url = "https://www.androidcentral.com/feed"
    url = Link.objects.all()[0].url #django-orm
    # url = Link.objects.all() #django-orm
    # print(url)
    # for ani in url:
    #     avi=ani

    r = requests.get(url)
    htmlContent = r.content
    # print(htmlContent)

    soup = BeautifulSoup(htmlContent,'xml')
    # print(soup.prettify)

    title=soup.title
    # print(title)

    paras = soup.find_all('item')
    # print(paras[1])

    # for ani in paras:
    #       yos = ani.find('description')
    #       print(yos)
        # yo = ani.find_all('title')
        # print(yo)                                                                                                                

    # def test(request):
    #     return HttpResponse(paras)


    for ani in paras:
        case = {'title': ani.find('title').text , 'description': ani.find('description').text , 'link': ani.find('link').text }
        case_list.append(case)
    return Response(case_list)


@api_view(['GET'])
def rss_title(request):
    title_list = [] 
    # url= " https://www.maketecheasier.com/feed/ "
    # url= " https://techwiser.com/feed/ "
    url = Link.objects.filter(user=request.user) #django-orm

    for x in url:
         ani= x.url
         r = requests.get(ani)
         htmlContent = r.content    
         soup = BeautifulSoup(htmlContent,'xml')          
         titles = {'title': soup.title.text }
         title_list.append(titles)
    return Response(title_list)

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer