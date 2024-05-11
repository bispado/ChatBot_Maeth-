from django.shortcuts import render, redirect
from .models import Message
from . import ai

# Create your views here.
def home(request):
    return render(request, 'index.html',)

def chat(request):
    messages = Message.objects.all()
    context = {'messages': messages}

    if request.method == 'POST':
        user_message = Message(body = request.POST.get('message'))

        ai_response = ai.get_ai_response(user_message.body)
        ai_message = Message(body = ai_response)
    
        user_message.save()
        ai_message.save()

        redirect('chat')

    return render(request, 'chat.html', context=context)

def resetarChat(request):
    Message.objects.all().delete()
    return redirect('chat')