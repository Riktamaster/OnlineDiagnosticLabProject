from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class usersignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField(max_length=20)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=200)

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.test_name

class TestBooking(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.EmailField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.fullname} - {self.test.test_name}"
    
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking = models.ForeignKey('TestBooking', on_delete=models.CASCADE)  # Replace 'YourBookingModel' with your actual booking model
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Payment for {self.booking} by {self.user.username}"

class TestResult(models.Model):
    booking = models.OneToOneField(TestBooking, on_delete=models.CASCADE)
    result_text = models.TextField()
    attachment = models.FileField(upload_to='test_results/')

    def __str__(self):
        return f"Test Result for {self.booking}"

