from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import ResourceForm, MeetingForm
from .models import Resource, Meeting
# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')

@login_required
def newResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/resource.html', {'form': form})

@login_required
def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/meeting.html', {'form': form})


# @login_required
def getResource(request):
    resources_list=Resource.objects.all()
    return render(request, 'club/resourcelist.html', {'resources_list': resources_list})

# @login_required
def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetinglist.html', {'meeting_list': meeting_list})

# @login_required
def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    meetingdate=meet.meetingdate
    context={
        'meet' : meet,
        'meetingdate' : meetingdate,
    }
    return render(request, 'club/meetingdetails.html', context=context)
