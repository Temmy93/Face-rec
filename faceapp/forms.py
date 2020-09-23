from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth import authenticate

from faceapp.models import Admin, Student


class AdminRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = Admin
        fields = ('firstname', 'surname', 'staff_number', 'department', 'phone', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = Student
        fields = ('firstname', 'surname', 'matric_number',
                  'department', 'phone', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        print(self.cleaned_data)
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = kwargs.get("request")
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password, user_category=self.user_category)
            if self.user_cache is None:
                raise ValidationError("Invalid Username or Password")

        return self.cleaned_data

    def save(self):
        return self.user_cache


class StudentLoginForm(LoginForm):
    user_category = "student"


class AdminLoginForm(LoginForm):
    user_category = "admin"


class StudentImageUpload(forms.ModelForm):
    img = forms.ImageField(allow_empty_file=False)

    class Meta:
        model = Student
        fields = ("img",)
