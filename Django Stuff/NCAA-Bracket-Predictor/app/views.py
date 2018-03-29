"""
Definition of views.
"""

from django.shortcuts import render
from app import generateBracket
from win32timezone import now
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
def home(request):
    listResults = generateBracket.get_tourney_results(2014, ['OPF'])
    listOrder = generateBracket.get_tourney_order(2014)
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'html/index.html',
        {
            'round1':listOrder,
            'roundOthers':listResults

        }
    )