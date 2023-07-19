from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def home(request):
#     return HttpResponse('''<h1>Option Pricing</h1><br>
#     <h3>Two step binomial option pricing model.</h3>
#     <h3>N step binomial option pricing model.</h3>
#     <h3>Black and Scholes model with approx. normal distribution.</h3>''')


def home(request):
    return render(request, 'home.html')
