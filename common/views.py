from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Task
from django.urls import reverse

from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView 
from .models import Items

# Create your views here.


def home(request):

    tasks = Task.objects.order_by('-id')
    return render(request, "index4.html", {'tasks': tasks})


def create_task(request):

    if request.method == "POST":
        print(request.POST)
        title = request.POST.get('task')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        Task.objects.create(
            title = title,
            description = description,
            deadline =deadline
        )
        return HttpResponseRedirect('/')
    return render(request, 'create_task.html')


def edit_status(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        status = request.POST.get('status')
        task.status = status
        task.save()

        return HttpResponseRedirect('/')
    return render(request, 'edit_task.html', {'task': task})


def new_status(requset):
    pass

#         Task.TaskChoices.objects()


class TaskSerializier(ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description")
    


class TaskListAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializier
    
from rest_framework.generics import CreateAPIView,UpdateAPIView
from .serializers import TaskSerializer

class RegisterCreateAPIView(CreateAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class RegisterUpdate(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


from rest_framework.views import APIView, Response
from . import serializers


class ItemAPIView(APIView):

    def get(self, request, *args, **kwargs):
        items = Items.objects.all()
        serializer = serializers.ItemsSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        info = request.data
        name = info.get('name', "")
        if len(name)<10:
            raise serializers.serializers.ValidationError(detail={'name': "10 dan kop"})
        serializer = serializers.ItemsSerializer(data=info)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        

        return Response(data= serializer.is_valid(), status=201)


    #********************************************* 

from rest_framework.generics import  ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ItemListAPIView(ListAPIView):
    serializer_class=serializers.ItemsSerializer
    queryset = Items.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('is_done',)
    search_fields = ('name',)

# ***********************metsenat*********************



from . import models, serializers


class SponsorsListAPI(ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer


class StudentListAPI(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends =[DjangoFilterBackend,]
    filterset_fields = ('student_type', 'university')
    search_fields = ('full_name',)

class StudentDetailAPIView(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentDetailSerializer


class UniversityListAPI(ListAPIView):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class StudentSponsorListAPI(ListAPIView):
    queryset = models.StudentSponser.objects.all()
    serializer_class = serializers.StudentSponsorSerializer


from django.db.models import Sum
class StatisticAPIView(APIView):
   
    def get(self, request):
        total_paid_sum = models.StudentSponser.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        total_required_sum = models.Student.objects.aggregate(total_amount=Sum('contract'))['total_amount'] or 0
        total_unpaid_sum = 0
        
        return Response(
            data={
                "total_paid_sum": total_paid_sum,
                "total_required_sum": total_required_sum,
                "total_unpaid_sum": total_unpaid_sum
            }
        )
    
from datetime import datetime
class GraficAPIView(APIView):

    def get(self, request):
