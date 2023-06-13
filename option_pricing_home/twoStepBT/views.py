from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import numpy as np
import math


# Create your views here.


def priceCalc(n, S0, sigma, r, T, K):
    time_var1 = sigma * (T / n) ** 0.5
    u = np.exp(time_var1)
    d = np.exp(time_var1 * -1)
    p = (np.exp(r * T / n) - d) / (u - d)
    C0 = 0  # Option price at the current moment.
    for i in range(n + 1):
        fact_term = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
        prob_term = (p ** i) * ((1 - p) ** (n - i))
        option_value = max(S0 * (u ** i) * (d ** (n - i)) - K, 0)
        discount_term = np.exp(- r * T)
        C0 += fact_term * prob_term * option_value * discount_term
    return C0


# def home(request):
#     return HttpResponse('''<h1>Option Pricing</h1><br>
#         <h3>Two step binomial option pricing model.</h3>''')


def home(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        # value = int(data.get('s0')) + int(data.get('sigma'))
        n = 2
        S0 = float(data.get('s0'))
        sigma = float(data.get('sigma'))
        r = float(data.get('r'))
        T = float(data.get('T'))
        K = float(data.get('K'))
        value = priceCalc(n, S0, sigma, r, T, K)
        print(value)
        p_value = value + K * np.exp(-r * T) - S0
        value = float("{:.2f}".format(value))
        p_value = float("{:.2f}".format(p_value))
        redirectURL = 'empty/' + str(value) + '/' + str(p_value) + '/' + str(S0) + '/' + str(sigma * 100) + '/' + str(r * 100) + '/' + str(T) + '/' + str(K) + '/'
        return redirect(redirectURL)
    return render(request, 'twoStep.html')


def empty(request, **kwargs):
    template = loader.get_template('Tworesult.html')
    p_value, value, S0, sigma, r, K, T = kwargs['p_value'], kwargs['value'], kwargs['S0'], kwargs['sigma'], kwargs['r'], kwargs[
        'K'], kwargs['T']
    # [value, n, S0, sigma, r, T, K] = kwargs.split('|')
    context = {'pVal': p_value, 'Val': value, 'S0': S0, 'sigma': sigma, 'r': r, 'T': T, 'K': K}
    return HttpResponse(template.render(context, request))
