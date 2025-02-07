from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admission-process/', admission_process, name='admission_process'),
    path('requirements/', requirements, name='requirements'),
    path('apply-now/', apply_now, name='apply_now'),
    path('subjects/', subjects, name='subjects'),
    path('academic-calendar/', academic_calendar, name='academic_calendar'),
    path('exams/', exams, name='exams'),
    path('news/', news, name='news'),
    
    path('executive-leaders/', executive_leaders, name='executive_leaders'),
    path('prefects/', prefects, name='prefects'),
    path('staff/', staff, name='staff'),
    path('lower_subjectives', lower_subjectives, name='lower_subjectives'),
    path('higher_subjectives/', higher_subjectives, name='higher_subjectives'),
    path('Uneb_performance/', Uneb_performance, name='Uneb_performance'),
    path('events_and_news/', events_and_news, name='events_and_news'),
     path('gallery/', gallery, name='gallery'),
    
]
