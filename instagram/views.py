from django.shortcuts import render,redirect
from .models import Image,Profile
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm,ProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
     
     images = Image.objects.all()

     return render(request, 'welcome.html', {"images":images})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('new-image')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})



@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(welcome)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def viewprofile(request):

    current_user = request.user
    current_user.id
    profile = Profile.objects.get(user=current_user.id)
    
    return render(request, 'viewprofile.html',{"profile":profile})
    

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(welcome)

    else:
        form = CommentsForm()
    return render(request, 'comment.html', {"form": form})


  