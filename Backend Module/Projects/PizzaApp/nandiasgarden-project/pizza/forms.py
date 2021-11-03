from django import forms
from .models import Pizza, Size

# This is the first version with regular forms:
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.Textarea)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

# This is the second version with ModelForm:
# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}

# This is the third version with regular form and some widgets:
# class PizzaForm(forms.Form):
#     # topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.PasswordInput)
#     # topping2 = forms.CharField(label='Topping 2', max_length=100)
#     # toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')])
#     toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

# Fourth version with ModelForm and some widgets:
# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}
#         widgets = {'topping1':forms.Textarea, 'size':forms.CheckboxSelectMultiple}

# # This is the sixth version, importing Size class elements into a single selection widget:
# class PizzaForm(forms.ModelForm): 
#     # This is our change, dont wanna empty label, good to see multiple choice check box widget
#     # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
#     size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}

# This is the seventh version, getting object from users:
class PizzaForm(forms.ModelForm): 
    # image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)