from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Voluteer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name