from rest_framework import serializers, status
from .models import Course, Category, Branch, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('TYPES', 'img_path', 'name')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', "url", 'name', 'logo')

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    branches = BranchSerializer()
    contacts = ContactSerializer()

    class Meta:
        model = Course
        fields = ('id', "url", 'name', 'logo', 'category', 'branches', 'contacts')

# class CombineSerializer(serializers.ModelSerializer):
#     course = CourseSerializer()
#     class Meta