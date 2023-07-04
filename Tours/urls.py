"""Tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static 

urlpatterns = [
    path('', include('tours.urls')),
    path('packages/',include('tours.urls')),
    path('services/',include('tours.urls')),
    path('gallery/',include('tours.urls')),
    path('book/',include('tours.urls')),

    path('serv/',include('tours.urls')),
    path('reservation/',include('tours.urls')),
    path('terms/',include('tours.urls')),
    path('contact/',include('tours.urls')),
    path('contect/',include('tours.urls')),
    path('about/',include('tours.urls')),
    path('video/',include('tours.urls')),
    path('logo/',include('tours.urls')),
    

    #services
    path('services/lodge/',include('tours.urls')),
    path('services/maldive/',include('tours.urls')),
    path('services/dubai/',include('tours.urls')),
    path('services/zanzibar/',include('tours.urls')),
    path('services/capetown/',include('tours.urls')),
    path('services/fly/',include('tours.urls')),
    path('services/hotel/',include('tours.urls')),
    path('services/camp/',include('tours.urls')),
    path('services/mountain/',include('tours.urls')),
    path('services/excursion/',include('tours.urls')),
    path('services/short/',include('tours.urls')),
    path('services/shopping/',include('tours.urls')),
    path('services/mara/',include('tours.urls')),
    path('services/moon/',include('tours.urls')),
    path('services/tsafari/',include('tours.urls')),

    #services ++
    path('services/lodge/KDHL001',include('tours.urls')),
    path('services/lodge/KDHL002',include('tours.urls')),
    path('services/lodge/KDHL003',include('tours.urls')),
    path('services/lodge/KDHL004',include('tours.urls')),
    path('services/lodge/KDHL005',include('tours.urls')),
    path('services/lodge/KDHL006',include('tours.urls')),
    path('services/lodge/KDHL007',include('tours.urls')),
    path('services/lodge/KDHL008',include('tours.urls')),
    path('services/lodge/KDHL009',include('tours.urls')),
    path('services/lodge/KDHL010',include('tours.urls')),
    path('services/lodge/KDHL011',include('tours.urls')),
    path('services/lodge/KDHL012',include('tours.urls')),

    #services +++
    
    path('services/camp/KDHC001',include('tours.urls')),
    path('services/camp/KDHC002',include('tours.urls')),
    path('services/camp/KDHC003',include('tours.urls')),
    path('services/camp/KDHC004',include('tours.urls')),
    path('services/camp/KDHC005',include('tours.urls')),
    path('services/camp/KDHC006',include('tours.urls')),
    path('services/camp/KDHC007',include('tours.urls')),
    path('services/camp/KDHC008',include('tours.urls')),
    path('services/camp/KDHC009',include('tours.urls')),

    #services ++++
    path('services/excursion/Day021',include('tours.urls')),
    path('services/excursion/Day022',include('tours.urls')),
    path('services/excursion/Day019',include('tours.urls')),
    path('services/excursion/Day017',include('tours.urls')),
    path('services/excursion/Day016',include('tours.urls')),
    path('services/excursion/Day018',include('tours.urls')),
    path('services/excursion/Day003',include('tours.urls')),
    path('services/excursion/Day020',include('tours.urls')),


    #services +++ shorts
    path('services/short/Day001',include('tours.urls')),
    path('services/short/Day002',include('tours.urls')),
    path('services/short/Day004',include('tours.urls')),
    path('services/short/Day015',include('tours.urls')),

    #services +++ fly
    path('services/short/Day010',include('tours.urls')),
    path('services/short/Day011',include('tours.urls')),
    path('services/short/Day013',include('tours.urls')),
    path('services/short/Day008',include('tours.urls')),
    path('services/short/Day009',include('tours.urls')),
    path('services/short/Day005',include('tours.urls')),
    path('services/short/Day012',include('tours.urls')),
    path('services/short/Day014',include('tours.urls')),
    path('services/short/Day007',include('tours.urls')),
    path('services/short/Day006',include('tours.urls')),

    #services +++ tsafari
    path('services/tsafari/KDHT001',include('tours.urls')),
    path('services/tsafari/KDHT002',include('tours.urls')),
    path('services/tsafari/KDHT003',include('tours.urls')),
    path('services/tsafari/KDHT004',include('tours.urls')),

    #poster ++++
    path('services/maldive',include('tours.urls')),
    path('services/dubai',include('tours.urls')),
    path('services/zanzibar',include('tours.urls')),
    path('services/capetown',include('tours.urls')),

    #searchpackages
    path('', include('tours.urls')),


   
    path('admin/', admin.site.urls),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)