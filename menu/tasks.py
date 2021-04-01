from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect

from .models import Menu
from .forms import MenuForm
import slack
from django.conf import settings


from celery.task.schedules import crontab
from celery.decorators import periodic_task





@periodic_task(
    run_every=(crontab(minute='*/35')),
    name="menu_send",
    ignore_result=True
)
def send(request,pk):
    context ={}
    menu = get_object_or_404(Menu,pk=pk)
    uuid=str(menu.unique_id)
    client = slack.WebClient(token=settings.SLACK_TOKEN)
    client.chat_postMessage(channel='job', text=settings.SLACK_URL+uuid)
