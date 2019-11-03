from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, default='')
    imgpath = models.CharField(max_length=255, default='')
#
# class Branch(models.Model):
#     latitude = models.CharField(max_length=100, default='')
#     longitude = models.CharField(max_length=100, default='')
#     address = models.CharField(max_length=255, default='')
#
# class Contact(models.Model):
#     value = models.CharField(max_length=255, default='')

class Course(models.Model):
    name = models.CharField(max_length=50, default='')
    #description = models.CharField()
    logo = models.CharField(max_length=255, default='')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, default=True)
    # contacts = models.ForeignKey('Contact', related_name='courses', on_delete=models.CASCADE)
    # branches = models.ForeignKey('Branch', related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

