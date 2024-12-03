from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Farmer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(default="unknown@example.com")
    location = models.CharField(max_length=255)
    soil_type = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    password = models.CharField(max_length=128)  # Use hashed passwords in practice


    def __str__(self):
        return self.full_name

class GovernmentAgency(models.Model):
    agency_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, default="Unknown")
    email = models.EmailField(default="unknown@example.com")
    region = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # Use hashed passwords in practice


    def __str__(self):
        return self.agency_name


class NGO(models.Model):
    organization_name = models.CharField(max_length=255, default="Unknown Organization")
    email = models.EmailField(default="unknown@example.com")
    focus_area = models.CharField(max_length=255, blank=True, null=True)  # Optional field
    password = models.CharField(max_length=128)  # Use hashed passwords in practice


def __str__(self):
        return self.organization_name

