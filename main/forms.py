# main/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Tutor

# main/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Tutor

class StudentSignUpForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'bio', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
            student = Student.objects.create(user=user, bio=self.cleaned_data.get('bio'))
        return user

class TutorSignUpForm(UserCreationForm):
    subjects = forms.CharField()
    skills = forms.CharField()
    availability = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'subjects', 'skills', 'availability', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
            tutor = Tutor.objects.create(user=user, subjects=self.cleaned_data.get('subjects'), skills=self.cleaned_data.get('skills'), availability=self.cleaned_data.get('availability'))
        return user

    subjects = forms.CharField()
    skills = forms.CharField()
    availability = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'subjects', 'skills', 'availability', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        if commit:
            user.save()
            tutor = Tutor.objects.create(user=user, subjects=self.cleaned_data.get('subjects'), skills=self.cleaned_data.get('skills'), availability=self.cleaned_data.get('availability'))
        return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['bio']

class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['subjects', 'skills', 'availability']
