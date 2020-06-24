from django.shortcuts import render, reverse, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from bugApp.forms import LoginForm, TicketAddForm, TicketEditForm
from bugApp.models import Ticket, SomeUser


@login_required
def index(request):
    new = Ticket.objects.filter(status='New')
    in_progress = Ticket.objects.filter(status='In Progress')
    done = Ticket.objects.filter(status='Done')
    return render(request, 'index.html', {
        'done': done,
        'in_progress': in_progress,
        'new': new})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    html = 'base_form.html'
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def ticketview(request, id):
    data = Ticket.objects.filter(id=id)
    return render(request, 'ticketview.html', {
        'data': data,
        'username': request.user.username
    })

@login_required
def ticketadd(request):
    html = 'base_form.html'
    if request.method == 'POST':
        form = TicketAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title = data['title'],
                description = data['description'],
                author = request.user
            )
            return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.latest('id').id))

    form = TicketAddForm()
    return render(request, html, {'form': form})

@login_required
def ticket_edit(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.assigned = data['assigned']
            ticket.compleated = data['compleated']
            ticket.status = data['status']
            ticket.save()
            return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.get(id=id).id))

    form = TicketEditForm(initial={
        'title': ticket.title,
        'description': ticket.description,
        'assigned': ticket.assigned,
        'compleated': ticket.compleated,
        'status': ticket.status 
    })

    return render(request, 'base_form.html', {'form': form})

def profile(request, username):
    user = SomeUser.objects.get(username=username)
    data = Ticket.objects.filter(author=user)
    return render(request, 'profile.html', {
        'data':data,
        'username': user.username
    })


def assign(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.get(id=id).id))

def unassign(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned = None
    ticket.status = 'New'
    ticket.save()
    return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.get(id=id).id))

def compleat(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.compleated = ticket.assigned
    ticket.assigned = None
    ticket.status = 'Done'
    ticket.save()
    return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.get(id=id).id))

def invalid(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.assigned = None
    ticket.compleated = request.user
    ticket.status = 'Invalid'
    ticket.save()
    return HttpResponseRedirect('/ticket/'+ str(Ticket.objects.get(id=id).id))

