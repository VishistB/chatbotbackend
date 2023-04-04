from django.http import HttpResponse
from django.views import View
from django.shortcuts import render,redirect
from chatbotbackend.chatbotdeployment.chat import get_response

def chatPage(request):
    # return HttpResponse('Hi check')
    resp="I would be happy to answer Your questions"
    if request.method == 'POST' and 'text_button' in request.POST:
        user_input = request.POST.get('prompt')
        resp=get_response(user_input)
        # request.session['resp'] = resp
        # print(resp)

    context={'resp':resp}
    return render(request,'chatPage.html',context)