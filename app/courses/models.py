from django.db import models

class Category(models.Model):
    TYPES = (
        (1, 'Languages'),
        (2, 'Cooking'),
        (3, 'Writing'),
        (4, 'Singing'),
    )
    name = models.CharField(max_length=255, choices=TYPES, default=True)
    img_path = models.CharField(max_length=255, default='')

class Contact(models.Model):
    TYPE = (
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email'),
    )
    type = models.CharField(max_length=90, default=True, choices=TYPE)
    value = models.CharField(max_length=255, default='')

class Branch(models.Model):
    latitude = models.CharField(max_length=100, default='')
    longitude = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=255, default='')


class Course(models.Model):
    name = models.CharField(max_length=50, default='')
    logo = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, default=True)
    contacts = models.ForeignKey(Contact, related_name='courses', on_delete=models.CASCADE)
    branches = models.ForeignKey(Branch, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
