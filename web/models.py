from django.db import models
from django.db.models.deletion import CASCADE 


# Create your models here.
class Gallery(models.Model):
    thumbnail = models.ImageField(upload_to="gallery/")
    category = models.ForeignKey("web.Category",on_delete=CASCADE)
    image = models.FileField(upload_to="gallery/",blank=True,null=True)

    def __str__(self):
        return str(self.thumbnail)


class Category(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Address(models.Model):
    details = models.TextField()

    def __str__(self):
        return self.details

class About(models.Model):
    image = models.FileField(upload_to="details/")
    title = models.CharField(max_length=56)
    description = models.TextField()

    def __str__(self):
        return self.title