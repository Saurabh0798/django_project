from django import forms

class ContactForm(forms.Form):
    your_name= forms.CharField(label='Your Name', max_length=20)
    your_email=forms.EmailField(label='Email')
    mobile_number=forms.IntegerField(label='Mobile')
    your_city=forms.CharField(label='City',max_length=10)
