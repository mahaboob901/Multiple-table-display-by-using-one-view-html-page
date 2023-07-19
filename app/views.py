
from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def registration(request):
    d={'USFO':UserForm(),'PFO':profileForm}
    if request.method=='POST' and request.FILES:
        USFOD=UserForm(request.POST)
        PFOD=profileForm(request.POST,request.FILES)
        if USFOD.is_valid() and PFOD.is_valid():
            NUSFOD=USFOD.save(commit=False)
            submittedpw=USFOD.cleaned_data['password']
            NUSFOD.set_password(submittedpw)
            NUSFOD.save()
            NPFOD=PFOD.save(commit=False)
            NPFOD.username=NUSFOD
            NPFOD.save()
            return HttpResponse('successfully Registered')


    return render(request,'registration.html',d)        
