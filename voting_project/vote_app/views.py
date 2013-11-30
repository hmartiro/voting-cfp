from django.template.response import TemplateResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import datetime

from vote_app.models import Voter, Discussion, Vote

# Create your views here.

def home(request):

    voters = Voter.objects.all()
    discussions = Discussion.objects.all()

    return TemplateResponse(request, 'home.html', {'voters':voters, 'discussions':discussions})

def about(request):
	return TemplateResponse(request, 'about.html', {})

@csrf_exempt
def vote(request):
    
    if request.method == 'GET':
        raise Http404

    voter_name = request.POST['voter']
    discussion_name = request.POST['discussion']
    vote_val = request.POST['vote']

    voter = Voter.objects.get(name=voter_name)
    discussion = Discussion.objects.get(name=discussion_name)

    vote = Vote(voter=voter, discussion=discussion, value=vote_val)
    print('saving new vote: %s' % vote)
    vote.save()

    return HttpResponse('')

def view_home(request):
    discussions = Discussion.objects.all()
    return TemplateResponse(request, 'view_home.html', {'discussions': discussions})

def view(request, discussion_id):
    
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    votes = Vote.objects.filter(discussion=discussion).order_by('time')
    
    start_time = votes[0].time
    start_time_str = start_time.strftime("%H:%M on %A %d. %B %Y")

    times = [(v.time - start_time) for v in votes]
    times = [t.total_seconds() for t in times]

    values = [v.value for v in votes]
    print times
    return TemplateResponse(request, 'view.html', 
        {
        'discussion': discussion, 
        'votes': votes, 
        'times': times, 
        'values': values,
        'start_time': start_time_str,
        })
