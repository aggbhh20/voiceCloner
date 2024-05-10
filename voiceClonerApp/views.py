from django.shortcuts import render
from django.http import HttpResponse
from .forms import voiceCloneForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the voiceClonerApp index.")
# def voiceCloneView(request):
#     form=voiceCloneForm()
#     return render(request, "C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html")
def voiceCloneView(request):
    form = voiceCloneForm()
    if request.method == "POST":
        form = voiceCloneForm(request.POST)
        if form.is_valid():
            #do the api stuff
            print("api stuff done")
            return HttpResponseRedirect("C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html")
        else:
            form=voiceCloneForm()
    return render(request, "C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html", {"form": form})