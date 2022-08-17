from django.shortcuts import render

# Create your views here.
def mypagereview(request):
    return render(request,'mypage_review.html')