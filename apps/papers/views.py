from rest_framework import viewsets
from .models import Answers, Students, Questions, Papers
from .serializers import (
    AnswersSerializer,
    StudentsSerializer,
    QuestionsSerializer,
    PapersSerializer,
)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    serializer_class = PapersSerializer
