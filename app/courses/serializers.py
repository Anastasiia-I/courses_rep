from rest_framework import serializers, status
from .models import Course, Branch, Category, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Branch
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Contact
        fields = '__all__'


    # def create(self, validated_data):
    #     branches_data = validated_data.pop('branches')
    #     course = Course.objects.create(**validated_data)
    #
    #     for branch in branches_data:
    #         branch, created = Branch.objects.get_or_create(address=branch['address'])
    #         course.branches.add(branch)
    #     return course
    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     branches_data = validated_data.pop('branches')
    #     contacts_data = validated_data.pop('contacts')
    #     course = Course.objects.create(**validated_data)
    #     Course.objects.create(course=course, **category_data, **branches_data, **contacts_data)
    #     return course

