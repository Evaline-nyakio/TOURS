from django import views
from django.urls import path
from .views import AboutPageView, BookPageView, CampPageView, CapetownPageView, ContactPageView, CreateContactView, CreateReservationView, Day001PageView, Day002PageView, Day003PageView, Day004PageView, Day005PageView, Day006PageView, Day007PageView, Day008PageView, Day009PageView, Day010PageView, Day011PageView, Day012PageView, Day013PageView, Day014PageView, Day015PageView, Day016PageView, Day017PageView, Day018PageView, Day019PageView, Day020PageView, Day021PageView, Day022PageView, DubaiPageView, ExcursionPageView, FlyPageView, HomePageView, HotelPageView, KDHC001PageView, KDHC002PageView, KDHC003PageView, KDHC004PageView, KDHC005PageView, KDHC006PageView, KDHC007PageView, KDHC008PageView, KDHC009PageView, KDHL001PageView, KDHL002PageView, KDHL003PageView, KDHL004PageView, KDHL005PageView, KDHL006PageView, KDHL007PageView, KDHL008PageView, KDHL009PageView, KDHL010PageView, KDHL011PageView, KDHL012PageView, KDHT001PageView, KDHT002PageView, KDHT003PageView, KDHT004PageView, LodgePageView, LogoPageView, MaldivePageView, MaraPageView, MoonPageView, MountainPageView,PackPageView, Poster001PageView, Poster002PageView, Poster003PageView, Poster004PageView, ReservationPageView, SearchPackagesPageView, ServPageView,GalleryPageView, ShoppingPageView, ShortPageView, TermPageView, TsafariPageView, VideoPageView, ZanzibarPageView, contect, search_packages
from .views import contactView

urlpatterns =[
    path("", HomePageView.as_view(), name="home"),
    path("packages/", PackPageView.as_view(), name="packages"),
    path("gallery/", GalleryPageView.as_view(), name="gallery"),
    path("book/", BookPageView.as_view(), name="book"),
    path("services/", ServPageView.as_view(), name="services"),
    path("serv/", ServPageView.as_view(), name="serv"),
    path("reservation/", ReservationPageView.as_view(), name="reservation"),
    path("terms/", TermPageView.as_view(), name="terms"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("video/", VideoPageView.as_view(), name="video"),
    path("logo/", LogoPageView.as_view(), name="logo"),
   
   #services
    path("services/lodge/", LodgePageView.as_view(), name="lodge"),
    path("services/maldive/", MaldivePageView.as_view(), name="maldives"),
    path("services/dubai/", DubaiPageView.as_view(), name="maldives"),
    path("services/zanzibar/", ZanzibarPageView.as_view(), name="zanzibar"),
    path("services/capetown/", CapetownPageView.as_view(), name="capetown"),
    path("services/fly/", FlyPageView.as_view(), name="fly"),
    path("services/hotel/", HotelPageView.as_view(), name="hotel"),
    path("services/camp/", CampPageView.as_view(), name="camp"),
    path("services/mountain/", MountainPageView.as_view(), name="mountain"),
    path("services/excursion/", ExcursionPageView.as_view(), name="excursion"),
    path("services/short/", ShortPageView.as_view(), name="short"),
    path("services/shopping/", ShoppingPageView.as_view(), name="shopping"),
    path("services/tsafari/", TsafariPageView.as_view(), name="tsafari"),
    path("services/mara/", MaraPageView.as_view(), name="mara"),
    path("services/moon/", MoonPageView.as_view(), name="moon"),
    

    #services ++
    path("services/lodge/KDHL001", KDHL001PageView.as_view(), name="KDHL001"),
    path("services/lodge/KDHL002", KDHL002PageView.as_view(), name="KDHL002"),
    path("services/lodge/KDHL003", KDHL003PageView.as_view(), name="KDHL003"),
    path("services/lodge/KDHL004", KDHL004PageView.as_view(), name="KDHL004"),
    path("services/lodge/KDHL005", KDHL005PageView.as_view(), name="KDHL005"),
    path("services/lodge/KDHL006", KDHL006PageView.as_view(), name="KDHL006"),
    path("services/lodge/KDHL007", KDHL007PageView.as_view(), name="KDHL007"),
    path("services/lodge/KDHL008", KDHL008PageView.as_view(), name="KDHL008"),
    path("services/lodge/KDHL009", KDHL009PageView.as_view(), name="KDHL009"),
    path("services/lodge/KDHL010", KDHL010PageView.as_view(), name="KDHL010"),
    path("services/lodge/KDHL011", KDHL011PageView.as_view(), name="KDHL011"),
    path("services/lodge/KDHL012", KDHL012PageView.as_view(), name="KDHL012"),
    
    #services +++
    path("services/camp/KDHC001", KDHC001PageView.as_view(), name="KDHC001"),
    path("services/camp/KDHC002", KDHC002PageView.as_view(), name="KDHC002"),
    path("services/camp/KDHC003", KDHC003PageView.as_view(), name="KDHC003"),
    path("services/camp/KDHC004", KDHC004PageView.as_view(), name="KDHC004"),
    path("services/camp/KDHC005", KDHC005PageView.as_view(), name="KDHC005"),
    path("services/camp/KDHC006", KDHC006PageView.as_view(), name="KDHC006"),
    path("services/camp/KDHC007", KDHC007PageView.as_view(), name="KDHC007"),
    path("services/camp/KDHC008", KDHC008PageView.as_view(), name="KDHC008"),
    path("services/camp/KDHC009", KDHC009PageView.as_view(), name="KDHC009"),
    
    #services ++++ Excursions
    path("services/excursion/Day021", Day021PageView.as_view(), name="Day021"),
    path("services/excursion/Day022", Day022PageView.as_view(), name="Day022"),
    path("services/excursion/Day019", Day019PageView.as_view(), name="Day019"),
    path("services/excursion/Day017", Day017PageView.as_view(), name="Day017"),
    path("services/excursion/Day016", Day016PageView.as_view(), name="Day016"),
    path("services/excursion/Day018", Day018PageView.as_view(), name="Day018"),
    path("services/excursion/Day003", Day003PageView.as_view(), name="Day003"),
    path("services/excursion/Day020", Day020PageView.as_view(), name="Day020"),
    
    #services ++++ shorts
    path("services/short/Day001", Day001PageView.as_view(), name="Day001"),
    path("services/short/Day002", Day002PageView.as_view(), name="Day002"),
    path("services/short/Day004", Day004PageView.as_view(), name="Day004"),
    path("services/short/Day015", Day015PageView.as_view(), name="Day015"),
    
    #services +++
    path("services/short/Day010", Day010PageView.as_view(), name="Day010"),
    path("services/short/Day011", Day011PageView.as_view(), name="Day011"),
    path("services/short/Day013", Day013PageView.as_view(), name="Day013"),
    path("services/short/Day008", Day008PageView.as_view(), name="Day008"),
    path("services/short/Day009", Day009PageView.as_view(), name="Day009"),
    path("services/short/Day005", Day005PageView.as_view(), name="Day005"),
    path("services/short/Day012", Day012PageView.as_view(), name="Day012"),
    path("services/short/Day014", Day014PageView.as_view(), name="Day014"),
    path("services/short/Day007", Day007PageView.as_view(), name="Day007"),
    path("services/short/Day006", Day006PageView.as_view(), name="Day006"),
   
    #tsafari +++
    path("services/tsafari/KDHT001", KDHT001PageView.as_view(), name="KDHT001"),
    path("services/tsafari/KDHT002", KDHT002PageView.as_view(), name="KDHT002"),
    path("services/tsafari/KDHT003", KDHT003PageView.as_view(), name="KDHT003"),
    path("services/tsafari/KDHT004", KDHT004PageView.as_view(), name="KDHT004"),
    
    #psoter ++++
    path("services/maldive", Poster001PageView.as_view(), name="maldive_poster"),
    path("services/dubai", Poster002PageView.as_view(), name="maldive_poster"),
    path("services/zanzibar", Poster003PageView.as_view(), name="maldive_poster"),
    path("services/capetown", Poster004PageView.as_view(), name="maldive_poster"),


    #search +++
    path("search/",search_packages, name="search_packages"),


    #forms
    path("reserve/",CreateReservationView.as_view(), name="add_post"),
    path("us/", contactView, name="add_contact"),
    path("contect/", contect, name="contect"),


]
