from django.shortcuts import render,redirect , get_object_or_404
from django.urls import reverse
from .models import Task

# Create your views here.
# to show the list
def task_list(request):
    task = Task.objects.all().order_by('-created_at')
    return render(request,'show_task.html',{'tasks':task})



#  to create a task
def task_edit(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description').strip()
        if title:
            Task.objects.create(title=title,description=description)
            return redirect(reverse('todo:task_list'))
        error = "Title cannot by empty."
        return render(request,'create.html',{'error':error})
    return render(request,'create.html')


def task_upadate(request, pk):
    task = get_object_or_404(Task ,pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description').strip()
        completed = request.POST.get('completed') == 'on'


        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect(reverse('todo:task_list'))
        return render(request,'task_form.html',{'task': task , 'error':"Title cannot be empty"})
    return render(request,'task_form.html',{'task': task })





def task_delete(request,pk):
    task = get_object_or_404(Task ,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request,'task_confirm_delete.html',{'task': task})





def task_toggle_complete(request,pk):
    task= get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('todo:task_list')

    