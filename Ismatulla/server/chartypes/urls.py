from django.urls import path
from .views import (
    QuestionTestView
)
urlpatterns=[
    path('question-test/', QuestionTestView.as_view(), name='question-test'),
]