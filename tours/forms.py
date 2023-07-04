from django.forms import ModelForm, Textarea, TextInput
from .models import Contect, Reservation, Contact
from django import forms

Destination =['Maasai Mara','Samburu','Amboseli and Tsavo','Mombasa','Malindi','Zanzibar','Dubai','Nairobi Excursions','Tanzania','Conferences and HoneyMo']
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["dest","fname","email","pno","sdate","fdate","gender","country","city","no_child","no_adults"]
        widgets ={
            "dest" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Place to Visit","style":"width: 300px;", "class":"form-control"}),
            "fname" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Full Name ","style":'width: 300px;',"class":"form-control"}),
            "email" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Email Address","style":'width: 300px;',"class":"form-control"}),
            "pno" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Phone Number","style":'width: 300px;',"class":"form-control"}),
            "sdate" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Start Date of Tour  yy-mm-dd","style":'width: 300px;',"class":"form-control"}),
            "fdate" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Last Date of Tour yy-mm-dd","style":'width: 300px;',"class":"form-control"}),
            "gender" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter Your Preferred Gender","style":'width: 300px;',"class":"form-control"}),
            "country" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Place to Visit","style":'width: 300px;',"class":"form-control"}),
            "city" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter City of Origin","style":'width: 300px;',"class":"form-control"}),
            "no_child" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter the Number  of Children  Travelling","style":'width: 300px;',"class":"form-control"}),
            "no_adults" : Textarea(attrs={"cols" : 60, "rows" : 1, "placeholder" : "Enter the Number  of Children  Travelling","style":'width: 300px;',"class":"form-control"}),
         }
        labels ={
            "dest":("Destination :"),
            "fname":("Full Name :"),
            "email":("Email Address:"),
            "pno": ("Phone Number:"),
            "sdate": ("Start Date:"),
            "fdate": ("Final Date:"),
            "gender": ("Enter Gender:"),
            "country":("Country of Origin :"),
            "city":("City of Origin:"),
            "no_child":("No of children:"),
            "no_adults":("No of adults:")
        }



# class ContactForm(forms.Form):
#     email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(required=True)
class ContactForm(ModelForm):
    class Meta:
            model = Contact
            fields = ["message","email","subject"]
            widgets ={
                "message" : TextInput(attrs={"cols" : 40, "placeholder" : "Enter your Name","style":'width: 300px;',"class":"form-control"}),
                "email" : TextInput(attrs={"cols" : 40,  "placeholder" : "Enter Email Address","style":'width: 300px;',"class":"form-control"}),
                # "phone" : TextInput(attrs={"cols" : 40,  "placeholder" : "Enter Phone Number","style":'width: 300px;',"class":"form-control"}),
                "subject" : Textarea(attrs={"cols" : 40,  "placeholder" : "Enter Subject ","style":'width: 300px;',"class":"form-control"}),
            }
            labels ={
                "mesage":("Input your message:"),
                "email":("Email Address:"),
                "subject": ("Enter subject:")
            }

class PackSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search')



select_mode_of_contect = (
    ("email", "E-mail"),
    ("phone", "Phone"),
)

select_question_categories = (
    ("certification","Certification"),
    ("interview","Interview"),
    ("material","Material"),
    ("access_duration","Access and Duration"),
    ("other","Others"),
)
class ContectForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    mode_of_contect = forms.CharField(required = False, widget=forms.RadioSelect(choices =select_mode_of_contect))
    question_categories = forms.CharField(required= False, widget=forms.Select(choices=select_question_categories))

    class Meta:
        model = Contect
        fields = '__all__'