from django.shortcuts import render

from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    # current_user = request.user
    # if request.method == 'POST':
    #     form = NewImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         image = form.save(commit=False)
    #         image.user = current_user
    #         image.save()
        return redirect('welcome')

    # else:
    #     form = NewImageForm()
    # return render(request, 'new_image.html', {"form": form})


    
    # return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('new-image')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})







  