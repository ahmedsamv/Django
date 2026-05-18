from django.contrib.postgres import serializers

from rest_framework import serializers
from course.models import *
from traniee.models import *



class CourseSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields=['id','name']


class TranieeSerlizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    fees = serializers.DecimalField(decimal_places=2, max_digits=10)
    create_date = serializers.DateField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField( required=False,allow_null=True)
    Course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
       )
    is_active = serializers.BooleanField(default=True)


        #private logic to insert
    def create(self,validated_data):
        return Traniee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update the instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance