from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import FormForHub
from django.views import View, generic
from .models import HubModels  
from django.views.generic.edit import FormView
from django.views import View

class IndexHub(generic.ListView ):
    model = HubModels
    template_name = 'hub/hub.html'
    context_object_name = 'carry' # carry = all object from HubModels !
    

    def queryset(self):
        return HubModels.objects.all()

class IndexTask(generic.DeleteView):
    model = HubModels
    form = FormForHub
    template_name = 'hub/task.html'


def IndexAdd(request):
    if request.method == 'POST':
        form = FormForHub(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            model = HubModels.objects.create( title = title , description = description)
            model.save()
            return HttpResponseRedirect('/hub/')
    else:
        form = FormForHub()
        model = HubModels.objects.all()
    context = {'modelpost' : model , "form" : form }
    return render(request , 'hub/add.html' , context)


    
    





