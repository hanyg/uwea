from django import forms
from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Div, Submit
#from crispy_forms.bootstrap import TabHolder, Tab

from .models import Envelope, Campaign, Pledge

class EnvelopeForm(forms.ModelForm):

    class Meta:
        model = Envelope
        fields = ('name', 'desc', 'belongs_to',)

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ('name', 'desc', 'title', 'notes', 'start_date', 'end_date')

class PledgeForm(forms.ModelForm):

    class Meta:
        model = Pledge
        #fields =("name", "belongs_to", "is_from_contact", "is_from_company", "payments", "payments_cycle", "amount", "total", "recurring", "start_date", "end_date")
        fields =("name", "belongs_to", "is_from_contact", "is_from_company", "start_date", "end_date")

#class PledgeFilterForm(forms.ModelForm):
#    def __init__(self,*args, **kwargs):
#            super(PledgeFilterForm, self).__init__(*args, **kwargs)
#
#            for key in self.fields:
#                self.fields[key].required = False
#
#            self.helper = FormHelper()
#            #self.helper.add_input(Submit('submit', 'Submit'))
#
#            self.helper.layout = Layout(
#               TabHolder(
#                   Tab(
#                       'Basic Information',
#                       'name',
#                       'belongs_to'
#                   ),
#                   Tab(
#                       'Source',
#                       'is_from_contact',
#                       'is_from_company',
#                   ),
#                   Tab(
#                       'Payment Info',
#                       'payments',
#                       'payments_cycle',
#                       'amount',
#                       'total',
#                       'recurring',
#                   ),
#                   Tab(
#                       'Dates',
#                       'start_date',
#                       'end_date',
#                   ),
#               )
#            )
#
#    class Meta:
#        model = Pledge
#        fields =("name", "belongs_to", "is_from_contact", "is_from_company", "payments", "payments_cycle", "amount", "total", "recurring", "start_date", "end_date")
