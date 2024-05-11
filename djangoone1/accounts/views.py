from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

#function for login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        #let check if the user is present in the database
        if user is not None:
            auth.login(request, user) # this user means a current user
            return redirect('/')
        else:
            messages.info(request,'Wrong username or password')
            return redirect('login')

    else:
        return render(request,"login.html")
    
    
#function for register page
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username is already taken')
                return redirect('register')
                # print('username is already taken')  # this line print in the terminal
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email is already taken')
                return redirect('register')
                #print('email is already taken')
            else:
                user = User.objects.create_user(username = username, password=password1,email=email,first_name =first_name,last_name = last_name)
                user.save();
                print('user created')
                return redirect('login') # automatic go to login page

        else:
            messages.info(request,'password not matching...')
            return redirect('register') #this means go to the register page
            # print('password not matching...')
            
        return redirect('/') # this means go to the main page
    
    else:
        return render(request, "register.html")

#function for logout 
def logout(request):
    auth.logout(request)
    return redirect("/")

