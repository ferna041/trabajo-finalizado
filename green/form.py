from .models import Comment, Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('description','grado',"asignatura_Media","asignatura_Basica","image","contacto","dato_de_contacto")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({"class": "form-control"})




class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Comment Something...'
            }),
        required=True
        )

    class Meta:
        model=Comment
        fields=['comment']