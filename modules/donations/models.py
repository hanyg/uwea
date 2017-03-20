from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import (GenericRelation,
                                                GenericForeignKey)
from django.contrib.auth.models import User
import datetime


PAYMENT_OPTIONS = (
    (1, 'Monthly'),
    (2, 'Weekly'),
    (3, 'Annually'),
)

class BaseData(models.Model):
    created_by = models.ForeignKey(User, editable=False, null=True)
    created_on = models.DateField(auto_now_add=True, null=False)
    last_modified_on = models.DateField(auto_now_add=True, null=False)
    class Meta:
        abstract = True

class Campaign(BaseData):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    start_date = models.DateField(default=datetime.date.today,null=False)
    end_date = models.DateField(default=datetime.date.today,null=False)
    def __unicode__(self):
        return self.name

class Company(BaseData):
    """Company model."""
    name = models.CharField(max_length=200)
    contact = models.ForeignKey('Contact', null=True)
    phone_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    email_address = models.EmailField()
    def __unicode__(self):
        return self.name

class Contact(BaseData):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField()
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Pledge(BaseData):
    name = models.CharField(max_length=100)
    belongs_to = models.ForeignKey('Envelope', null=False)
    is_from_contact = models.ForeignKey('Contact', null=True)
    is_from_company = models.ForeignKey('Company', null=True)
    payments = models.IntegerField(default=1)
    payments_cycle = models.IntegerField(choices=PAYMENT_OPTIONS, default=1)
    amount = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    recurring = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.date.today,null=False)
    end_date = models.DateField(default=datetime.date.today,null=False)

    def __unicode__(self):
        return self.name

class Envelope(BaseData):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    belongs_to = models.ForeignKey('Campaign', null=False)
    def __unicode__(self):
        return self.name
