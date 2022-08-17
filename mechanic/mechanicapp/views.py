from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'test.html')

def worker(request):
    return render(request,'worker.html')

def worker_review(request):
    return render(request,'worker_review.html')