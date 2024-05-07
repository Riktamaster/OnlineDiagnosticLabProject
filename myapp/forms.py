from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class TestForm(forms.ModelForm):
    class Meta:
        model=Test
        fields='__all__'

class TestBookingForm(forms.ModelForm):
    class Meta:
        model=TestBooking
        fields='__all__'

class TestResultForm(forms.ModelForm):
    class Meta:
        model=TestResult
        fields='__all__'