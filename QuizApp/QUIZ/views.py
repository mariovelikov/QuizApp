from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.core.paginator import Paginator

lst = []
anslist = []


def LandingPage(request):
    lst.clear()
    anslist.clear()
    context = {
        'model': QuizModel.objects.all()
    }
    return render(request, 'index.html', context)

    # Quiz and question's


def quiz_data(request, pk):
    test = QuizModel.objects.get(pk=pk)
    for x in test.get_questions():
        anslist.append(x.correctOpt)
        print()

    test = QuizModel.objects.get(pk=pk)
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
    lst.append(ans)


def result(request, pk):
    score = 0

    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 1
        else:
            score += 0

    context = {
        'score': score,
        'count': lst.count
    }

    return render(request, 'quiz/result.html', context)


def delete(request):
    lst.clear()
    print(lst)
