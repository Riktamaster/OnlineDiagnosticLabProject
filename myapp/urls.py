from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('userlogout/',views.userlogout,name='userlogout'),
   path('booking/',views.booking,name='booking'),
   path('confirmbooking/<int:booking_id>/',views.confirmbooking,name='confirmbooking'),
   path('payment/', views.payment),
   path('about/',views.about),
   path('contact/',views.contact),
   path('news/',views.news),
   path('event1/',views.event1),
   path('event2/',views.event2),
   path('event3/',views.event3),
   path('careers/',views.careers),
   path('location/',views.location),
   path('otpverify/',views.otpverify,name='otpverify'),
   path('testresult/', views.testresult, name='testresult'),
   path('view_result/', views.view_result, name='view_result'),
   path('userlogout/',views.userlogout,name='userlogout'),
   path('test_results/<str:filename>/', views.download_attachment, name='download_attachment'),
]