from django.shortcuts import render


def error_badrequest(request, exception):
    return render(request, "errors/default.html", {})


def error_forbidden(request, exception):
    return render(request, "errors/default.html", {})


def error_notfound(request, exception):
    return render(request, "errors/default.html", {})


def error_servererror(request):
    return render(request, "errors/default.html", {})
