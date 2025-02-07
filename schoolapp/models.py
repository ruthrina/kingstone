from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class ExecutiveLeader(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='executives/', blank=True, null=True)
    quote = models.TextField()

    def __str__(self):
        return self.name


class Prefect(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='prefects/')
    
    def __str__(self):
        return self.name    
    


class Staff(models.Model):
    STAFF_CHOICES = [
        ('staff', 'Staff'),
        ('non_staff', 'Non-Staff'),
    ]
    
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/')
    category = models.CharField(max_length=10, choices=STAFF_CHOICES, default='non_staff')

    def __str__(self):
        return self.name




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    


class SchoolGallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
    
from django.db import models

class Application(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    previous_school = models.CharField(max_length=255)
    intended_class = models.CharField(max_length=50)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.intended_class}"
    



class UNEBPerformance(models.Model):
    year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"UNEB Performance {self.year}"

class UCEPerformance(models.Model):
    uneb_performance = models.ForeignKey(UNEBPerformance, on_delete=models.CASCADE, related_name='uce_performance',  default=1 )
    number_of_students = models.PositiveIntegerField(default=0)
    first_grade = models.PositiveIntegerField(default=0)
    second_grade = models.PositiveIntegerField(default=0)
    third_grade = models.PositiveIntegerField(default=0)
    fourth_grade = models.PositiveIntegerField(default=0)
    failures = models.PositiveIntegerField(default=0)
   

    def __str__(self):
        return f"UCE {self.uneb_performance.year} - {self.number_of_students} students"

class UACEPerformance(models.Model):
    uneb_performance = models.ForeignKey(UNEBPerformance, on_delete=models.CASCADE, related_name='uace_performance', default=1 )
    number_of_students = models.PositiveIntegerField(default=0)
    three_principals = models.PositiveIntegerField(default=0)
    two_principals = models.PositiveIntegerField(default=0)
    one_principal = models.PositiveIntegerField(default=0)
    subsidiaries = models.PositiveIntegerField(default=0)
    failures = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"UACE {self.uneb_performance.year} - {self.number_of_students} students"







