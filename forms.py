from django import forms
from .models import itemlost
from .models import itemfound
from django.contrib.admin import widgets                                       


class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type='time'

class lostform(forms.ModelForm):
    product_title = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Title'}))
    #for text field     widget=forms.Textarea()
    place = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'placeholder':'Lost this thing near'}))
    date = forms.DateField(widget=DateInput,label="Date")
    time = forms.TimeField(widget=TimeInput,label="Time")
    description = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Description'}))
    contactme = forms.CharField(max_length=150,label="Contact",widget= forms.TextInput(attrs={'placeholder':'Contact'})) 
    username=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Your username (optional)',}),required=False)
    class Meta:
        model=itemlost
        fields=[
            'product_title',
            'place',
            'date',
            'time',
            'description',
            'contactme',
            'username'
        ]

class foundform(forms.ModelForm):
    product_title = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Title'}))
    #for text field     widget=forms.Textarea()
    place = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'placeholder':'Found this thing near'}))
    date = forms.DateField(widget=DateInput,label="Date")
    time = forms.TimeField(widget=TimeInput,label="Time")
    description = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Description'}))
    contactme = forms.CharField(max_length=150,label="Contact",widget= forms.TextInput(attrs={'placeholder':'Contact'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model=itemfound
        fields=[
            'product_title',
            'place',
            'date',
            'time',
            'description',
            'contactme',
            'username'
        ]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(foundform, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
'''class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter username'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    rollnumber=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter your roll number'}))
    email=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter user email'}))'''



class ClaimForm(forms.Form):
    key_details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter key details here'}))
    
