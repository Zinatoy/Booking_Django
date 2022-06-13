from django import forms
from apps.tours.models import Tour


class TourCreateForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"

class TourUpdateForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)