from django.contrib import admin

from vote_app.models import Voter
from vote_app.models import Discussion
from vote_app.models import Vote

class VoterAdmin(admin.ModelAdmin):
	pass

class DiscussionAdmin(admin.ModelAdmin):
	pass

class VoteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Voter, VoterAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Vote, VoteAdmin)