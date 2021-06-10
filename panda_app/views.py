from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def index(request):
    context={
        'all_pandas': Panda.objects.all()
    }
    return render(request, 'index.html', context)

def new_panda_page(request):
    return render(request, 'new.html') #get

def create_panda(request): #Post
    print('We are in the post request')

    new_panda=Panda.objects.create(name=request.POST['panda_name'], age=request.POST['age'], sex=request.POST['sex'])
    print(new_panda)

    return redirect('/')

def panda_profile(request, panda_id): #get
    panda=Panda.objects.get(id=panda_id)
    context={
        'this_panda':panda
    }
    return render(request,'profile.html', context)

def edit_page(request, panda_id): #get
    panda=Panda.objects.get(id=panda_id)
    context={
        'this_panda':panda
    }
    return render(request,'edit.html', context)

def update(request, panda_id):
    panda=Panda.objects.get(id=panda_id)
    panda.name=request.POST['panda_name']
    panda.age=request.POST['age']
    panda.sex=request.POST['sex']
    panda.save()

    return redirect(f'/pandas/{panda_id}')
    


