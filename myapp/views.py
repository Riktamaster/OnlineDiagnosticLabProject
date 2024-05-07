from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.http import HttpResponse
from django.conf import settings
import os
from .forms import *
from .models import *
import random

# Create your views here.
def login(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        fnm=usersignup.objects.get(username=unm)
        uid=usersignup.objects.get(username=unm)
        print("Firstname:",fnm.firstname)
        print("UserID:",uid.id)
        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            request.session['user']=unm #session create
            request.session['user']=fnm.firstname
            request.session['uid']=uid.id
            #request.session.set_expiry(300)
            return redirect('dashboard')
        else:
            print("Error!Something went wrong...Try again")
    return render(request,'login.html')

otp = random.randint(1111, 9999)
def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            # Send Email for OTP
            sub="OTP Verification for New user!"
            msg=f"Dear User!\n\nThanks for registraion with us!\nYour one time password is {otp}\n\nThanks & Regards!\nNotesApp Team - Rajkot\n+91 97247 99469 | www.tops-int.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['username']]
            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            print("Your OTP:",otp)
            return redirect('otpverify')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def dashboard(request):
    user = request.session.get('user')
    return render(request, 'dashboard.html', {'user': user})

def userlogout(request):
    logout(request)
    return redirect('/')

def booking(request):
    user = request.session.get('user')
    tests = Test.objects.all()
    if request.method == 'POST':
        form = TestBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmbooking', booking_id=form.instance.id)
    else:
        form = TestBookingForm()
    return render(request, 'booking.html', {'form': form, 'tests': tests,'user':user})

def confirmbooking(request, booking_id):
    try:
        booking = TestBooking.objects.get(id=booking_id)
        total_cost = booking.test.cost  # Retrieve the cost of the booked test
        return render(request, 'confirmbooking.html', {'booking': booking, 'total_cost': total_cost})
    except TestBooking.DoesNotExist:
        return redirect('booking')

def payment(request):
        user = request.session.get('user')
        return render(request, 'payment.html',{'user':user})


def about(request):
    user = request.session.get('user')
    return render(request, 'about.html',{'user':user})

def contact(request):
    user = request.session.get('user')
    return render(request, 'contact.html',{'user':user})

def news(request):
    user = request.session.get('user')
    return render(request, 'news.html',{'user':user})

def careers(request):
    user = request.session.get('user')
    return render(request, 'careers.html',{'user':user})

def location(request):
    return render(request,'location.html')

def event1(request):
    return render(request,'event1.html')

def event2(request):
    return render(request,'event2.html')

def event3(request):
    return render(request,'event3.html')

def otpverify(request):
    global otp
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect('login')
        else:
            print("OTP Faild...")
            msg="OTP Faild...Plz enter valid OTP"
    return render(request,'otpverify.html',{'msg':msg})


def view_result(request):
    user = request.session.get('user')
    test_result = TestResult.objects.all()
    
    return render(request, 'view_result.html', {'user': user, 'test_result': test_result})

def download_attachment(request, filename):
    # Define the directory where the attachments are stored
    attachment_dir = os.path.join(settings.MEDIA_ROOT, 'test_results')

    # Define the full path to the requested file
    file_path = os.path.join(attachment_dir, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in binary mode for reading
        with open(file_path, 'rb') as f:
            # Create an HTTP response with the file content as the response content
            response = HttpResponse(f.read(), content_type='application/force-download')
            # Set the Content-Disposition header to force the browser to download the file
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            return response
    else:
        # Return a 404 response if the file does not exist
        return HttpResponse('File not found', status=404)

def testresult(request):
    user = request.session.get('user')
    result_form = TestResultForm()  # Define result_form outside of the if statement
    
    if request.method == 'POST':
        result_form = TestResultForm(request.POST, request.FILES)
        
        if result_form.is_valid():
            test_result = result_form.save()
            print("Your test result has been submitted!")
            return render(request, 'testresult_submitted.html', {'user': user})
        else:
            print(result_form.errors)
    
    return render(request, 'testresult.html', {'user': user, 'result_form': result_form})