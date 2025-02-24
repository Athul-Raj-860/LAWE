
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password


from App.models import Register, User_Details, Case_Details, Lawyer_Register, Basic_Laws, Book_Lawyer, Payment_Details, \
    Emergency_Numbers


def Signup(request):

    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Number = request.POST.get('Number')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('Password1')
        if Password != Confirm_Password:
            return render(request,"Signup.html",{'Error':'Passwords Doesnot Match'})
        else:
          hashed_password = make_password(Password)
          Register.objects.create(Name=Name,Email=Email,Number=Number,Username=Username,Password=hashed_password)
          return render(request, "Login.html")
    return render(request,"Signup.html")

def Login(request):

    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        try:
            user = Register.objects.get(Username=Username)
            print(f"{Password}")
            print(f"{user.Password}")
            if check_password(Password, user.Password):
                request.session['User_Id'] = user.User_Id
                return redirect('Home')
            else:
                return render(request, "Login.html", {'Error': ' Password is Invalid'})
        except Register.DoesNotExist:
            return render(request, "Login.html", {'Error': 'Username or Password is Invalid'})

    return render(request, "Login.html")


def Forgot_Password(request):

    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('Password1')
        try:
            user = Register.objects.get(Email=Email)
            if Password == ConfirmPassword:
                hashed_password = make_password(Password)
                user.Password = hashed_password
                user.save()
                return redirect("Login")
            else:
                return render(request,"ForgotPassword.html",{"Error":"Password Doesnot Match"})

        except Register.DoesNotExist:
            return render(request,"ForgotPassword.html",{"Error":"Email Doesnot Exist"})
    return render(request,"ForgotPassword.html")

def Home(request):
    if "User_Id" in request.session:
        User_Id = request.session["User_Id"]
        r = Register.objects.get(User_Id=User_Id)
        return render(request,"Home.html",{'r':r})

def Register_Case(request):
    if "User_Id" in request.session:
        if request.method =="POST" :
                Name = request.POST.get('Name')
                Number = request.POST.get('Number')
                Email = request.POST.get('Email')
                Address = request.POST.get('Address')
                City = request.POST.get('City')
                State = request.POST.get('State')

                Complaint_Type = request.POST.get('Complaint_Type')
                Complaint_Subject = request.POST.get('Complaint_Subject')
                Complaint_Area = request.POST.get('Complaint_Area')
                Complaint_Date = request.POST.get('Complaint_Date')
                Complaint_Description = request.POST.get('Complaint_Description')
                Complaint_Image = request.FILES.get('Image')

                User_Details.objects.create(Name=Name,Number=Number,Email=Email,Address=Address,City=City,
                                            State=State)
                Case_Details.objects.create(Complaint_Type=Complaint_Type,Complaint_Subject=Complaint_Subject,Complaint_Area=Complaint_Area,Complaint_Date=Complaint_Date,
                                            Complaint_Details=Complaint_Description,Complaint_Image=Complaint_Image)
                return redirect("Home")
        return render(request,"RegisterCase.html")

def Lawyer_List(request):
    if "User_Id" in request.session:
        lawyer = Lawyer_Register.objects.all()
        User_Id = request.session["User_Id"]
        r = Register.objects.get(User_Id=User_Id)
        Sort = request.POST.get('Sort')
        Filter = request.POST.get('Filter')
        # Sort
        if Sort == "Name_asc":
            lawyer = lawyer.order_by('Name')
        elif Sort == "Name_desc":
            lawyer = lawyer.order_by('-Name')
        else:
            lawyer = lawyer

        # filter
        if Filter == 'Criminal':
            lawyer = lawyer.filter(Category="Criminal")
        elif Filter == 'Cyber':
            lawyer = lawyer.filter(Category="Cyber")
        elif Filter == 'Environment':
            lawyer = lawyer.filter(Category="Environment")
        elif Filter == 'Family':
            lawyer = lawyer.filter(Category='Family')
        elif Filter == 'Civil':
            lawyer = lawyer.filter(Category="Civil")
        else:
            lawyer = lawyer

        # Search
        search = request.POST.get('Search')
        if search:
            lawyer = lawyer.filter(Name__icontains=search)
            if not lawyer.exists():
                return render(request, "Lawyers`.html", {'Error': 'Item not in list', 'lawyer': lawyer,
                                                          'search': search})
        else:
            lawyer = lawyer

        # Pagination
        paginator = Paginator(lawyer, 6)
        page_number = request.GET.get('page')
        try:

            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return render(request, "Lawyers.html", {'page_obj': page_obj,'Sort':Sort,'Filter':Filter ,'r':r})

def Update_User(request,id):
    user = Register.objects.get(User_Id=id)

    if request.method == "POST":
        user.Name = request.POST.get('Name')
        user.Email = request.POST.get('Email')
        user.Number = request.POST.get('Number')
        try:

            New_Password = request.POST.get('NewPassword')
            ConfirmPassword = request.POST.get('Password1')
            if New_Password == ConfirmPassword:
                    hashed_password = make_password(New_Password)
                    user.Password = hashed_password
                    user.save()
                    return redirect("Home")
            else:
                    return render(request, "Update_User.html.html", {"Error": "Password Doesnot Match"})
        except:
          user.save()
          return redirect("Home")


    return render(request,"Update_User.html",{'user':user})



def Logout(request):
    if "User_Id" in request.session:
        del request.session["User_Id"]
    return render(request, "Login.html")

def EmergencyNumbers(request):
    if "User_Id" in request.session:
      Num = Emergency_Numbers.objects.all()
      return render(request,"EmergencyNumbers.html",{'Num':Num })

def Book_Lawyer1(request):
    LawyersNames = Lawyer_Register.objects.values('Name','Category')
    if "User_Id" in request.session and request.method == "POST":
        Name = request.POST.get('Name')
        Number = request.POST.get('Number')
        Email = request.POST.get('Email')
        City = request.POST.get('City')
        State = request.POST.get('State')

        Lawyer_Name = request.POST.get('LawyerName')
        Category = request.POST.get('Category')
        Appointment_Date = request.POST.get('Appointment_Date')
        Appointment_Time = request.POST.get('Appointment_Time')
        Contact_Time = request.POST.get('Contact_Time')


        booking = Book_Lawyer.objects.create(
            Name=Name,
            Number=Number,
            Email=Email,
            City=City,
            State=State,
            Lawyer_Name=Lawyer_Name,
            Category=Category,
            Appointment_Date=Appointment_Date,
            Appointment_Time=Appointment_Time,
            Contact_Time=Contact_Time
        )
        return redirect("Payment",Book_Id=booking.Book_Id)

    return render(request, 'BookLawyer1.html', {'LawyersNames': LawyersNames})

def Book_Lawyer2(request,id):
    Lawyer = Lawyer_Register.objects.get(User_Id=id)
    if "User_Id" in request.session and request.method == "POST":

        Name = request.POST.get('Name')
        Number = request.POST.get('Number')
        Email = request.POST.get('Email')
        City = request.POST.get('City')
        State = request.POST.get('State')

        Lawyer.Lawyer_Name = request.POST.get('Lawyer_Name')
        Lawyer.Category = request.POST.get('Category')
        Appointment_Date = request.POST.get('Appointment_Date')
        Appointment_Time = request.POST.get('Appointment_Time')
        Contact_Time = request.POST.get('Contact_Time')

        Book_Lawyer.objects.create(Name=Name, Number=Number, Email=Email, City=City, State=State,
                                   Appointment_Date=Appointment_Date,Appointment_Time=Appointment_Time,
                                   Contact_Time=Contact_Time)
        return redirect("Payment")

    return render(request, 'BookLawyer2.html',{'Lawyer':Lawyer})

def BasicLaws(request):
    if "User_Id" in request.session:
        Sort = request.POST.get('Sort','All')
        Filter = request.POST.get('Filter','All')
        search = request.POST.get('Search')
        Law = Basic_Laws.objects.all()

        page_number = request.GET.get('page', 1)
        if Sort!='All'  or Filter!='All'  or search:
            page_number = 1
        #Sort
        if Sort == "Title_asc":
            Law = Law.order_by('Law_Title')
        elif Sort == "Title_desc":
            Law = Law.order_by('-Law_Title')
        else:
            Law = Law

        #filter
        if Filter != 'All':
            Law = Law.filter(Law_Category = Filter)
        else:
            Law = Law

        # Search
        if search:
            Law = Law.filter(Law_Title__icontains=search)
            if not Law.exists():
                return render(request, "BasicLaws.html", {'Error': 'Item not in list', 'Law': Law,
                                                     'search': search})
        else:
            Law = Law

        #Pagination
        paginator = Paginator(Law, 6)  # 6 items per page

        try:
            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)

        return render(request, "BasicLaws.html", {'page_obj': page_obj,'Sort': Sort,
                      'Filter': Filter,'search': search})


def Payment(request,book_id):

        Lawyer = Book_Lawyer.objects.get(Book_Id=book_id)
        Lawyer_details = Lawyer_Register.objects.get(Name=Lawyer.Lawyer_Name)
        if "User_Id" in request.session and request.method == "POST":

            CardName = request.POST.get('CardName')
            CardNumber = request.POST.get('CardNumber')
            CardExpiryMonth = request.POST.get('CardExpiryMonth')
            CardExpiryYear = request.POST.get('CardExpiryYear')
            Cvv = request.POST.get('CVV')
            Lawyer_details.Price = request.POST.get('Price')

            Payment_Details.objects.create(CardName=CardName,CardNumber=CardNumber,CardExpiryMonth=CardExpiryMonth,
                                           CardExpiryYear=CardExpiryYear,Cvv=Cvv,Price=Lawyer_details.Price)
            return redirect("Home")
        return render(request,"AppointmentPayment.html",{'Lawyer':Lawyer,'Lawyer_details':Lawyer_details})
# Create your views here.
