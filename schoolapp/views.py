
from .models import Event, New,Prefect, Staff, SchoolGallery,UNEBPerformance
from .models import ExecutiveLeader
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

from .models import Application



# Create your views here.
def home(request):
    events = Event.objects.all()  # Adjust to the correct model
    news = New.objects.all()  # Adjust to the correct model
    return render(request, 'index.html', {'events': events, 'news': news})


def about(request):
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to the same page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def gallery(request):
    images = SchoolGallery.objects.all()
    return render(request, 'gallery.html', {'images': images})


def admission_process(request):
    return render(request, 'admission_process.html')

def requirements(request):
    return render(request, 'requirements.html')



def subjects(request):
    return render(request, 'subjects.html')

def academic_calendar(request):
    return render(request, 'academic_calendar.html')

def exams(request):
    return render(request, 'exams.html')

def news(request):
    return render(request, 'news.html')




def executive_leaders(request):
    executive_leaders = ExecutiveLeader.objects.all()
    return render(request, 'executive_leaders.html', {'executive_leaders': executive_leaders})



def prefects(request):
    prefects = Prefect.objects.all()
    return render(request, 'prefects.html', {'prefects': prefects})

def staff(request):
    staff = Staff.objects.filter(category='staff')
    non_staff = Staff.objects.filter(category='non_staff')
    return render(request, 'staff.html', {'staff': staff, 'non_staff': non_staff})
    



def lower_subjectives(request):
    subjects = [
        {"name": "English Language", "description": "Master the global language for effective communication.", "icon": "fas fa-language"},
        {"name": "Mathematics", "description": "Build problem-solving skills and numerical literacy.", "icon": "fas fa-square-root-alt"},
        {"name": "Physics", "description": "Explore the principles of matter and energy.", "icon": "fas fa-atom"},
        {"name": "Chemistry", "description": "Understand the composition of substances and their reactions.", "icon": "fas fa-flask"},
        {"name": "Biology", "description": "Study living organisms and their ecosystems.", "icon": "fas fa-dna"},
        {"name": "Geography", "description": "Discover the physical and human features of the Earth.", "icon": "fas fa-globe"},
        {"name": "History and Political Education", "description": "Learn about past events and political systems.", "icon": "fas fa-landmark"},
        {"name": "Physical Education", "description": "Promote physical fitness and healthy lifestyles.", "icon": "fas fa-running"},
        {"name": "CRE", "description": "Gain insight into Christian values and teachings.", "icon": "fas fa-cross"},
        {"name": "Kiswahili", "description": "Learn East Africa’s most widely spoken language.", "icon": "fas fa-comments"},
        {"name": "Entrepreneurship Education", "description": "Develop business and innovation skills.", "icon": "fas fa-lightbulb"},
        {"name": "Performing Arts", "description": "Nurture your creativity through drama, music, and dance.", "icon": "fas fa-theater-masks"},
        {"name": "German", "description": "Learn the language of Europe’s leading economy.", "icon": "fas fa-flag"},
        {"name": "Luganda", "description": "Master a rich and vibrant local language.", "icon": "fas fa-comment-alt"},
        {"name": "Literature in English", "description": "Dive into the world of poetry, prose, and drama.", "icon": "fas fa-book"},
        {"name": "Nutrition and Food Technology", "description": "Explore the science of food and healthy living.", "icon": "fas fa-utensils"},
        {"name": "Technology and Design", "description": "Learn to innovate with practical technology.", "icon": "fas fa-cogs"},
        {"name": "ICT", "description": "Master information technology and digital tools.", "icon": "fas fa-desktop"},
        {"name": "Art and Design", "description": "Unleash your artistic creativity and design skills.", "icon": "fas fa-paint-brush"}
    ]
    return render(request, "0_level_subjectives.html", {"subjects": subjects})


def higher_subjectives(request):
    subjects = [
    {"code": "S101", "name": "General Paper", "description": "Compulsory subject focusing on critical thinking.", "icon": "fas fa-book-open"},
    {"code": "S475", "name": "Subsidiary Maths", "description": "Mathematical concepts for higher learning.", "icon": "fas fa-calculator"},
    {"code": "S875", "name": "Subsidiary ICT", "description": "ICT skills for the digital age.", "icon": "fas fa-laptop-code"},
    {"code": "P210", "name": "History", "description": "Explore global and regional historical events.", "icon": "fas fa-landmark"},
    {"code": "P220", "name": "Economics", "description": "Study economic systems and principles.", "icon": "fas fa-chart-line"},
    {"code": "P230", "name": "Entrepreneurship", "description": "Learn the essentials of business creation.", "icon": "fas fa-lightbulb"},
    {"code": "P245", "name": "Christian Religious Education", "description": "Deepen your faith and knowledge of Christianity.", "icon": "fas fa-cross"},
    {"code": "P250", "name": "Geography", "description": "Understand the Earth's physical and human systems.", "icon": "fas fa-globe"},
    {"code": "P310", "name": "Literature in English", "description": "Dive into the world of prose, poetry, and drama.", "icon": "fas fa-feather-alt"},
    {"code": "P340", "name": "German", "description": "Learn Europe’s key language for cultural exchange.", "icon": "fas fa-language"},
    {"code": "P360", "name": "Luganda", "description": "Master the rich language of Buganda.", "icon": "fas fa-comment"},
    {"code": "P425", "name": "Mathematics", "description": "Develop advanced problem-solving skills.", "icon": "fas fa-square-root-alt"},
    {"code": "P510", "name": "Physics", "description": "Explore the science of matter and energy.", "icon": "fas fa-atom"},
    {"code": "P525", "name": "Chemistry", "description": "Understand chemical reactions and compounds.", "icon": "fas fa-flask"},
    {"code": "P530", "name": "Biology", "description": "Study living organisms and ecosystems.", "icon": "fas fa-dna"},
    {"code": "P615", "name": "Art and Design", "description": "Express creativity through visual arts.", "icon": "fas fa-palette"},
    {"code": "P620", "name": "Music", "description": "Learn music theory and performance.", "icon": "fas fa-music"},
    {"code": "P630", "name": "Clothing and Textiles", "description": "Master design and textile production.", "icon": "fas fa-tshirt"},
    {"code": "P640", "name": "Food and Nutrition", "description": "Discover the science of healthy living.", "icon": "fas fa-utensils"},
    {"code": "P710", "name": "Technical Drawing (Mechanical)", "description": "Learn the principles of mechanical design.", "icon": "fas fa-cogs"},
    {"code": "P720", "name": "Technical Drawing (Building)", "description": "Focus on architectural and structural design.", "icon": "fas fa-drafting-compass"},
]
    return render(request, 'A_level_subjectives.html', {"subjects": subjects})





def Uneb_performance(request):
    # Prefetch 'uce_performance' and 'uace_performance' (correct related names)
    performances = UNEBPerformance.objects.prefetch_related('uce_performance', 'uace_performance').all()
    return render(request, 'uneb_performance.html', {'performances': performances})




def events_and_news(request):
    events = Event.objects.order_by('date')[:5]  # Fetch latest 5 events
    news = New.objects.order_by('-created_at')[:5]  # Fetch latest 5 news
    return render(request, "events_and_news.html", {
        "events": events,
        "news": news,
    })



def apply_now(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        previous_school = request.POST.get("previous_school")
        intended_class = request.POST.get("intended_class")
        reason = request.POST.get("reason")

        Application.objects.create(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            email=email,
            phone=phone,
            previous_school=previous_school,
            intended_class=intended_class,
            reason=reason
        )

        messages.success(request, "Your application has been submitted successfully!")
        return redirect("apply_now")  # Change this to your actual page name

    return render(request, "apply_now.html")





