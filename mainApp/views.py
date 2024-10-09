from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

from .models import Cars,Bikes,Mobiles,Applications




def home(request):
    
    
    cars = Cars.objects.all()  
    bikes = Bikes.objects.all()
    mobiles=Mobiles.objects.all()
    applications=Applications.objects.all()
    
    context = {
        'cars': cars,
        'bikes': bikes,
        'mobiles':mobiles,
        'applications':applications,

    }
    return render(request,'home.html',context)

def sell(request):
    return render(request,'sell.html')

def cars(request):
    

    if request.method == 'POST':
        car = Cars()
        car.seller = request.user
        car.fuel = request.POST.get('fuel')
        car.transmission = request.POST.get('transmission')
        car.km = request.POST.get('km')
        car.title = request.POST.get('title')
        car.description = request.POST.get('description')
        car.price = request.POST.get('price')
        car.brand = request.POST.get('brand')
        car.year = request.POST.get('year')
        car.noOfOwner = request.POST.get('noOfOwner')
        car.location = request.POST.get('location')
        car.address = request.POST.get('address')
        car.phno = request.POST.get('phno')
        
        
        if request.FILES.get('image'):
            car.image = request.FILES.get('image')
        if request.FILES.get('image1'):
            car.image1 = request.FILES.get('image1')
        if request.FILES.get('image2'):
            car.image2 = request.FILES.get('image2')
        if request.FILES.get('image3'):
            car.image3 = request.FILES.get('image3')
        
       
        car.save()
        print('success')
        messages.success(request, 'Car details updated successfully!')
        return redirect('home')
    else:
        return render(request,'cars.html')


def bikes(request):
    if request.method == 'POST':
        bike = Bikes()
        bike.seller = request.user
        
        bike.bikeKm = request.POST.get('bikeKm')
        bike.title = request.POST.get('title')
        bike.description = request.POST.get('description')
        bike.price = request.POST.get('price')
        bike.brand = request.POST.get('brand')
        bike.year = request.POST.get('year')
        bike.noOfOwner = request.POST.get('noOfOwner')
        bike.location = request.POST.get('location')
        bike.address = request.POST.get('address')
        bike.phno = request.POST.get('phno')
        
        
        if request.FILES.get('image'):
            bike.image = request.FILES.get('image')
        if request.FILES.get('image1'):
            bike.image1 = request.FILES.get('image1')
        if request.FILES.get('image2'):
            bike.image2 = request.FILES.get('image2')
        if request.FILES.get('image3'):
            bike.image3 = request.FILES.get('image3')
        
       
        bike.save()
        print('success')
        messages.success(request, 'bike details updated successfully!')
        return redirect('home')
    else:
        return render(request,'bikes.html')
def mobiles(request):
    return render(request,'mobiles.html')
def applications(request):
    return render(request,'applications.html')

def onlycars(request):
    cars = Cars.objects.all()
    context = {
        'cars': cars,
        
    }
    return render(request,'onlycars.html',context)

def onlybikes(request):
    bikes = Bikes.objects.all()
    context = {
        'bikes': bikes,
        
    }
    return render(request,'onlybikes.html',context)

def onlymobiles(request):
    mobiles = Mobiles.objects.all()
    context = {
        'mobiles': mobiles,
        
    }
    return render(request,'onlymobiles.html',context)


def details(request,type,p_id):

    if type == 'car':
        product = get_object_or_404(Cars, id=p_id)
        template = 'car_details.html'
    elif type == 'bike':
        product = get_object_or_404(Bikes, id=p_id)
        template = 'bike_details.html'
    else:
        
        return render(request, '404.html')  

    return render(request, template, {'product': product})
    



def message(request, p_id):
    try:
        
        product = get_object_or_404(Cars, id=p_id)
    except Cars.DoesNotExist:
        try:
            
            product = get_object_or_404(Bikes, id=p_id)
        except Bikes.DoesNotExist:
            
            return render(request, '404.html')

    return render(request, 'message.html', {'product': product})





def signup(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, 'signup.html')

            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use")
                return render(request, 'signup.html')
           
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            
            
            if user is not None:
               
                messages.success(request, f"Account created successfully for {username}")
                return redirect('home') 

    return render(request, 'signup.html')

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

            
        user = authenticate(request, username=username, password=password)

        if user is not None:
            
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            print('sucesss')
            return redirect('home')  
        else:
            print('unsuccesfull')
            messages.error(request, "Invalid username or password")
    return render(request,'login.html')  
            

        
    
    
        
def signout(request):
    logout(request)
    messages.success(request, 'logout successfull!')
    return redirect('home')

        

            

            