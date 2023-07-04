from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    
    

class Pack(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    
class Gallery(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
   
    
class Serv(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Term(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    email  = models.EmailField(max_length=300)
    subject = models.TextField(max_length=300)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Contect(models.Model):
	name = models.CharField(max_length = 250)
	email = models.EmailField()
	phone = models.CharField(max_length = 10)
	mode_of_contact = models.CharField('Contact by', max_length=50)
	question_categories =models.CharField('How can we help you?', max_length=50)
	message = models.TextField(max_length = 3000)


	def __str__(self):
		return self.email
    
class About(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
 
 

class Reservation(models.Model):
    dest = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    sdate = models.DateField(max_length=50)
    fdate = models.DateField(max_length=50)
    gender = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    no_child = models.IntegerField()
    no_adults = models.IntegerField()


    def __str__(self):
        return self.fname
    

#services
class Lodge(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Maldive(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    
class Dubai(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Zanzibar(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Capetown(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class Fly(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Hotel(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Camp(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class Mountain(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Excursion(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Short(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Moon(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Shopping(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class Tsafari(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class Mara(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=50)
    cover = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
    
class Logo(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.title


#deep services
class KDHL001(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHL002(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHL003(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHL004(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHL005(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHL006(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL007(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL008(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL009(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL010(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL011(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHL012(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

#services +++ 

class KDHC001(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC002(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC003(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC004(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC005(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC006(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC007(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHC008(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class KDHC009(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

#services +++
class Day001(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Day002(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day003(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day004(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day005(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Day006(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day007(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day008(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day009(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day010(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day011(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day012(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day013(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day014(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Day015(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day016(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day017(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day018(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day019(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day020(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day021(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Day022(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

#services +++ tsafari
class KDHT001(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHT002(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class KDHT003(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class KDHT004(models.Model):
    title = models.CharField(max_length=50)
    links = models.CharField(max_length=50)

    def __str__(self):
        return self.title



#poster +++ 
class Poster001(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Poster002(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Poster003(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Poster004(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


#searchPackages
class SearchPackages(models.Model):
    title = models.CharField(max_length=50)
    dest = models.CharField(max_length=50)
    links= models.CharField(max_length=50)
    

    def __str__(self):
        return self.title