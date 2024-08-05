from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Task

@login_required
def index(request):
    choices = ['low', 'medium', 'high']
    tasks = Task.objects.all().order_by('-created')
    page_size = 6
    page = int(request.GET.get('page', 1)) 

    paginator = Paginator(tasks, page_size)
    page_tasks = paginator.get_page(page)

    
    paginator = Paginator(tasks, page_size)
    page_tasks = paginator.get_page(page)
    
    if request.htmx:
        template = 'todos_partial.html'
    
    else:
        template = 'home.html'

    if request.method == 'POST':
        subject = request.POST.get('subject')
        assigned_to = request.POST.get('assigned_to')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        notes = request.POST.get('notes')
        task = Task(user=request.user, subject=subject, assigned_to=assigned_to, due_date=due_date, priority=priority, notes=notes, is_completed=False)
        task.save()
        return render(request, 'home.html', context={"tasks" : tasks, 'choices' : choices})

    return render(request, template , context={
        "tasks": page_tasks,
        'choices': choices,
        'page': page,
        'has_next': page_tasks.has_next(),
    })

def completed(request):
    tasks = Task.objects.filter(is_completed=True)
    return render(request, 'home.html', context={"tasks" : tasks} )

def urgent(request):
    tasks = Task.objects.filter(priority='high')
    return render(request, 'home.html', context={'tasks' : tasks})

def overdue(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def partial_search(request):

    search_query = request.GET.get('query')
    if request.htmx and search_query:
        print(search_query)
        tasks = Task.objects.filter(
            Q(subject__icontains=search_query) | 
            Q(notes__icontains=search_query) | 
            Q(assigned_to__icontains=search_query)
        )
    else:
        tasks = Task.objects.all()

    return render(request, 'todos_partial.html', context={'tasks': tasks})

def complete_task(request, pk):

    tasks = Task.objects.filter(id=pk)
    tasks.update(is_completed = True)
    return redirect('/')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('/')









