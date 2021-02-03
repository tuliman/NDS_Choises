from django.shortcuts import render,redirect
from .models import Objects
from .forms import ObjectsForm
from .utils import prescription


def index(request):
    form = ObjectsForm()
    if request.method == 'POST':

        form = ObjectsForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('main')
        else:
            return render(request, 'choises/index.html', {'obj': form})
    else:

        result =prescription()
        return render(request, 'choises/index.html', {'obj': form,'res':result})
