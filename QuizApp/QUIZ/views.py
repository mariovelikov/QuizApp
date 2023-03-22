from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

CurrentAnsList = []
CorrectAnslist = []


def LandingPage(request):
    CurrentAnsList.clear()
    CorrectAnslist.clear()
    context = {
        'model': QuizModel.objects.all()
    }
    return render(request, 'index.html', context)

# Quiz and question's


def quiz_data(request, pk):
    test = QuizModel.objects.get(pk=pk)

    if len(CorrectAnslist) == 0:
        for x in test.get_questions():
            CorrectAnslist.append(x.correctOpt)

    paginator = Paginator(test.get_questions(), 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'questions': test,
        'count': paginator.count,
        'page': page_obj,
    }
    return render(request, 'quiz/questions.html', context)


def saveans(request, pk):
    ans = request.GET['ans']
    # print(ans)
    CurrentAnsList.append(f'{ans}')

    return HttpResponse(status=200)


def result(request, pk):
    score = 0
    answer_list_length = len(CurrentAnsList)
    num_of_questions = QuizModel(pk=pk).get_questions()

    for i in range(answer_list_length):
        if CurrentAnsList[i] == CorrectAnslist[i]:
            score += 1
        else:
            pass

    context = {
        'score': score,
        'count': len(num_of_questions)
    }

    return render(request, 'quiz/result.html', context)
