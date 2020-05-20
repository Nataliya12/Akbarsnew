# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from portal.forms import *
from portal.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings

def index (request):
    return render (request, 'mainpage.html')

def login(request):
    form_log = FormLog(request.POST)
    if request.method == "POST":
        form_log = FormLog(request.POST)
        if "first_form" in request.POST:
            if form_log.is_valid(): 
                username = form_log.cleaned_data.get('mail', None)
                password = form_log.cleaned_data.get('password', None)
                
                
                user = authenticate(request, username=username, password=password)   
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect("/page/")
    else:
        form_log = FormLog()
    return render(request, 'authorization.html', {'form_log':form_log,})

def reg (request):
    form_reg = FormReg (request.POST)
    if "second_form" in request.POST:
            if form_reg.is_valid (): 
                username = form_reg.cleaned_data.get ('mail', None)
                password = form_reg.cleaned_data.get ('password', None)
                password_copy = form_reg.cleaned_data.get ('password_copy', None)
                name = form_reg.cleaned_data.get ('name', None)
                family = form_reg.cleaned_data.get ('family', None)
                registr = User.objects.create_user (username=username, password=password)
                registr.save ()
                UserProfile.objects.create (user = registr, nameuser = name, family = family)
                user = authenticate (request, username=username, password=password)   
                if user is not None:
                    auth_login (request, user)
                    return HttpResponseRedirect ('/reg_ok/')
           
    else:
        form_reg = FormReg()
    return render(request, 'reg.html', {'form_reg':form_reg,})

def red (request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'red.html'
    return render(request,
                  template)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect("/logout/")

def lk(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'lk.html'
    return render(request,
                  template)



def page(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'site.html'
    return render(request,
                  template)


def reg_ok(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'reg_ok.html'
    return render(request,
                  template)


def newday(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'newday.html'
    return render(request,
                  template)

def portal(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'portal.html'
    return render(request,
                  template)

def sertification(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    objects = Test.objects.all()
    return render(request, 'sertification.html', {'objects':objects})

def new1(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new1.html'
    return render(request,
                  template)

def new2(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new2.html'
    return render(request,
                  template)

def new3(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new3.html'
    return render(request,
                  template)

def new4(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new4.html'
    return render(request,
                  template)

def new5(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new5.html'
    return render(request,
                  template)

def new6(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new6.html'
    return render(request,
                  template)

def new7(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new7.html'
    return render(request,
                  template)

def new8(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new8.html'
    return render(request,
                  template)

def new9(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new9.html'
    return render(request,
                  template)

def new10(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new10.html'
    return render(request,
                  template)

def new11(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new11.html'
    return render(request,
                  template)

def new12(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new12.html'
    return render(request,
                  template)

def new13(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new13.html'
    return render(request,
                  template)

def new14(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new14.html'
    return render(request,
                  template)

def new15(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new15.html'
    return render(request,
                  template)

def new16(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new16.html'
    return render(request,
                  template)

def new17(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new17.html'
    return render(request,
                  template)

def new18(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new18.html'
    return render(request,
                  template)

def new19(request):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    template = 'new19.html'
    return render(request,
                  template)

def ser(request,id):
    if not request.user.is_authenticated:
        return render(request, 'error.html')
    resultat = Test.objects.get(id=id)

    
    if request.method == "POST":
        if "answer" in request.POST:
            id_question = request.POST.get('que_id')
            id_answer = request.POST.get('galochka')
            answer_for_bd =  Answer.objects.get(id=id_answer)
            answer_user = AnswerHistory.objects.get(id=id_question)
            if answer_for_bd.status == True:
                res = 1
            else:
                res = 0
            answer_user.answer = answer_for_bd.otvet
            answer_user.result = res
            answer_user.status_answer=True
            answer_user.save()
            return redirect('/sertification/%s' % id)
    
    
    if not TestHistory.objects.filter(userid=request.user, test=resultat):
        test_u = TestHistory.objects.create(userid=request.user, test=resultat)
        quet = Questions.objects.filter(test=resultat)
        for i in quet:
            if not AnswerHistory.objects.filter(questions=i, testhistory=test_u):
                AnswerHistory.objects.create(questions=i, testhistory=test_u)
    else:
        test_u = TestHistory.objects.get(userid=request.user, test=resultat)
        if test_u.status == False:
            quet = Questions.objects.filter(test=resultat)
            for i in quet:
                if not AnswerHistory.objects.filter(questions=i, testhistory=test_u):
                    AnswerHistory.objects.create(questions=i, testhistory=test_u)
    questions_for_user_false = AnswerHistory.objects.filter(testhistory=test_u, status_answer=False).order_by('?')
    questions_for_user_all = AnswerHistory.objects.filter(testhistory=test_u)
    sum = 0 
    questions_for_user_result = AnswerHistory.objects.filter(testhistory=test_u, status_answer=True)
    for i in questions_for_user_result:
        sum = sum+i.result
    return render(request, 'resultat.html', {'resultat':resultat,'questions_for_user_false':
                                             questions_for_user_false,
                                             'sum':sum,
                                             'questions_for_user_all':questions_for_user_all})
    
    