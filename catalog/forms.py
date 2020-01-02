from django import forms

class GenreForm(forms.Form):
    name = forms.CharField(label='Genre name', max_length=100)



class AuthorForm(forms.Form):
	first_name = forms.CharField(label = "First name", max_length=100)
	last_name = forms.CharField(label = "Last name", max_length=100)
	date_of_birth = forms.DateField(label = "DOB",input_formats = ['%Y-%m-%d','%d/%m/%Y','%m/%d/%y'])
	date_of_death = forms.DateField(label = "Died", required=False)