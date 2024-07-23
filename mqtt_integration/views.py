from django.http import HttpResponse
from django.shortcuts import render, redirect
from .mqtt import publish_message, subscribe_topic, get_received_messages

def publish_message_view(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        message = request.POST.get('message')
        print(topic," ",message)
        request.session['published_topic'] = topic
        publish_message(topic, message)
        return HttpResponse('Message published successfully!')
    return render(request, 'mqtt_integration/publish_message.html')

def subscribe_topic_view(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        print(topic)
        published_topic = request.session.get('published_topic')
        if topic == published_topic:
            subscribe_topic(topic)
            return redirect('display_messages')
    return render(request, 'mqtt_integration/subscribe_topic.html')

def display_messages(request):
    messages = get_received_messages()
    print(f'Displaying messages: {messages}')
    return render(request, 'mqtt_integration/messages.html', {'messages': messages})
