from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404, render
from .serializers import EmpolyeeSerializer, StudentSerializer, StudentInfoSerializer, EmployeeInfoSerializer, UserSerializer,EmployeeUserSerializer
from .models import Empolyee, Student, User
from rest_framework import generics, status


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 교직원 회원가입
class EmpolyeeCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeUserSerializer

# 학생 회원가입
class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password, )
    if user:
        token, _  = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response(status=401)


class StudentInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer

    # def get_queryset(self):
    #     student_id = self.request.user.id
    #     queryset = get_object_or_404(Student, id=student_id)

    #     return queryset

class EmployeeInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmployeeInfoSerializer

    # def get_queryset(self):
    #     employee_id = self.request.user.id
    #     queryset = get_object_or_404(Empolyee, id=employee_id)

    #     return queryset

