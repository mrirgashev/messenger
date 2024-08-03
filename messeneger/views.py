from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Message
from django.contrib.auth.models import User
from django.db.models import Q
from . forms import MessageForm

@login_required(login_url='users/sign_in')
def home(request):
    users = User.objects.all()  
    current_user = request.user
    search = request.GET.get('search', '')
    if search:
        search_results = users.filter(
            Q(username__icontains=search) 
        )
        if not search_results.exists():
            search_results = users
        users = search_results

    return render(request, 'home.html', {
        'users': users,
        'current_user':current_user,
    })


@login_required
def chat(request, receiver_id):
    # Get the receiver user
    receiver = User.objects.get(id=receiver_id)
    # Get the sender user (current logged-in user)
    sender = request.user
    users = User.objects.all()  

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.receiver = receiver
            message.save()
            return redirect('messeneger:chat', receiver_id=receiver_id)  # Use receiver_id, not the receiver object
    else:
        form = MessageForm()

    # Get messages between sender and receiver
    messages = Message.objects.filter(
        (Q(sender=sender) & Q(receiver=receiver)) | 
        (Q(sender=receiver) & Q(receiver=sender))
    ).order_by('timestamp')

    context = {
        'receiver': receiver,
        'messages': messages,
        'form': form,
        'users': users,
        'current_user': request.user,  # Include the current user in the context for the template to display their username in the navbar.  # Use receiver_id, not the receiver object.  # Include the current user in the context for the template to display their username in the navbar.  # Use receiver_id, not the receiver object.  # Include the current user in the context for the template to display their username in the navbar.
    }
    return render(request, 'chat.html', context)