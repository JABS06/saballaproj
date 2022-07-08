from django.db import models

class Info(models.Model):
 	p_fname = models.CharField(max_length=100,null=True)
 	p_sname = models.CharField(max_length=100,null=True)
 	p_email = models.CharField(max_length=100,null=True)
 	p_purpose = models.CharField(max_length=100,null=True)
 	p_budget = models.IntegerField(null=True)

class Components(models.Model):

	procs = models.CharField(max_length=100,null=True)
	mobo = models.CharField(max_length=100,null=True)
	gpu = models.CharField(max_length=100,null=True)
	ram = models.CharField(max_length=100,null=True)
	psu = models.CharField(max_length=100,null=True)

class Feedback(models.Model):
	feedmes = models.TextField(null=True,blank=False)
	feedname = models.CharField(max_length=100,null=True)

# class Mybuild(models.Model):
# 	#user_info = models.ForeignKey(Info,null = True)
# 	comps = models.ManyToManyField(Components)
# 	bld_purpose = models.TextField(null=True,blank=False)
# 	bld_budget = models.DecimalField(decimal_places = 2, max_digits = 10)
# 	bld_total = models.DecimalField(decimal_places = 2, max_digits = 10)
# 	bld_date = models.DateTimeField(auto_now_add = True,null = True,blank = True)






# class BuildService(models.Model):
# 	user_info = models.ForeignKey(PersonalInformation,null = True)
# 	build_info = models.ForeignKey(Mybuild,null = True)
# 	mode_of_payment = (
# 		('Cash on Delivery','Cash on Delivery')
# 		('Online','Online')
# 		('Bank','Bank')
# 		)
# 	service_type = (
# 		('Build My Pc','Build My Pc')
# 		('Self PC Build','Self PC Build')
# 		)
# 	mop = models.CharField(max_length=200, null=True, choices = mode_of_payment)
# 	delivery_fee = models.DecimalField(decimal_places = 2, max_digits = 10)
# 	serv = models.CharField(max_length=200, null=True, choices = service_type)
# 	serv_fee = models.DecimalField(decimal_places = 2, max_digits = 10)
# 	order_total = models.DecimalField(decimal_places = 2, max_digits = 10)
# 	serv_date = models.DateTimeField(auto_now_add = True,null = True,blank = True)
# #5th

class Review(models.Model):
	message = models.TextField(null=True,blank=False)
	feedname = models.CharField(max_length=100,null=True)
 	