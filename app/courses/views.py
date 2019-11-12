from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import CourseSerializer
from .models import Course

class CourseListView(ListCreateAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(RetrieveDestroyAPIView):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
