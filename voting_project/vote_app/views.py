from django.template.response import TemplateResponse

from vote_app.models import Voter, Discussion, Vote

# Create your views here.

def home(request):

    all_votes = Vote.objects.all()
    print all_votes
    return TemplateResponse(request, 'home.html', {'all_votes':all_votes})
