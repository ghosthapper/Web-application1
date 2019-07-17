from django.shortcuts import render,redirect
from forms.form import StudentForm
from forms.models import Student1
# Create your views here.

def new(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            
            Student = form.save()
            return redirect("/show")
    else:
        form = StudentForm()
    return render(request,"home.html",{'form':form})
def show(request):
    students = Student1.objects.all()
    return render(request,"dis.html",locals())