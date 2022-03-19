from django.db import models

class HubModels(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=300)


    def __str__(self):
        return self.title