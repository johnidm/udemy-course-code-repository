from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render


def index(request):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]
    return render(request, "challenges/index.html",
        {
            "months": months,
        }
    )


def monthly_by_id(request, month: int):
    month_list = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]

    if month > len(month_list):
        return HttpResponseNotFound("No month found")

    redirect_month = month_list[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly(request, month: str):
    return render(request, "challenges/challenge.html", 
        {   
            "month": month,
        }
    )
