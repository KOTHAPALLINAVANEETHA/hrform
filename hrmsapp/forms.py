from django import forms
from .models import Personal
from .models import Official
from .models import Leave



class PersonalForm(forms.ModelForm):
	DOB = forms.DateField(label='date of birth',widget = SelectDateWidget(required = True, years = range(2020, 1970, -1)))
    bloodgroup = forms.ChoiceField(choices=BLOODGROUPS,required=True)
    marital_status = forms.ChoiceField(choices=MARITALSTATUS,required=True)
    
    class Meta:
    	model = Personal

class OfficialForm(forms.ModelForm):
	Designations = forms.ChoiceField(choices=DESIGNATIONS,required=True)
	DOJ = forms.DateField(label='date of joining',widget= SelectDateWidget(required=True))
    Departments = forms.ChoiceField(choices=DEPARTMENTS,required=True)


	class Meta:
		model = Official

class LeaveForm(forms.ModelForm):
	leaves = forms.ChoiceField(choices=LEAVES, required=True)

	class Meta:
		model = Leave
