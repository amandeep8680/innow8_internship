from django.shortcuts import render,  get_object_or_404 , redirect
from .form import StudentForm
from .models import Student

# Create your views here.
def create_student(request):
    form = StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
        # else:
        #     print(form.errors)

    return render(request,'student_form.html' ,{'forms':form})


def show_list(request):
    lst = Student.objects.all()
    return render(request , 'show_list.html',{'lsst':lst})
 

def student_detail(request, pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,'student_detail.html',{'lst':student})


def update(request , pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method=='POST': 
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
            form = StudentForm(instance=student)   
    return render(request,'student_form.html' ,{'form':form})


def delete(request , pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method=='POST': 
        student.delete()
        return redirect('show_list')
    return render(request,'delete.html',{'forms':student})
