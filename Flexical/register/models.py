from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='freelancer')

    # Agregar related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Cambia el related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Cambia el related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

# Modelo de perfil de Cliente
class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='client_profile')
    company_nit = models.CharField(max_length=20, unique=True, verbose_name=_('Company NIT'))
    company_name = models.CharField(max_length=100, verbose_name=_('Company Name'))
    business_type = models.CharField(max_length=100, verbose_name=_('Business Type'))
    country = models.CharField(max_length=50, verbose_name=_('Country'))
    business_vertical = models.CharField(max_length=50, verbose_name=_('Business Vertical'))
    city = models.CharField(max_length=50, verbose_name=_('City'))
    address = models.CharField(max_length=100, verbose_name=_('Address'))
    phone_number = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message=_('Phone number must be entered in the format: +999999999.')
        )
    ], verbose_name=_('Phone Number'))
    legal_representative = models.CharField(max_length=100, verbose_name=_('Legal Representative'))

    def __str__(self):
        return f'{self.company_name} Client Profile'