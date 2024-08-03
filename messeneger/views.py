from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q




@login_required(login_url='users/sign_in')
def home(request):
    users = User.objects.all()  
    search = request.GET.get('search', '')
    if search:
        search_results = users.filter(
            Q(name__icontains=search) |
            Q(category__name__icontains=search) |
            Q(company__name__icontains=search)
        )
        if not search_results.exists():
            search_results = users
        users = search_results

    return render(request, 'home.html', {
        'users': users,
    })

