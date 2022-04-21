from django import forms
from .models import Algorithm, Solution, Solution_Comment

class AlgorithmForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '제목',

                }
            ),
        )
    
    site_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'url',

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

    input = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '입력',

                }
            ),
        ) 
    output = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '출력',

                }
            ),
        )     
    constricts = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '제한사항',

                }
            ),
        )     

    examples = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '예시',

                }
            ),
        )     
    level = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': '레벨',

                }
            ),
        )    
    class Meta:
        model = Algorithm
        exclude = ('user', 'like_users',)




class SolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
        exclude = ('user', 'like_users',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Solution_Comment
        exclude = ('user', 'like_users',)