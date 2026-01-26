from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class OfficialContactInformation(models.Model):
    name = models.CharField(max_length=500, default="Planway IT")
    Location = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class TeamMambarProfile(models.Model):
    name = models.CharField(max_length=500)
    profile_picture = models.ImageField()
    designation = models.CharField(max_length=500)


    def __str__(self):
        return self.name


class Clients(models.Model):
    profile_picture = models.ImageField()
    name = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    description = models.TextField()


    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    profile_picture = models.ImageField()
    name = models.CharField(max_length=500)


    def __str__(self):
        return self.name
