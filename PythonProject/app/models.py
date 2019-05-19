from django.db import models
from django.urls import reverse

projectStatuses = (
    ('active','Active'),
    ('incomplete', 'Incomplete'),
    ('complete','Complete')
)

class Client(models.Model):
    clientName = models.CharField(max_length=100)
    contactPerson = models.CharField(max_length=100)
    contactNumber = models.IntegerField()

    def __str__(self):
        return self.clientName

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})


class Project(models.Model):
    projectName = models.CharField(max_length=100)
    projectStatus = models.CharField(max_length=15, choices=projectStatuses, default='active')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.projectName

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

