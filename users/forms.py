from django import forms

from users.models import CustomUser


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','profile_pic','job','password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()



class ProfileForm(forms.ModelForm):
    JOB_CHOICES = [
        ('Frontend','Frontend'),
        ('Backend','Backend'),
        ('FullStack', 'FullStack'),
        # Add more job choices as needed
    ]

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_pic', 'job')