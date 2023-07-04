from django.http import BadHeaderError, HttpResponse
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from Tours import settings
from .forms import ContactForm, ContectForm



from .forms import ContactForm, ReservationForm
from .models import KDHC001, KDHC002, KDHC003, KDHC004, KDHC005, KDHC006, KDHC007, KDHC008, KDHC009, KDHL001, KDHL002, KDHL003, KDHL004, KDHL005, KDHL006, KDHL007, KDHL008, KDHL009, KDHL010, KDHL011, KDHL012, KDHT001, KDHT002, KDHT003, KDHT004, Camp, Capetown, Day001, Day002, Day003, Day004, Day005, Day006, Day007, Day008, Day009, Day010, Day011, Day012, Day013, Day014, Day015, Day016, Day017, Day018, Day019, Day020, Day021, Day022, Dubai, Excursion, Fly, Hotel, Lodge, Logo, Maldive, Mara, Moon, Mountain, Poster001, Poster002, Poster003, Poster004, Reservation, SearchPackages, Shopping, Short, Tour, Tsafari, Video, Zanzibar
from .models import Pack
from .models import Serv
from .models import Gallery
from .models import Book
from .models import  Term
from .models import  About
from .models import  Contact

from django.shortcuts import redirect, render
from .models import Pack
from .forms import PackSearchForm


#forms
class CreateReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation_form.html"
    success_url = reverse_lazy("home")

class CreateContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contactus.html"
    success_url = reverse_lazy("home")

class HomePageView(ListView):
    model = Tour
    template_name = "index.html"

class PackPageView(ListView):
    model = Pack
    template_name = "packages.html"

class ServPageView(ListView):
    model = Serv
    template_name = "services.html"


class BookPageView(ListView):
    model = Book
    template_name = "book.html"


class GalleryPageView(ListView):
    model = Gallery
    template_name = "gallery.html"

class ReservationPageView(ListView):
    model = Reservation
    template_name = "reservations.html"

class AboutPageView(ListView):
    model = About
    template_name = "about.html"
class ContactPageView(ListView):
    model = Contact
    template_name = "contact.html"

class TermPageView(ListView):
    model = Term
    template_name = "terms.html"



#services
class LodgePageView(ListView):
    model = Lodge
    template_name = "lodge.html"

class MaldivePageView(ListView):
    model = Maldive
    template_name = "maldive.html"
class DubaiPageView(ListView):
    model = Dubai
    template_name = "dubai.html"
class ZanzibarPageView(ListView):
    model = Zanzibar
    template_name = "zanzibar.html"
class CapetownPageView(ListView):
    model = Capetown
    template_name = "capetown.html"
class FlyPageView(ListView):
    model = Fly
    template_name = "fly.html"

class HotelPageView(ListView):
    model = Hotel
    template_name = "hotel.html"

class CampPageView(ListView):
    model = Camp
    template_name = "camp.html"

class MountainPageView(ListView):
    model = Mountain
    template_name = "mountain.html"

class ExcursionPageView(ListView):
    model = Excursion
    template_name = "excursion.html"

class ShortPageView(ListView):
    model = Short
    template_name = "short.html"

class ShoppingPageView(ListView):
    model = Shopping
    template_name = "shopping.html"

class MaraPageView(ListView):
    model = Mara
    template_name = "mara.html"

class TsafariPageView(ListView):
    model = Tsafari
    template_name = "tsafari.html"

class MoonPageView(ListView):
    model = Moon
    template_name = "moon.html"

class VideoPageView(ListView):
    model = Video
    template_name = "index.html"

class LogoPageView(ListView):
    model = Logo
    template_name = "nav.html"

#services ++
class KDHL001PageView(ListView):
    model = KDHL001
    template_name = "KDHL001.html"

class KDHL002PageView(ListView):
    model = KDHL002
    template_name = "KDHL002.html"

class KDHL003PageView(ListView):
    model = KDHL003
    template_name = "KDHL003.html"

class KDHL004PageView(ListView):
    model = KDHL004
    template_name = "KDHL004.html"


class KDHL005PageView(ListView):
    model = KDHL005
    template_name = "KDHL005.html"

class KDHL006PageView(ListView):
    model = KDHL006
    template_name = "KDHL006.html"

class KDHL007PageView(ListView):
    model = KDHL007
    template_name = "KDHL007.html"

class KDHL008PageView(ListView):
    model = KDHL008
    template_name = "KDHL008.html"

class KDHL009PageView(ListView):
    model = KDHL009
    template_name = "KDHL009.html"

class KDHL010PageView(ListView):
    model = KDHL010
    template_name = "KDHL010.html"

class KDHL011PageView(ListView):
    model = KDHL011
    template_name = "KDHL011.html"

class KDHL012PageView(ListView):
    model = KDHL012 
    template_name = "KDHL012.html"


#services +++

class KDHC001PageView(ListView):
    model = KDHC001
    template_name = "KDHC001.html"

class KDHC002PageView(ListView):
    model = KDHC002
    template_name = "KDHC002.html"

class KDHC003PageView(ListView):
    model = KDHC003
    template_name = "KDHC003.html"

class KDHC004PageView(ListView):
    model = KDHC004
    template_name = "KDHC004.html"

class KDHC005PageView(ListView):
    model = KDHC005
    template_name = "KDHC005.html"

class KDHC006PageView(ListView):
    model = KDHC006
    template_name = "KDHC006.html"

class KDHC007PageView(ListView):
    model = KDHC007
    template_name = "KDHC007.html"

class KDHC008PageView(ListView):
    model = KDHC008
    template_name = "KDHC008.html"

class KDHC009PageView(ListView):
    model = KDHC009
    template_name = "KDHC009.html"

#services ++

class Day001PageView(ListView):
    model = Day001
    template_name = "Day001.html"

class Day002PageView(ListView):
    model = Day002
    template_name = "Day002.html"

class Day003PageView(ListView):
    model = Day003
    template_name = "Day003.html"

class Day004PageView(ListView):
    model = Day004
    template_name = "Day004.html"

class Day005PageView(ListView):
    model = Day005
    template_name = "Day005.html"

class Day006PageView(ListView):
    model = Day006
    template_name = "Day006.html"

class Day007PageView(ListView):
    model = Day007
    template_name = "Day007.html"

class Day008PageView(ListView):
    model = Day008
    template_name = "Day008.html"

class Day009PageView(ListView):
    model = Day009
    template_name = "Day009.html"

class Day010PageView(ListView):
    model = Day010
    template_name = "Day010.html"

class Day011PageView(ListView):
    model = Day011
    template_name = "Day011.html"

class Day012PageView(ListView):
    model = Day012
    template_name = "Day012.html"

class Day013PageView(ListView):
    model = Day013
    template_name = "Day013.html"

class Day014PageView(ListView):
    model = Day014
    template_name = "Day014.html"

class Day015PageView(ListView):
    model = Day015
    template_name = "Day015.html"

class Day016PageView(ListView):
    model = Day016
    template_name = "Day016.html"

class Day017PageView(ListView):
    model = Day017
    template_name = "Day017.html"

class Day018PageView(ListView):
    model = Day018
    template_name = "Day018.html"

class Day019PageView(ListView):
    model = Day019
    template_name = "Day019.html"


class Day020PageView(ListView):
    model = Day020
    template_name = "Day020.html"

class Day021PageView(ListView):
    model = Day021
    template_name = "Day021.html"

class Day022PageView(ListView):
    model = Day022
    template_name = "Day022.html"

#services +++ tsafari

class KDHT001PageView(ListView):
    model = KDHT001
    template_name = "KDHT001.html"

class KDHT002PageView(ListView):
    model = KDHT002
    template_name = "KDHT002.html"

class KDHT003PageView(ListView):
    model = KDHT003
    template_name = "KDHT003.html"

class KDHT004PageView(ListView):
    model = KDHT004
    template_name = "KDHT004.html"

#posters ++++ 
class Poster001PageView(ListView):
    model = Poster001
    template_name = "maldive.html"

class Poster002PageView(ListView):
    model = Poster002
    template_name = "maldive.html"

class Poster003PageView(ListView):
    model = Poster003
    template_name = "maldive.html"

class Poster004PageView(ListView):
    model = Poster004
    template_name = "maldive.html"


#search_packages

class SearchPackagesPageView(ListView):
    model = SearchPackages
    template_name = "search_packages.html"    

def search_packages(request):
    if request.method == 'GET':
        form = PackSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Pack.objects.filter(name__icontains=query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = PackSearchForm()
    return render(request, 'search_form.html', {'form': form})


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            
            contact=form.save()

            print(f"NEW CONTACT::: {contact}")

            try:
                send_mail(subject,email,message, ["kennkanja@gmail.com"])
                
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contactus.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

def contect(request):
    if request.method == 'POST':
        form = ContectForm(request.POST)
        if form.is_valid(): 
            form.save()
            subject = "Welcome to Kenya Dream Holidays"
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list])
            return render(request, 'success.html') 
    form = ContectForm()
    context = {'form': form} 
    return render(request, 'contect.html', context)
