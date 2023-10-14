from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp
from django.contrib import messages                    
from django.contrib.auth import authenticate,logout,login as auth_login          
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Emp,EmpAdmin,AssignTask # Import your custom user model (Emp)

from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request,'home.html',{})
@login_required
def emphome(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
       # User is not authenticated, redirect them to the login page
       messages.error(request, 'You must be logged in to access this page.')
       print("DONOT")
       print(request.user.is_authenticated)

       return redirect('/login/')  # Adjust the URL to your login page
    # if request.user.is_staff == False:

    #     print("Account is not verified yet")
    #     messages.error(request, 'Account is not verified yet.')
    #     return redirect('/login/')
    assigned_tasks = AssignTask.objects.filter(employee_email=request.user.email)
    print("HEllo bro",assigned_tasks)
    for task in assigned_tasks:
        print("Task Name:", task.task_name)
        print("Task Description:", task.task_description)
    user = request.user
    name = user.name
    phone = user.phone 
    email = user.email
    staff = user.is_staff
    context = {
        'name': name,
        'phone': phone,
        'email': email,
        'staff': staff,
        'assigned_tasks':assigned_tasks
    }
    print("My name is",user,name)
    if staff == False:
        print(staff)
        logout(request)
        messages.error(request, 'Account not activated yet')
        return redirect('/login/')
    return render(request,'emphome.html',context)
def sign(request):
    if request.method == "POST":
        name = request.POST.get("username") 
        email = request.POST.get("useremail") 
        phone = request.POST.get("phone") 
        password = request.POST.get("password") 
        cpassword = request.POST.get("cpassword") 
        print(name,email,password,cpassword)
        print("data comming")
        if Emp.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            print("Already Exists")
        elif Emp.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone already exists.')
            print("Already Exists")
        else:
            e = Emp()
            e.name =  name
            e.email =  email
            e.phone =  phone
            e.password =  password
            e.cpassword =  cpassword
            e.save()
            return redirect("/login/")
    return render(request,'sign.html',{})

def login(request):
    if request.method == "POST":
        email = request.POST.get("useremail")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect("/emp/home/")  # Redirect to 'emphome' upon successful login
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'login.html', {})
def services(request):
    
    return render(request,'services.html',{})



def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))  # Adjust 'home' to your home page URL name
from django.contrib.auth import login as auth_login, logout as auth_logout

@login_required
def update_profile(request):
    user = request.user  # Get the current user
    old_email = request.user.email
    print(old_email)
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']

        # Get the uploaded image from the request
        uploaded_image = request.FILES.get('image_upload')
        print("File hu",request.FILES)
        print("Image hu",uploaded_image)
        try:
            # Update user data
            user.name = name
            user.phone = phone
            user.email = email
            user.password = password  # Use set_password to hash the password
            user.address = address
            user.state = state
            user.country = country

            # Update the image if a new image is uploaded
            if uploaded_image:
                user.image = uploaded_image

            # Save the updated user
            user.save()

            print(f"User's new email: {request.user.email}"," ",old_email )

            assigned_tasks = AssignTask.objects.filter(employee_email=old_email)
            print("HEre me", assigned_tasks)
            
            for task in assigned_tasks:
                task.employee_email = email
                task.save()
                print(f"Task ID: {task.id}, Task New Email: {task.employee_email}")

            # Reauthenticate the user
            auth_logout(request)  # Log the user out
            auth_login(request, user)  # Log the user back in with the updated user object

            # Redirect to the same page with updated data
            return redirect('update_profile')  # You should set your URL name accordingly

        except IntegrityError as e:
            # Handle IntegrityError exceptions (e.g., duplicate email or phone)
            error_message = "A user with the same email or phone already exists."
            return render(request, 'update_profile.html', {'user': user, 'error_message': error_message})

    else:
        # Render the profile update form with the current user data
        return render(request, 'update_profile.html', {'user': user})



def admin_emp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # Check if the provided username and password match
        try:
            empAdmin = EmpAdmin.objects.get(username=username, password=password)
            print(empAdmin)
            # If a matching EmpAdmin is found, you can consider them logged in
            # Perform any additional logic you need here.
            return redirect('admin_dashboard')  # Redirect to a success page
        except EmpAdmin.DoesNotExist:
            error_message = "Invalid username or password."
    else:
        error_message = None
    
    
    
    return render(request, 'admin_login.html', {'error_message': error_message})




def admin_dashboard(request):
    # Fetch all Emp objects
    employees = Emp.objects.all()

    if request.method == 'POST':
        # Handle form submissions for editing and deleting employees
        action = request.POST.get('action')
        if action == 'edit':
            # Get the employee ID from the form
            employee_id = request.POST.get('employee_id')
            try:
                employee = Emp.objects.get(email=employee_id)
                # Update employee fields based on form data
                employee.name = request.POST.get('name', employee.name)
                employee.phone = request.POST.get('phone', employee.phone)
                employee.is_staff = request.POST.get('is_staff', employee.is_staff)
                employee.address = request.POST.get('address', employee.address)
                employee.state = request.POST.get('state', employee.state)
                employee.country = request.POST.get('country', employee.country)
                employee.image = request.FILES.get('image', employee.image)
                employee.role = request.POST.get('role', employee.role)
                # Add code to update other fields as needed
                employee.save()
            except Emp.DoesNotExist:
                pass  # Handle the case where the employee does not exist

        elif action == 'delete':
            # Get the employee ID from the form
            employee_id = request.POST.get('employee_id')
            try:
                employee = Emp.objects.get(email=employee_id)
                employee.delete()
            except Emp.DoesNotExist:
                pass  # Handle the case where the employee does not exist
        if action == 'add_task':
            try:
                emp_id = request.POST.get('employee_id')
            
                employee_name = request.POST.get('employee_name')
            
                employee_email = request.POST.get('employee_email')
            
                employee_phone = request.POST.get('employee_phone')
            
                employee_role = request.POST.get('employee_role')
            
                submission_date = request.POST.get('task_submission_date')
            
                task_name = request.POST.get('task_name')
            
                task_desc = request.POST.get('task_desc')
            
                task_file = request.FILES.get('task_file')
            
                task = AssignTask()
            
                task.employee_email = employee_email
            
                task.employee_name = employee_name
            
                task.task_submission_date = submission_date
            
                task.employee_phone = employee_phone
            
                task.employee_role = employee_role
            
                task.task_name =task_name
            
                task.task_description =task_desc
            
                task.file_submission =task_file
            
                print(task_file)

                task.save()
            
                
                print("HEllo bro",employee_name)

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                messages.error(request,"Please fill all the field")
    # Pass the employees to the template for rendering
    context = {
        'employees': employees
    }

    return render(request, 'admin_dashboard.html', context)