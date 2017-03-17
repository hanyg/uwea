from django.shortcuts import render, get_object_or_404
from .models import Envelope

def donations(request):
    envelopes = Envelope.objects.order_by('created_on')
    return render(request, 'donations/donations.html', { 'envelopes': envelopes })


def envelope_detail(request, pk):
    e = get_object_or_404(Envelope, pk=pk)
    return render(request, 'donations/envelope_detail.html', {'e': e})
