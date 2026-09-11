from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content"]
        labels = {"author": "작성자", "title": "제목", "content": "내용"}
        widgets = {
            "author": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "글 제목"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "글 내용"}),
        }