from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import (GenericRelation,
                                                GenericForeignKey)
from datetime import datetime

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    start_date = models.DateField(default=datetime.now,null=False)
    end_date = models.DateField(default=datetime.now,null=False)
    created_on = models.DateField(default=datetime.now,null=False)
    last_modified_on = models.DateField(default=datetime.now,null=False)
    def __unicode__(self):
        return self.name

class Company(models.Model):
    """Company model."""
    name = models.CharField(max_length=200)
    contact = models.ForeignKey('Contact', null=True)
    phone_number = models.CharField(max_length=50)
    fax_number = models.CharField(max_length=50)
    email_address = models.EmailField()
    created_on = models.DateField(default=datetime.now,null=False)
    last_modified_on = models.DateField(default=datetime.now,null=False)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email_address = models.EmailField()
    created_on = models.DateField(default=datetime.now,null=False)
    last_modified_on = models.DateField(default=datetime.now,null=False)
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Pledge(models.Model):
    name = models.CharField(max_length=100)
    belongs_to = models.ForeignKey('Envelope', null=False)
    is_from_contact = models.ForeignKey('Contact', null=True)
    is_from_company = models.ForeignKey('Company', null=True)
    created_on = models.DateField(default=datetime.now,null=False)
    last_modified_on = models.DateField(default=datetime.now,null=False)
    def __unicode__(self):
        return self.name

class Envelope(models.Model):
    name = models.CharField(max_length=100)
    belongs_to = models.ForeignKey('Campaign', null=False)
    created_on = models.DateField(default=datetime.now,null=False)
    last_modified_on = models.DateField(default=datetime.now,null=False)
    def __unicode__(self):
        return self.name
