from django.urls import path
from .views import CourseListView, CourseDetailView


app_name = "courses"
urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),
]

