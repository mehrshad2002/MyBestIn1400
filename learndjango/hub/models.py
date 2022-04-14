from django.db import models
from django.contrib.auth.models import User 


class HubModels(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    image = models.ImageField(upload_to = '%Y/%m/%d' , null=True , blank=True)

    def __str__(self):
        return self.title
