from django.shortcuts import render


def handler404(request, exception):
    """
    Renders custom 404 page
    """
    return render(request, 'errors/404.html', status=404)