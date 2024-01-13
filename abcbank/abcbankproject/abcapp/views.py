from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Applicationdetails
# import pdb; pdb.set_trace()

def homepage(request):

    return render(request, 'homepage.html')

def register(request):
    try:
        if request.method == 'POST':
           username = request.POST['username']
           first_name = request.POST['first_name']
           last_name = request.POST['last_name']
           email = request.POST['email']
           password = request.POST['password']
           cpassword = request.POST['confirmpassword']

           if password == cpassword:
              if User.objects.filter(username=username).exists():
                 messages.info(request, 'Username is already taken.')
                 return redirect('abcapp:register')
              elif User.objects.filter(email=email).exists():
                 messages.info(request, 'Email is already taken.')
                 return redirect('abcapp:register')
              else:
                 user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                 user.save()
                 # print("User created")
                 messages.success(request, 'Registration successful. Please log in.')
                 return redirect('abcapp:login')
           else:
               messages.info(request, 'Passwords do not match.')
               return redirect('abcapp:register')
    except:
        pass

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'form.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('abcapp:login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request, 'form.html')

def applicationform(request):
     try:
        if request.method == 'POST':
           Name = request.POST.get('Name')
           DOB = request.POST.get('DOB')
           Age = request.POST.get('Age')
           Gender = request.POST.get('Gender')
           Phone = request.POST.get('Phone')
           Email = request.POST.get('Email')
           Address = request.POST.get('Address')
           District = request.POST.get('District',None)
           Branch = request.POST.get('Branch',None)
           Account_Type = request.POST.get('AccountType')  # Correct the field name
           Materials_provided = request.POST.get('MaterialsProvided')

           applicationform = Applicationdetails(Name=Name, DOB=DOB, Age=Age, Gender=Gender, Phone=Phone, Email=Email,
                                      Address=Address, district=District, branch=Branch, Account_Type=Account_Type, Materials_Provided=Materials_provided)
           applicationform.save()
           messages.info(request,"Application Submitted")
     except:
         messages.info(request,"field is required")
     return render(request, 'applicationform.html')
# def dependentfield(request):
#     districtid=request.POST.get('district',None)
#     district=None
#     branch=None
#     if districtid:
#         getdistrict= District.objects.get(id=districtid)
#         branch = Branch.objects.filter(district=getdistrict)
#
#     return render(request, 'dependentfield.html',locals())


# def applicationform(request):
#     form = Applicationform(request.POST or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'form': form}
#
#     return render(request, 'applicationform.html', context)

