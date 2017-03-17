from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import Envelope
from .forms import EnvelopeForm

def donations(request):
    envelopes = Envelope.objects.order_by('created_on')
    return render(request, 'donations/donations.html', { 'envelopes': envelopes })

def envelope_detail(request, pk):
    e = get_object_or_404(Envelope, pk=pk)
    return render(request, 'donations/envelope_detail.html', {'e': e})

def envelope_new(request):
    if request.method == "POST":
        form = EnvelopeForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            #e.created_by = request.user
            e.created_on = timezone.now()
            e.last_modified_on = timezone.now()
            e.save()
            return redirect('envelope_detail', pk=e.pk)
    else:
        form = EnvelopeForm()
    return render(request, 'donations/envelope_edit.html', {'form': form})


def envelope_edit(request, pk):
    envelope = get_object_or_404(Envelope, pk=pk)
    if request.method == "POST":
        form = EnvelopeForm(request.POST, instance=envelope)
        if form.is_valid():
            envelope = form.save(commit=False)
            #envelope.created_by = request.user
            envelope.created_on = timezone.now()
            envelope.last_modified_on = timezone.now()
            envelope.save()
            return redirect('envelope_detail', pk=envelope.pk)
    else:
        form = EnvelopeForm(instance=envelope)
    return render(request, 'donations/envelope_edit.html', {'form': form})
