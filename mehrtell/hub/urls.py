from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.HubIndex , name = 'hubindex'),
    path('task/<int:postid>' , views.ShowTaskIndex , name = 'showtaskindex'),
]