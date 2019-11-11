from django.db import models

class Category(models.Model):
    TYPES = (
        (1, 'Languages'),
        (2, 'Cooking'),
        (3, 'Writing'),
        (4, 'Singing'),
    )
    name = models.CharField(max_length=100, choices=TYPES)

class Course(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Contact(models.Model):
    TYPE = (
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email'),
    )
    type = models.CharField(max_length=90, choices=TYPE)
    value = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)




