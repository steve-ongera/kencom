from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def detail_view(request):
    return render(request, 'detail.html')

def feature_view(request):
    return render(request, 'feature.html')

def price_view(request):
    return render(request, 'price.html')

def quote_view(request):
    return render(request, 'quote.html')

def service_view(request):
    return render(request, 'service.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')


def custom_bad_request(request, exception):
    return render(request, '400.html', status=400)

def custom_permission_denied(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
