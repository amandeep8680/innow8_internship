from django.shortcuts import render , redirect ,get_object_or_404
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

# Create your views here.
def uploads(request):
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile is Uploaded')
            return redirect('view_profiles')
        else:
            messages.error(request,'Form Invalid!!!')
    else:
        form = ProfileForm()
    return render(request, 'uploads.html',{'form':form})

def view_profiles(request):
    form = Profile.objects.all()
    return render(request,'view_profile.html',{'profiles':form})

def delete(request , pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('view_profiles')
    return render(request,'delete.html',{'profile':profile})





   

