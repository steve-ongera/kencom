from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('detail/', views.detail_view, name='detail'),
    path('feature/', views.feature_view, name='feature'),
    path('price/', views.price_view, name='price'),
    path('quote/', views.quote_view, name='quote'),
    path('service/', views.service_view, name='service'),
    path('team/', views.team_view, name='team'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
]
