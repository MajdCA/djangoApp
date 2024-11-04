from django.shortcuts import get_object_or_404, render

from meetings_planner.models import Meeting

# Create your views here.
"""
def detail(request, id):
    meeting = get_object_or_404(Meeting,id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
"""
def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
def detail(request, id):
    meeting = get_object_or_404(Meeting,id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
