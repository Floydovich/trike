from django.shortcuts import render, redirect

from apps.tickets.models import Ticket


def home_page(request):
    if request.method == 'POST':
        Ticket.objects.create(title=request.POST['ticket_title'],
                              description=request.POST['ticket_description'])
        return redirect('/')

    tickets = Ticket.objects.all()

    return render(request, 'home.html', {'tickets': tickets})


def ticket_details(request, id):
    ticket = Ticket.objects.get(id=id)

    return render(request, 'ticket_details.html', {'ticket': ticket})
