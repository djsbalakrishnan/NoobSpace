from django import forms

class Login(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Username'}), label="Username", max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Password'}), label="Password")

class Register(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Username'}), label="Username", max_length=100)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Email Address'}),label="Email Address")
	fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'First Name'}), label="First Name", max_length=100)
	lname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Last Name'}), label="Last Name", max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Password'}), label="Password")
	cpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'Confirm Password'}), label="Confirm Password")