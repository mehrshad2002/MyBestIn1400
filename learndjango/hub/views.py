from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HubForms
from .models import HubModels


def HubIndex(request):
    carry = HubModels.objects.all()
    context = {
        "carry": carry
    }
    return render(request, 'hub/main.html' , context)  

def CreateIndex(request):
    if request.method == 'POST':
        form = HubForms(request.POST ,request.FILES)
        if form.is_valid():
            author = request.user 
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            carry = HubModels.objects.create( title = title, content = content , author = author , image = image  )
            carry.save()
            return HttpResponseRedirect('/hub/')
    else:
        form = HubForms()
        carry = HubModels.objects.all()
    context = {
        "carry" : carry , "form" : form,
    }

    return render(request, 'hub/create.html' , context)

def ShowIndex(request , pk ):
    carry = HubModels.objects.get( id = pk )
    context = {
        "carry" : carry
    }
    return render(request, 'hub/show.html' , context)   
 