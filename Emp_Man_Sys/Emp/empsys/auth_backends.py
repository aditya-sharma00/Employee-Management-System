from .models import Emp
from django.contrib.auth import get_user_model

User = get_user_model()

class EmpAuthenticationBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = Emp.objects.get(email=email)
            if user.password == password:
                return user
        except Emp.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Emp.objects.get(pk=user_id)
        except Emp.DoesNotExist:
            return None
