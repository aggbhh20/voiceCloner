from django import forms
class voiceCloneForm(forms.Form):
    voicePrompt = forms.CharField(label="Make Elon Say:", max_length=1000)