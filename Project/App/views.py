from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_protect
from .models import *
from .serializers import *

# Create your views here.

    
class LoginView(APIView):
    
    def post(self, request):
        data= request.data
        serializer= Loginserializers(data= data)
        user= authenticate(username= data['username'], password= data['password'])
        token,_= Token.objects.get_or_create(user= user)
        print(user)
        if user is not None:
            login(request, user)
            return Response({'message': 'User Login Successfully!', 'token': str(token)})
        
        else:
            return Response({'message': "Unauthorized User!"})

@api_view(['GET']) 
def LogoutView(request):
    logout(request)
    return Response({'message': 'User Logout recently!'})
    
class RegisterView(APIView):
    def get(self, request):
        obj= User.objects.all()
        serializer = Registerserializers(obj, many= True)
        return Response(serializer.data)

    def post(self, request):
        data= request.data
        serializer= Registerserializers(data= data)

        if not serializer.is_valid():
            return Response({
                'message': serializer.errors
            })
        else:
            serializer.save()
            return Response({
                'message': 'User Created Successfully!'
            })


class BooksView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request):
        obj= Books.objects.all()
        serializer= Bookserializers(obj, many= True)

        return Response(serializer.data)
    
    @csrf_protect
    def post(self, request):
        data= request.data
        serializer= Bookserializers(data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data= request.data
        obj= Books.objects.get(id= data['id'])
        
        serializer= Bookserializers(obj, data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def patch(self, request):
        data= request.data
        obj= Books.objects.get(id= data['id'])
        
        serializer= Bookserializers(obj, data= data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)


    def delete(self, request):
        data= request.data
        obj= Books.objects.get(id= data['id'])
        obj.delete()
        return Response({'message':'Data Deleted!'})
    

@api_view(['GET', 'POST','PUT','PATCH','DELETE'])
def home(request):
    if request.method == 'GET':
        obj= Person.objects.all()
        serializer = PersonSerializers(obj, many= True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data= request.data
        serializer= PersonSerializers(data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method== 'PUT':
        data= request.data
        obj= Person.objects.get(id= data['id'])
        print(obj)
        serializer= PersonSerializers(obj, data= data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method== 'PATCH':
        data= request.data
        obj= Person.objects.get(id= data['id'])
        serializer= PersonSerializers(obj, data= data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data= request.data
        obj= Person.objects.get(id= data['id'])
        obj.delete()
        return Response({'message':'Data Deleted!'})