from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact,PatientT,DoctorT

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'contact' : forms.TextInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }


choices = (
    ('male','Male'),
    ('female','Female')
)

class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.Select(choices=choices,attrs={'class':'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
    )
   
    class Meta:
        model = User
        fields = ['username','age', 'gender','email','contact','password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            patient = PatientT.objects.create(user=user, age=self.cleaned_data['age'], gender=self.cleaned_data['gender'])
            patient.save()
        return user
    
class DoctorRegistrationForm(UserCreationForm):
    specialty = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),
        strip=False,
    )
   
    class Meta:
        model = User
        fields = ['username','specialty','email','contact','password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            doctor = DoctorT.objects.create(user=user, specialty=self.cleaned_data['specialty'])
            doctor.save()
        return user
 

relate=(
    ('you','You'),
    ('family-member','Family-Member'),
    ('relative','Relative')
)

class AppointmentRequestForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=DoctorT.objects.all(),widget=forms.Select(attrs={'class':'form-control text-white'}))