from django import forms 

class FormForHub(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=400)

    def send_info(self):
        pass