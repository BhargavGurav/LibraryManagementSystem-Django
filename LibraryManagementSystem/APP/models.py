from django.db import models

# Create your models here.
class Student(models.Model):
    Fields = (
        ('Computer', 'Computer'),
        ('Electrical', 'Electrical'),
        ('Civil', 'Civil'),
        ('Mechanical', 'Mechanical'),
        ('Instrumentation', 'Instrumentation'),
        ('Electronics and Tele.', 'Electronics and Tele.')
    )
    Years = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th')
    )
    name = models.CharField(max_length=50)
    prn = models.CharField(max_length=10)
    branch = models.CharField(max_length=25, choices=Fields)
    year = models.CharField(max_length=3, choices=Years)

    def __str__(self):
        return self.prn
    

class Entry(models.Model):
    Student = models.OneToOneField("Student", on_delete=models.CASCADE)
    Book_issued = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Student.name
    
