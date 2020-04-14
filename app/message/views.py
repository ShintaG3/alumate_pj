from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from .models import Message
from .forms import MessageForm, ReplyForm
from datetime import datetime
from itertools import chain
from accounts.models import Follow


# Create your views here.
class MessageListView(LoginRequiredMixin, View):
    template_name = 'message/message-list.html'
    form_class = MessageForm
    
    def get(self, request, *args, **kwargs):
        user = request.user

        message_list = self.get_latest_message_list(user)


        following_ids = Follow.objects.filter(follower=user).values_list('followed', flat=True)
        following_users = User.objects.filter(id__in=following_ids)

        new_message_form = self.form_class(choices=following_users)


        context = {
            'message_list': message_list,
            'new_message_form': new_message_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.sent_datetime = datetime.now()
            message.save()
        return HttpResponseRedirect(self.request.path_info)


    def get_latest_message_list(self, user):
        sender_list = Message.objects.filter(receiver=user).values_list('sender', flat=True)
        receiver_list = Message.objects.filter(sender=user).values_list('receiver', flat=True)

        received_message_list = []
        for sender in sender_list:
            latest_message = Message.objects.filter(sender=sender)[0]
            received_message_list.append(latest_message)
        
        sent_message_list = []
        for receiver in receiver_list:
            latest_message = Message.objects.filter(receiver=receiver)[0]
            sent_message_list.append(latest_message)

        sender_and_receiver_set = set(chain(sender_list, receiver_list))
        sent_and_received_message_list = sorted(chain(received_message_list, sent_message_list), key=lambda x: x.sent_datetime, reverse=True)

        latest_message_list = []
        for message in sent_and_received_message_list:
            new_user = None
            if message.sender == user and message.receiver.id in sender_and_receiver_set:
                new_user = message.receiver
            elif message.receiver == user and message.sender.id in sender_and_receiver_set:
                new_user = message.sender
            
            if new_user:
                latest_message_list.append(message)
                sender_and_receiver_set.remove(new_user.id)
        
        return latest_message_list

class MessageDetailView(LoginRequiredMixin, View):
    template_name = 'message/message-detail.html'
    form_class = ReplyForm

    def get(self, request, *args, **kwargs):
        user = request.user
        to_user = get_object_or_404(User, username=kwargs['username_to'])

        received_messages = Message.objects.filter(sender=to_user, receiver=user)
        sent_message = Message.objects.filter(sender=user, receiver=to_user)
        messages = sorted(chain(received_messages, sent_message), key=lambda x: x.sent_datetime)

        form = self.form_class()

        content = {
            'to_user': to_user,
            'messages': messages,
            'new_reply_form': form
        }
        return render(request, self.template_name, content)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        to_user = get_object_or_404(User, username=kwargs['username_to'])
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = to_user
            message.sent_datetime = datetime.now()
            message.save()
        return HttpResponseRedirect(self.request.path_info)