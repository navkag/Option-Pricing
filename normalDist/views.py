from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import numpy as np
from scipy.stats import norm
import math


# Create your views here.


def priceCalc(S0, sigma, r, T, K):
    _d1 = (np.log(S0 / K) + (r + (sigma ** 2) / 2) * T) / (sigma * (T ** 0.5))
    _d2 = (np.log(S0 / K) + (r - (sigma ** 2) / 2) * T) / (sigma * (T ** 0.5))
    u1 = norm.cdf(_d1)
    u2 = norm.cdf(_d2)
    exp_term = np.exp(-r * T)
    c = S0 * u1 - exp_term * K * u2
    return c


# def home(request):
#     return HttpResponse('''<h1>Option Pricing</h1><br>
#         <h3>Two step binomial option pricing model.</h3>''')


def home(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        # value = int(data.get('s0')) + int(data.get('sigma'))
        S0 = float(data.get('s0'))
        sigma = float(data.get('sigma'))
        r = float(data.get('r'))
        T = float(data.get('T'))
        K = float(data.get('K'))
        value = priceCalc(S0, sigma, r, T, K)
        print(value)
        value = float("{:.2f}".format(value))
        p_value = value + K * np.exp(-r * T) - S0
        p_value = float("{:.2f}".format(p_value))
        redirectURL = 'empty/' + str(value) + '/' + str(p_value) + '/' + str(S0) + '/' + str(sigma * 100) + '/' + str(r * 100) + '/' + str(T) + '/' + str(K) + '/'
        return redirect(redirectURL)
    return render(request, 'normalDist.html')


def empty(request, **kwargs):
    template = loader.get_template('Normalresult.html')
    p_value, value, S0, sigma, r, T, K = kwargs['p_value'], kwargs['value'], kwargs['S0'], kwargs['sigma'], kwargs['r'], kwargs[
        'T'], kwargs['K']
    # [value, n, S0, sigma, r, T, K] = kwargs.split('|')
    context = {'pVal': p_value, 'Val': value, 'S0': S0, 'sigma': sigma, 'r': r, 'T': T, 'K': K}
    return HttpResponse(template.render(context, request))
