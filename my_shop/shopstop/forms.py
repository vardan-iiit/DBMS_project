from django import forms
class loginform(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()


class addcartform(forms.Form):
    userid=forms.IntegerField()
    productname=forms.CharField( max_length=50, required=True)
    quantity=forms.IntegerField()

class cartform(forms.Form):
    userid=forms.IntegerField()

class placeorderform(forms.Form):
    name=forms.CharField(max_length=25,required=False)
    phone=forms.IntegerField()
    city=forms.CharField( max_length=25, required=False)
    state=forms.CharField( max_length=25, required=False)
    country=forms.CharField( max_length=25, required=False)
    postal=forms.IntegerField()

