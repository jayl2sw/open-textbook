from django import forms
from .models import Anonymous, Comment

class AnonymousForm(forms.ModelForm):
    title = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': '제목',

            }
        ),
    )
    content = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': '내용',
            }
        ),
    )    
    

    class Meta:
        model = Anonymous
        exclude = ('user','like_users', 'view_cnt',)


class CommentForm(forms.ModelForm):


    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
    )
    
    class Meta:
        model = Comment
        fields = ('content',)