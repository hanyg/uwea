from django.shortcuts import render

def donations(request):
    return render(request, 'donations/donations.html', {})
