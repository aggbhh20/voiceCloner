from django import forms
class voiceCloneForm(forms.Form):
    voicePrompt = forms.CharField(label="Your Prompt", max_length=500)