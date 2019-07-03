from django import forms
from .models import Board,Hashtag, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','body','image']
        widgets={"image":forms.FileInput}

class HashtagForm(forms.ModelForm):
    class Meta:
        model=Hashtag
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
