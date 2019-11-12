from rest_framework import serializers, status
from .models import Course, Branch, Category, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)
    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        branches = validated_data.pop('branches')
        contacts = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        for branch in branches:
            Branch.objects.create(course=course, **branch)
        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        return course





