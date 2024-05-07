
from rest_framework.serializers import Serializer, ModelSerializer
from .models import Task, Person
from rest_framework import serializers
from datetime import date
from . import models


class TaskSerializer(Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    deadline = serializers.DateField()

    # def create(self, validated_data):
    #     title = validated_data.get('title')
    #     description = validated_data.get('description')
    #     deadline = validated_data.get('deadline')
    #     tasklar =Task.objects.create(
    #         title = title,
    #         description = description,
    #         deadline = deadline
    #     )
    #     return tasklar

    def validate(self, attrs):
        title = attrs.get('title')
        deadline  = attrs.get('deadline')
        if len(title) > 10:
            raise serializers.ValidationError(
                detail={'title': "title must not be more then 10 "}
            )
        
        if deadline < date.today():
            raise serializers.ValidationError(
                detail={'vaqt otib ketgan'})
        return super().validate(attrs)
    
    
    def update(self, instance, validated_data):
        instance.title =validated_data.get('title', instance.title)
        instance.description =validated_data.get('description', instance.description)
        instance.deadline =validated_data.get('deadline', instance.deadline)
        instance.save()
        return instance

    

    def create(self, validate_data):
        return Task.objects.create(**validate_data)
    








class PersonSerializer(Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    birth_data = serializers.DateField()
    


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Items
        fields = "__all__"


    def validate(self, attrs):
        name = attrs.get('name')
        if len(name)<10:
            raise serializers.ValidationError(
                detail={'name': "name must not be more then 10 "}
            )
            
# *************************************************


class SponsorSerializer(ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    
    university = serializers.StringRelatedField(source = "university.title")

    class Meta:
        model = models.Student
        exclude = ("created_at", "updataed_at")  

class StudentDetailSerializer(ModelSerializer):
    university = serializers.StringRelatedField(source = "university.title")
    
    class Meta:
        model = models.Student
        exclude = ("created_at", "update_at")   

class UniversitySerializer(ModelSerializer):
    class Meta:
        model = models.University
        fields = '__all__'


class StudentSponsorSerializer(ModelSerializer):
    class Meta:
        model = models.StudentSponser
        fields = '__all__'



