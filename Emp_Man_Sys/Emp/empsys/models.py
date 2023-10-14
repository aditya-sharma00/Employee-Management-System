from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EmpManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Emp(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=200)
    cpassword = models.CharField(max_length=200)
    
    # Add last_login field
    last_login = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # New fields for address, state, and country
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    # Image field with a default image
    image = models.ImageField(upload_to='profile_images', default='profile_images/default.png')

    objects = EmpManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email

    # Define related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='emp_set',  # Change 'emp_set' to a name that makes sense for your project
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='emp_set_permissions',  # Change 'emp_set_permissions' to a name that makes sense for your project
    )




class AssignTask(models.Model):
    
    # Employee Name
    employee_name = models.CharField(max_length=255)

    # Employee Email
    employee_email = models.EmailField()

    # Employee Phone
    employee_phone = models.CharField(max_length=15)

    # Employee Role
    employee_role = models.CharField(max_length=100)

    # Task Name
    task_name = models.CharField(max_length=255)

    # Task Description
    task_description = models.TextField()

    # Task Submission Date
    task_submission_date = models.DateField()

    # File Submission (you can use FileField or ImageField based on your requirements)
    file_submission = models.FileField(upload_to='task_files')

    def __str__(self):
        return f"{self.employee_email} - {self.task_name}"






class EmpAdmin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)  # You should hash and salt passwords in a real application

    def __str__(self):
        return self.username