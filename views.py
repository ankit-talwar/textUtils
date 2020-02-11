from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'Defualt')
    removePunc = request.GET.get('removePunc', 'off')
    upprCase = request.GET.get('upCase', 'off')
    count = request.GET.get('count', 'off')
    space = request.GET.get('spaceRem','off')
    space_inline = request.GET.get('space_l','off')

    # print(djtext)
    if removePunc == "on":
        analyzed = ""
        punctuation = '''!@#$%^&*()_+=-/*.'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        param = {'purpose': 'remove punctuation', 'analysis': analyzed}
        return render(request, 'analyze.html', param)
    elif upprCase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'converting to upper case', 'analysis': analyzed}
        return render(request, 'analyze.html', param)
    elif count == "on":

        analyzed = int(len(djtext))
        param = {'purpose': 'counting no of chars in text', 'analysis': analyzed}
        return render(request, 'analyze.html', param)
    elif space == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        param = {'purpose':'space remover','analysis':analyzed}
        return render(request,'analyze.html',param)
    elif space_inline == "on":
        analyzed = ""
        for char in djtext:
            if char != " " and char != "  ":
                analyzed = analyzed + char

        param = {'purpose':'removing spaces','analysis':analyzed}
        return render(request,'analyze.html',param)
    else:
        return "ERROR"
