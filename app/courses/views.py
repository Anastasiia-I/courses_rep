from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CourseView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=False)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class CourseCreateView(generics.CreateAPIView):
#     serializer_class = CourseSerializer

# class CourseListView(ListCreateAPIView):
#     model = Course
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
# class CourseDetailView(RetrieveDestroyAPIView):
#     model = Course
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
