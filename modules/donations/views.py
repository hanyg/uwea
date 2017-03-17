from django.shortcuts import render
from .models import Envelope

def donations(request):
    envelopes = Envelope.objects.order_by('created_on')
    return render(request, 'donations/donations.html', { 'envelopes': envelopes })
