from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudForm,SForm,DForm
from .models import stud
# Create your views here.
def show(request):
    return render(request,"home.html")
def register(request):
    title="New Registration form"
    form=StudForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        addr=form.cleaned_data['s_addr']
        clas=form.cleaned_data['s_class']
        school=form.cleaned_data['s_school']
        email=form.cleaned_data['s_email']

        p=stud(s_name=name,s_class=clas,s_addr=addr,s_email=email,s_school=school)
        p.save()

        return render(request,'ack.html',{'msg':"success"})
        
    context={
        'title':title,
        'form':form
    }
    
    return render(request,'register.html',context)
def existing(request):
    title="Already Registered students"
    queryset=stud.objects.all()
    context={
        'title':title,
        'queryset':queryset

    }
    return render(request,'existing.html',context)
def search(request):
    title="searching"
    form=SForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name)
        context={
            'title':title,
            'queryset':queryset
        }
        return render(request,'existing.html',context)
    context={
        'title':title,
        'form':form
    }
    return render(request,'search.html',context)
def dropout(request):
    title="Student dropout"
    form=DForm(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['s_name']
        queryset=stud.objects.filter(s_name=name).delete()
        return render(request,'ack.html',{'msg':'Student Removed Successfully'})
    context={
        'title':title,
        'form':form
    }
    return render(request,'drop_out.html',context)
