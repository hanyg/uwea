from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render(request, 'main/main.html', { })

