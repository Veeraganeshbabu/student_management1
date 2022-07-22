from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.shortcuts import redirect ,render
from django.contrib.auth import login ,logout ,authenticate
from django.http import HttpResponse
from .forms import *
from .models import*
from django.views import View

def home(request):

    details = Details.objects.all()

    context = {

        'details':details,

    }
    return render(request ,'home.html',context)


def addDetails(request):
    if request.user.is_authenticated:
        form=addDetailsform()
        if (request.method=='POST'):
            form =addDetailsform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context ={'form':form}
        return render(request,'addDetails.html',context)
    else:
        return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form =createuserform()
        if request.method =='POST':
            form =createuserform(request.POST)
            if form.is_valid() :
                user =form.save()
                return redirect('login')
        context ={
            'form':form,
        }
        return render(request ,'register.html' ,context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username =request.POST.get('username')
            password =request.POST.get('password')
            user =authenticate(request ,username=username ,password=password)
            if user is not None:
                login(request ,user)
                return redirect('/')
        context ={}
        return render(request ,'login.html' ,context)

class DeleteInputView(View):
    def get(self,request):
        return render(request,"deleteinput.html")
class DeleteView(View):
    def get(self,request):
        Student_Id=int(request.GET["s1"])
        stud=Details.objects.filter(StudentId=Student_Id)
        stud.delete()
        resp = HttpResponse("Student deleted successfully")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdateView(View):
    def post(self,request):
        Student_Id=int(request.POST["s1"])
        Student_name = request.POST["s2"]
        Student_BatchName = request.POST["s3"]
        Student_Dateofbirth = request.POST["s4"]
        Student_Graduation = request.POST["s5"]
        Student_Yearofpass= request.POST["s6"]
        Student_Email = request.POST["s7"]
        stud=Details.objects.get(StudentId=Student_Id)
        stud.StudentName=Student_name
        stud.BatchName=Student_BatchName
        stud.Dateofbirth=Student_Dateofbirth
        Stud.Graduation=Student_Graduation
        stud.YearOfPass= Student_Yearofpass
        stud.EMail = Student_Email
        stud.save()
        resp = HttpResponse("Student updated successfully")
        return resp


def searchpage(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        Detail=Details.objects.filter(StudentId__contains='searched' )
        return render(request,'search.html',{'searched':searched,
                                             'Detail':Detail})
    else:
        return render(request, 'search.html', {})






def logoutPage(request):
    logout(request)
    return redirect('/')







