from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    if request.method == 'POST':
        return render(request, 'home.html', {
            'new_ticket_title': request.POST.get('ticket_title', ''),
        })
    return render(request, 'home.html')
