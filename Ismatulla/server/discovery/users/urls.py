from django.urls import path
from users.views import (
    SignInView, SignUpView, QuestionTestView
)


urlpatterns = [
    path('signup', SignUpView.as_view(), name='sign_up'),
    path('signin', SignInView.as_view(), name='sign_in'),
    path('question-test/', QuestionTestView.as_view(), name='question-test'),
]