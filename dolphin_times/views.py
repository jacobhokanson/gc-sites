from django.shortcuts import render, redirect
from django.http import HttpResponse
from dolphin_times.models import Dolphin, Vote
from dolphin_times.forms import DolphinVoteForm

# Create your views here.
def index(request):
    #create an iterable object of your dolphins to vote on from your database
    #return them to the front of your website
    dolphins = Dolphin.objects.all()
    form = DolphinVoteForm()

    dolphins_dictionary = {"dolphins":dolphins, "form":form}
    return render(request, 'dolphin_times/index.html', context=dolphins_dictionary)


def details(request):
    dolphins_dictionary = {'dolphin':{'name':'broken'}}
    #allow a user to vote on one dolphin
    #OR allow a write-in that creates a new dolphin record (if that name isn't your records),
    #as well as a vote for that dolphin
    #return a dictionary of information for ONLY ONE selected dolphin, with vote count, and other related data

    # ok
    if request.method == 'POST':
        post = DolphinVoteForm(request.POST)
        if post.is_valid():
            votedata = post.cleaned_data

            result = None
            if Dolphin.objects.filter(name=votedata['dolphin_name']).exists():
                result = Dolphin.objects.filter(name=votedata['dolphin_name'])[0]
            else:
                Dolphin.objects.create(name=votedata['dolphin_name'])
                result = Dolphin.objects.filter(name=votedata['dolphin_name'])[0]

            vote = Vote(recipient=result)
            vote.save()

            dolphins_dictionary = {'dolphin':{'name':result.name, 'info':result.info, 'votes':len(Vote.objects.filter(recipient=result))}}
            if votedata['voter_name']:
                dolphins_dictionary['voter'] = votedata['voter_name']

            return render(request, 'dolphin_times/details.html', context=dolphins_dictionary)
    elif request.method == 'GET':
        url_get = request.GET
        if 'id' in url_get:
            result = Dolphin.objects.filter(id=url_get['id'])[0]
            dolphins_dictionary = {'dolphin':{'name':result.name, 'info':result.info, 'votes':len(Vote.objects.filter(recipient=result))}}
            return render(request, 'dolphin_times/details.html', context=dolphins_dictionary)
        else:
            return redirect('/')
