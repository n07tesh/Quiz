from django.shortcuts import render,HttpResponse
from . models import Quiz
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home.html')

def quiz(request):
    questions = Quiz.objects.all().order_by('-id')
    paginator = Paginator(questions,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request,'App/quiz.html',context)


score = 0

def answer(request):
    questions = Quiz.objects.all()
    global score
    for question in questions:
        correct_answer = question.answer
        entered_answer = request.POST.get(str(question.id))
        if(entered_answer == correct_answer):
            score+=1
        context = {'score':score}
        #return HttpResponse('<h1>Successfully Submit</h1>')
        return render(request,'App/answer.html',context)


def certificate(request):
    global score
    context = {'score':score}
    return render(request,'App/certificate.html',context)

#def leader(request):
  #  adr=Quiz.objects.all()
  #  usr=User.objects.all()
   # context = {'usr':usr,'adr':adr}
   # return render(request,'App/leader.html',context)