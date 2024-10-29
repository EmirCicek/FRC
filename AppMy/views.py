from django.shortcuts import render
from AppMy.models import *
# Create your views here.

def indexPage(request):
    # Get is_live True cards and filter them by categoryName and just the last 3 of them


    ProjectCards = Card.objects.filter(category__categoryName="Projects",is_live=True).order_by('-id')[:3]
    SponsorCards = SponsorCard.objects.filter(is_live=True)
    GalleryCards = MediaCard.objects.filter(is_live=True).order_by('-id')[:4]
    
    context = {
        'Projects':ProjectCards,
        'Sponsors':SponsorCards,
        'Medias':GalleryCards
    }

    return render(request,"index.html",context)

def aboutUsPage(request):
    context = {}

    return render(request,"aboutUs.html",context)

def projectsPage(request):
    projects = Card.objects.filter(category__categoryName="Projects")
    
    context = {
        'projects':projects
    }

    
    return render(request,"projects.html",context)


def sponsorsPage(request):
    SponsorCards = SponsorCard.objects.filter(is_live=True)
    context = {
        'SponsorCards':SponsorCards

    }
    return render(request,"sponsor.html",context)

def contactPage(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = ContactMessages(first_name=first_name,last_name=last_name,email=email,phone=phone,message=message)
        contact.save()

    context = {

    }
    return render(request,"contact.html",context)

def resourcesPage(request):
    context = {

    }
    return render(request,"resources.html",context)

def galleryPage(request):

    medias = MediaCard.objects.filter(is_live=True)
    context = {

        'medias':medias

    }
    return render(request,"gallery.html",context)

def projectDetailPage(request,id):
    print(id)
    context = {

        'project':Card.objects.get(id=id)

    }
    return render(request,"project_details.html",context)


def blogDetails(request,id=0):
    blog_card = Card.objects.get(id=id)
    context = {
        'blog':blog_card,

    }

    return render(request,"blog_details.html",context)


def blogPage(request):
    blog_cards = Card.objects.filter(category__categoryName="Blogs")
    
    for card in blog_cards:
        print(card.title)

    context = {
        "blogs":blog_cards,
    }
    return render(request,"blog.html",context)
