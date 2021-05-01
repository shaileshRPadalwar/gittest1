from django.shortcuts import render,redirect
from .models import Task
from .forms import FormTask
from django.http import HttpResponseRedirect
#Create your views here.

def todolist(request):
    task=Task.objects.all()
    form=FormTask()
    if request.method=="POST":
        form=FormTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    #print(form)
    context={'task':task,'form':form}
    return render(request,'tasks/list.html',context)


#update tasks
def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        form = FormTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'tasks/update.html',{'form':task})



#TO DELETE
def delete_task(request,pk):
    item = Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'tasks/delete.html',context)

