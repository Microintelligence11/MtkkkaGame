from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import points
from .models import Jay_Bharat_Chart
from .models import Moon_night_Chart
from .models import Great_India_Chart
from .models import Kalyan_day_Chart
from .models import Jay_Bharat_panle
from .models import Moon_night_panle
from .models import Great_India_panle
from .models import Kalyan_day_panle




# Create your views here.


def index(request):
    all_objects = points.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'index.html',context)

def weeklyChart(request):
    all_objects = points.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'weeklyChart.html',context)   

def allMarket(request):
    all_objects = points.objects.all()
    context = {'all_objects': all_objects} 
    return render(request, 'allMarket.html',context)

def gussingFrom(request):
    all_objects = points.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'gussingFrom.html',context)    

def bharathjodi(request): 
    all_objects = points.objects.all()
    bharath_objects = Jay_Bharat_Chart.objects.all() 
    context = {'all_objects': all_objects,'bharath_objects':bharath_objects}
    return render(request, 'bharathjodi.html',context)    

def milanDay(request):
    all_objects = points.objects.all()
    milaDay_objects = Kalyan_day_Chart.objects.all()
    context = {'all_objects': all_objects,'milaDay_objects':milaDay_objects}
    return render(request, 'milanDay.html',context)    

def sriDevi(request):
    all_objects = points.objects.all()
    sriDevi_objects = Moon_night_Chart.objects.all()
    context = {'all_objects': all_objects,'sriDevi_objects':sriDevi_objects}
    return render(request, 'sriDevi.html',context)

def timeBazar(request):
    all_objects = points.objects.all()
    timebazar_objects = Great_India_Chart.objects.all()
    context = {'all_objects': all_objects,'timebazar_objects':timebazar_objects}
    return render(request, 'timeBazar.html',context)   

def paneltime(request):
    paneltime_objects = Great_India_panle.objects.all() 
    all_objects = points.objects.all()
    context = {'all_objects': all_objects,'paneltime_objects':paneltime_objects}
    return render(request, 'paneltime.html',context)

def panelBharath(request):
    bharathpanle = Jay_Bharat_panle.objects.all()
    all_objects = points.objects.all()
    context = {'all_objects': all_objects,'bharathpanle':bharathpanle}
    return render(request, 'panelBharath.html',context)

def panelmilan(request):
    panelmilan_objects = Kalyan_day_panle.objects.all()
    all_objects = points.objects.all()
    context = {'all_objects': all_objects, 'panelmilan_objects':panelmilan_objects}
    return render(request, 'panelmilan.html',context)


def panelseridevi(request):
    panlesridavi = Moon_night_panle.objects.all()
    all_objects = points.objects.all()
    context = {'all_objects': all_objects,'panlesridavi':panlesridavi}
    return render(request, 'panelseridevi.html',context)

def playGame(request):
    return render(request, 'playGame.html')  
 
def handleSignUp(request):
   
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if len(username)>10:
            messages.error(request,"User Name Not Valid Please try again again")  
            return redirect('playGame')  
                  

        if pass1 != pass2:
            messages.error(request,"Your Password not mach Please try again")
            return redirect('playGame') 
    
        if User.objects.filter(username=username).exists():
            messages.error(request,'This Username already taken please try to anouther name')
            return redirect('playGame')
       
        else:
            myuser = User.objects.create_user(username=username,password=pass1,email=email)
            myuser.save()  
            messages.success(request,"You are Succesfuly Signup please Login now!") 
            return redirect('playGame')     
        
    else:
        return HttpResponse("404-Not Found")        

    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(request, username=loginusername, password=loginpassword)

    if user is not None:
        login(request,user)    
        messages.success(request,"You are Sucessful Log In")
        return redirect('playGame')


    else:
        messages.error(request,'Your Username or Password not correct please try agin')    
        return redirect('playGame')

def handlelogout(request):
    logout(request)
    messages.success(request,'you are sucessful logout')
    return redirect('playGame')

    
   

    

     

        



    
    
    


