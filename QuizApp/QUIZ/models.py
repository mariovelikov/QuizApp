from django.db import models


class QuizModel(models.Model):
    title = models.CharField(max_length=150)

    def get_questions(self):
        return self.questionsans_set.all()

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Quiz'


class QuestionsAns(models.Model):
    test = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    option1 = models.CharField(max_length=180)
    option2 = models.CharField(max_length=180)
    option3 = models.CharField(max_length=180)

    correctOpt = models.CharField(max_length=180)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Questions_Answers'
