from django.urls import path 
from . import views
from .views import IndexHub , IndexTask , IndexAdd

urlpatterns = [ 
    path('' , IndexHub.as_view() , name = "indexhub"),
    path('task/<int:pk>' , IndexTask.as_view() , name = "indextask"),
    path('addtask/' , views.IndexAdd , name = "indexadd")
]  