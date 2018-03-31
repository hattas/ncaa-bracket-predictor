"""
Definition of views.
"""

from django.shortcuts import render
from app import generateBracket
from win32timezone import now
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
listResults = []
listIndicator = []
listOrder = []
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'html/index.html',
        {
        }
    )

def bracket(request):
    inp_value = request.GET.get('results', 'This is a default value')
    context = {'inp_value': inp_value}
    listResults = generateBracket.get_tourney_results(2015, [inp_value])
    listOrder = generateBracket.get_tourney_order(2015)
    return render(
        request,
        'html/bracket.html',
        {
            'round1':listOrder,
            'roundOthers':listResults

        }
    )


# def bracket(request):
#    listResults = generateBracket.get_tourney_results(2015, ['OPF'])
#    listOrder = generateBracket.get_tourney_order(2015)
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'html/bracket.html',
#        {
#            'round1':listOrder,
#            'roundOthers':listResults
#
#        }