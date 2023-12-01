from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username=None, email=None, phone_number=None, password=None, **extra_fields):
        if not username and not email and not phone_number:
            raise ValueError('At least either username or email or phone_number must be set')
        if username:
            extra_fields['username'] = username
        if email:
            extra_fields['email'] = email
        if phone_number:
            extra_fields['phone_number'] = phone_number
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, phone_number=None, password=None, **extra_fields):
        if not username and not email and not phone_number:
            raise ValueError('At least either username or email or phone_number must be set')
        if not password:
            raise ValueError('Password must be set')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_verified') is not True:
            raise ValueError('Superuser must have is_verified=True')

        return self.create_user(username, email, phone_number, password, **extra_fields)
