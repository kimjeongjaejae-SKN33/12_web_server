from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    # subject·content → 필수 여부·최대 길이 검증 → cleaned_data → View의 저장 분기에 사용한다.
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {'subject': '제목', 'content': '내용'}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content': '답변 내용'}