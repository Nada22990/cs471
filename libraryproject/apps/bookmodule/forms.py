from django import forms
from .models import Book,Student,Address,Student33,Address33,Profile2


class BookForm(forms.ModelForm):  
    class Meta:
        model = Book
        fields = ['title', 'author','price','edition']

##############################################################Task1
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

################################################################Task2

class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student33
        fields = '__all__'
        
class AddressForm2(forms.ModelForm):
    class Meta:
        model = Address33
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile2
        fields = ['name', 'photo']


