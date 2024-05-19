from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import voiceCloneForm
from gradio_client import Client

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the voiceClonerApp index.")
# def voiceCloneView(request):
#     form=voiceCloneForm()
#     return render(request, "C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html")
class CustomSchemeRedirect(HttpResponseRedirect):
    allowed_schemes = ['html', 'htm', 'xml', 'xhtml', 'c']
class CustomSchemeResponse(HttpResponse):
    allowed_schemes = ['html', 'htm', 'xml', 'xhtml', 'c']

async def voiceCloneView(request):
    form = voiceCloneForm()
    if request.method == "POST":
        form = voiceCloneForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data["voicePrompt"]
            client = Client("https://myshell-ai-openvoicev2.hf.space/--replicas/nx4jp/")
            result = client.predict(
		        prompt,	# str  in 'Text Prompt' Textbox component
		        "en_default",	# str (Option from: [('en_default', 'en_default'), ('en_us', 'en_us'), ('en_br', 'en_br'), ('en_au', 'en_au'), ('en_in', 'en_in'), ('es_default', 'es_default'), ('fr_default', 'fr_default'), ('jp_default', 'jp_default'), ('zh_default', 'zh_default'), ('kr_default', 'kr_default')]) in 'Style' Dropdown component
		        "C:\\Users\\noh\\Downloads\\actualllytruummmp.mp4",	# str (filepath on your computer (or URL) of file) in 'Reference Audio' Audio component
		        True,	# bool  in 'Agree' Checkbox component
		        fn_index=1
            )
            #do the api stuff


            print("api stuff done")
            print(result)
            print(result[1])
            response = HttpResponse(result[1], content_type="audio/wav")
            response["Content-Disposition"] = "attachment; filename=voiceClone.wav"
            return CustomSchemeResponse(response)
            # return CustomSchemeResponse(result[1],
            # headers={
            #     "Content-Type": "audio/vnd.wav",
            #     "Content-Disposition": "attachment; filename=voiceClone.wav",
            # },
            # )
        else:
            print("wrong form")
            form=voiceCloneForm()
            return render(request, "C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html", {"form": form})
    else:
       print("not post")
       form=voiceCloneForm()
       return render(request, "C:\\Users\\noh\\voiceCloner\\voiceCloner\\voiceCloner\\templates\\voiceClone.html", {"form": form})