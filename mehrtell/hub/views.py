from contextvars import Context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import HubModels
from .forms import FormForHub

def HubIndex(request):
    if request.method == 'POST':
        form = FormForHub(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            carry = HubModels.objects.create( title = title, content = content)
            carry.save()
            return HttpResponseRedirect('/hub/')
    else:
        form = FormForHub()
        carry = HubModels.objects.all()
    context = {
        "carry" : carry, "form" : form, 
    }
    return render(request, 'hub/homeindex.html' , context)

def ShowTaskIndex(request , postid):
    carry = HubModels.objects.get(id = postid)
    context =  {
        "carry" : carry 
    }
    return render(request, 'hub/showtaskindex.html' , context)
