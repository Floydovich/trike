from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from apps.tickets.models import Ticket


class HomePageView(TemplateView):

    # noinspection PyMethodOverriding
    def get(self, request):
        tickets = Ticket.objects.all()

        return render(request, 'home.html', {'tickets': tickets})


class TicketDetail(TemplateView):

    # noinspection PyMethodOverriding
    def get(self, request, id):
        ticket = Ticket.objects.get(id=id)

        return render(
            request,
            'ticket_detail.html',
            {'ticket': ticket, 'next_status': ticket.next_status}
        )


class TicketStatus(View):

    def post(self, request, id):
        ticket = Ticket.objects.get(id=id)
        status = request.POST['status']

        if status not in Ticket.Status.values:
            return HttpResponse(status=404)

        ticket.status = status
        ticket.save()

        return redirect(reverse('ticket-detail', args=[id]))


class NewTicket(TemplateView):

    # noinspection PyMethodOverriding
    def get(self, request):
        kinds = Ticket.Kind.values
        return render(request, 'new_ticket.html', {'kinds': kinds})

    def post(self, request):
        Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            kind=request.POST['kind']
        )
        return redirect('/')
