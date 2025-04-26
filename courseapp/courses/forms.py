from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="Kurs basligi",
        required=True,
        error_messages={"required":"kurs basligi girmelisiniz"},
        widget=forms.TextInput(attrs={"class" : "form-control"})
    )

    description = forms.CharField(widget= forms.Textarea(attrs={"class" : "form-control"}))
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
    slug = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
