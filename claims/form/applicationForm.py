from django import forms
from django.db.models.fields import FilePathField
from django.db.models.fields.files import FileField
from django.forms import TextInput, Select, FileInput, NumberInput, Textarea
from django.forms.widgets import DateInput, DateTimeInput
from claims.models import Claim


GEEKS_CHOICES =( 
    ("1", "Yes"), 
    ("2", "No"),  
) 

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Name'}),
            'email': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Email'}),
            'mob': NumberInput(attrs={'class': 'form-control', 'id': 'price','placeholder': 'Enter Mobile Number'}),
            'vehicle_year_make': DateInput(attrs={'class': 'form-control', 'id': 'description','placeholder': 'Enter Vehicle Year Make'}),
            'vehicle_model': TextInput(attrs={'class': 'form-control', 'id': 'price','placeholder': 'Enter Model'}),
            'vehicle_no': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter No'}),
            'accident_time': DateTimeInput(attrs={'class': 'form-control', 'id': 'product_image', 'placeholder': 'Enter Accident Time'}),
            'location_of_loss': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter Location of Loss'}),
            'type_of_loss': Select(attrs={'class':'form-control', 'id': 'title', 'placeholder': 'Enter Product Name'},choices=[('0', '---------'),('Own Damage', 'Own Damage'),('Knock For Knock', 'Knock For Knock'),('Windscreen Damage', 'Windscreen Damage'),('Theft', 'Theft')]),
            'description_of_loss': Textarea(attrs={'class': 'form-control', 'id': 'product_image'}),
            'policy_report_lodge': Select(attrs={'class':'form-control', 'id': 'title', 'placeholder': 'Enter Product Name'},choices=[('0', '---------'),('Yes', 'Yes'),('No', 'No')]),
            'any_body_injured': Select(attrs={'class':'form-control', 'id': 'title', 'placeholder': 'Enter Product Name'},choices=[('0', '---------'),('Yes', 'Yes'),('No', 'No')]),
            'loss_image': FileInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Upload Loss Image'}),
            'docfile': FileInput(attrs={'class': 'form-control', 'id': 'documents', 'placeholder': 'Upload Documents'}),
            'approve': TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Approved'}),
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        choices = [ ('1', 'Yes'),('LP', 'No'),]
        self.fields['any_body_injured'].choices = choices
     