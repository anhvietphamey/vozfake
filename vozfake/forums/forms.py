from django import forms

class LoanInfo(forms.Form):
	start_principal = forms.CharField(max_length=14)
	periods = forms.IntegerField(max_value=600,min_value=1)
	ir = forms.DecimalField(max_value = 20.00,min_value =0.00,decimal_places=2,max_digits=4)
	start_date = forms.DateField()