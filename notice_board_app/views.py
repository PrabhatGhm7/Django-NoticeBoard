from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Notice

def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notice_list.html', {'notices': notices})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notice_detail.html', {'notice': notice})


