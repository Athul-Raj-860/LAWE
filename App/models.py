from django.db import models

class Register(models.Model):
    User_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Number = models.CharField(max_length=20)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=255)

    class Meta:
        db_table = "Register"

class User_Details(models.Model):
     Case_Id = models.AutoField(primary_key=True)
     User_Id =models.ForeignKey(Register,on_delete=models.CASCADE)
     Name = models.CharField(max_length=255)
     Number =  models.CharField(max_length=12)
     Email = models.EmailField()
     Address = models.TextField()
     City = models.CharField(max_length=100)
     State = models.CharField(max_length=100)

     class Meta:
         db_table = "User_Details"

class Case_Details(models.Model):
    Case_Id = models.ForeignKey(User_Details,on_delete=models.CASCADE)
    User_Id = models.ForeignKey(Register, on_delete=models.CASCADE)
    Complaint_Type = models.CharField(max_length=100)
    Complaint_Area = models.CharField(max_length=100)
    Complaint_Date = models.DateField()
    Complaint_Details = models.TextField()
    Complaint_Image =models.ImageField()

    class Meta:
        db_table="Case_Details"

class Lawyer_Register(models.Model):
    User_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Number = models.CharField(max_length=20)
    Experience = models.DecimalField(max_digits=2,decimal_places=1)
    Firm = models.CharField(max_length=255)
    Category = models.CharField(max_length=25)
    Image = models.ImageField()
    Price = models.IntegerField()

    class Meta:
        db_table = "Lawyer_Register"

class Book_Lawyer(models.Model):
    User_Id = models.ForeignKey(Register, on_delete=models.CASCADE)
    Name =  models.CharField(max_length=255)
    Number = models.CharField(max_length=255)
    Email = models.EmailField()
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)

    Lawyer_Name =  models.ForeignKey(Lawyer_Register,on_delete=models.CASCADE,related_name='book_Lawyer_Name')
    Category = models.ForeignKey(Lawyer_Register,on_delete=models.CASCADE,related_name='book_Lawyer_Categories')
    Appointment_Date = models.DateField()
    Appointment_Time = models.CharField(max_length=25)
    Contact_Time = models.CharField(max_length=25)
    Price = models.IntegerField()

    class Meta:
        db_table='Book Lawyer'

class Basic_Laws(models.Model):

    Law_Id = models.AutoField(primary_key=True)
    Law_Title = models.CharField(max_length=60)
    Law_Category = models.CharField(max_length=25)
    Law_Relevant = models.CharField(max_length=255)
    Law_Punishment = models.TextField()
    Law_Description = models.TextField()
    Law_link = models.URLField()

    class Meta:
        db_table='Basic Laws'
# Create your models here.
