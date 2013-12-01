from django.template.response import TemplateResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import datetime
import math

from vote_app.models import Voter, Discussion, Vote

# Create your views here.

def home(request):

    voters = Voter.objects.all()
    discussions = Discussion.objects.filter(active=True)

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
    
    if(len(votes) == 0):
        return TemplateResponse(request, 'no_votes.html', {'discussion': discussion})

    start_time = votes[0].time
    start_time_str = start_time.strftime("%H:%M on %A %d. %B %Y")

    times = [(v.time - start_time) for v in votes]
    times = [t.total_seconds() for t in times]

    values = [v.value for v in votes]

    # Constants to play with
    FPS = 5.
    FADE_TIME = 10.

    m_times, m_up, m_down = generate_momentum_plot(times, values, FPS, FADE_TIME)

    return TemplateResponse(request, 'view.html', 
        {
            'discussion': discussion, 
            'votes': votes, 
            'times': times, 
            'values': values,
            'start_time': start_time_str,
            'm_times': m_times,
            'm_up': m_up,
            'm_down': m_down,
            'fps': FPS,
            'fade_time': FADE_TIME,
        })

def generate_momentum_plot(times, values, fps, fade_time):

    # Generate time steps
    m_times = [t/fps for t in range(0, int((times[-1] + fade_time + 1) * fps))]
    print m_times

    # Lists to store the momentum streams
    momentum_up = []
    momentum_down = []

    # For each time step
    for t in m_times:

        m_up = 0.
        m_down = 0.

        # Iterate through vote times
        for i in range(0, len(times)):

            # If this vote is after the time step, move on
            if(times[i] > t):
                break

            # How long ago was the vote cast?
            dt = t - times[i]

            # Scale linearly such that a vote with dt=0 is taken
            # at full value, and a vote after fade_time is ignored
            value = values[i] * max(fade_time - dt, 0) / fade_time

            if values[i] > 0.:
                m_up += value
            else:
                m_down += value

        momentum_up.append(m_up)
        momentum_down.append(m_down)
    
    print momentum_up
    print momentum_down
    return m_times, momentum_up, momentum_down
