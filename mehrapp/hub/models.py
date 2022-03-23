from django.db import models

class HubModels(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title



