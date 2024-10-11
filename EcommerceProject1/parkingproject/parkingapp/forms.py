from django import forms
from .models import AddVehicle,Category


class vehicleForm(forms.ModelForm):
    class Meta:
        model = AddVehicle
        fields=['id','vehicle_no','parking_area_no','vehicle_type','parking_charge','status','arrival_time']

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_no': forms.TextInput(attrs={'class':'form-control'}),
            'parking_area_no':forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_type':forms.TextInput(attrs={'class':'form-control'}),
            'parking_charge':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'}),
            'arrival_time':forms.TextInput(attrs={'class':'form-control'})
        }
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_id','parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge','status','doc']
        widgets = {
            'cat_id': forms.TextInput(attrs={'class': 'form-control'}),
            'parking_area_number': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_limit': forms.NumberInput(attrs={'class': 'form-control'}),
            'parking_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'doc': forms.DateInput(attrs={'class': 'form-control'}),
        }


class VehicleSearchForm(forms.Form):
    vehicle_number = forms.CharField(max_length=20, label='Vehicle Number')




class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

