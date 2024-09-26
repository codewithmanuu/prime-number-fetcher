from django import forms
from simple_primes import settings

class InputForm(forms.Form):
    input_number = forms.IntegerField(max_value=int(settings.LIMIT))

    def clean_input_number(self):
        input_number = self.cleaned_data.get('input_number')
        
        if input_number is None: 
            raise forms.ValidationError("This field is required.")
        
        if input_number <= 0:
            raise forms.ValidationError("The Number should be greater than 0.")
        
        return input_number
