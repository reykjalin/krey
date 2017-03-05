from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    def getUser(self):
        return user_name
    def getPassword(self):
        return password
