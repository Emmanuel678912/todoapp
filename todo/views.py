from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType # the user 
from .models import Task
from .forms import TaskForm

def home(request):

    # add new task
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = str(request.POST['task-name'])
            desc = str(request.POST['task-desc'])
            deadline = request.POST['deadline']

            try:
                task = Task.objects.get(task_name=name)
            except Task.DoesNotExist:
                task = Task(task_name=name)
            
            task.task_desc = desc
            task.task_deadline = deadline     
            task.save()    

            # task, created = Task.objects.get_or_create(
            #     task_name=name,
            # )

            # if task:
            #     task


                

        #messages.success(request, "You've added a task.")
        
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})



def logout_view(request):
    # check if user is logged in when logout button is pressed
    if request.POST.get('logout'):
        print("user has logged out")
        logout(request)
        return redirect('/')
    
    return render(request, 'logout.html', {})


def register(request):
    # collects customer group from database
    customers = Group.objects.get(name='customers')

    #customers.has_change_permission(request, obj=Task)
    #customers.has_view_permission(request, obj=Task)

    # task_content = ContentType.object.get_for_model(Task)

    # permission = Permission.objects.create(
    #     codename="can_update_tasks",
    #     name="Can Update Tasks",
    #     content_type=task_content
    # )

    
    # adds new user when they submit a form
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        # creates new user
        user = User.objects.create_user(is_superuser=False, username=username, password=password, last_name=lastname, first_name=firstname)

        # adds new user to customer group
        customers.user_set.add(user)

        # saves user data
        user.save()

    return render(request, 'register.html', {})

def login_view(request):

    # sends a request to database for user to login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checks if the username and password entered is in database
        user = authenticate(username=username, password=password)

        # checks if user's details exist in the database
        if user is not None:
            #messages.success(request, "Welcome Back!")
            login(request, user)

            return redirect('/')
        else:
            #messages.info(request, "Please register.")
            
            return redirect('register')

    return render(request, 'login.html', {})

def delete_task(request):
    tasks = Task.objects.all()

    for task in tasks:
        if request.method == 'POST':
            Task.delete(task)
            return redirect('/')

    return render(request, 'delete.html', {'tasks' : tasks})

def tasks(request):

    if request.method == 'POST':
        search = request.POST.get('search')

        name = Task.objects.get(task_name=search)
        task = name.task_name
        desc = name.task_desc
        deadline = name.task_deadline

        return render(request, 'tasks.html', {'task' : task, 'desc' : desc, 'deadline' : deadline})

    
    return render(request, 'tasks.html', {})
    


# FORMER UPDATE FUNCTION BELOW

# def update_task(request):
#     # update database using data submitted in form

#     f = TaskForm(request.POST)

#     if request.POST:
#         f = TaskForm(request.POST)

#         if f.is_valid():
#             task = Task.objects.filter(pk=id)
#             f = TaskForm(request.POST, instance=task)
#             f.save()
#             return redirect('/')
#         else:
#             task = Task.objects.filter(pk=id)
#             f = TaskForm(request.POST, instance=task)

#             return render(request, 'update.html', {'form' : f})


#     # tasks = []

#     # if request.user.is_authenticated:
#     #     name = Task.objects.filter(task_name)
#     #     desc = Task.objects.filter(task_deadline)
#     #     deadline = Task.objects.filter(task_deadline)

#     #     tasks.append(name, desc, deadline)
            
#     #     return render(request, 'update.html', {'tasks' : tasks})



#     return render(request, 'update.html', {'form' : f})


# when user registers add them to group (done)
    # user must login before they can add a task (done)
    # user must be logged in order to edit a task (done)
        # check if a user is logged in (done)
        # check if user is author of the task (unnecessary)
        # if user is author of task check what task they want to edit (unnecessary)
        # apply edits (unnecessary)
    # user must be logged in order to delete a task
        # check if user is logged in
        # check if user is author of task
        # check what task user wants to delete
        # delete task
    # display user's tasks on homepage
        # filter out tasks with current user's id
        # retrieve each task
        # display them on the page