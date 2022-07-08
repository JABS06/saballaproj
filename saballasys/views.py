from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Info, Components, Feedback
import datetime

def Home(request):
	return render(request, 'index.html')

def Profilelist(request):
	infos = Info.objects.all()
	return render(request,'tableinfo.html' ,{'infos':infos})

def Createinfo(request):
	if request.method == 'POST':
		p_fname = request.POST['p_fname']
		p_sname = request.POST['p_sname']
		p_email = request.POST['p_email']
		p_purpose = request.POST['p_purpose']
		p_budget = request.POST['p_budget']
		info = Info (p_fname = p_fname, 
		p_sname = p_sname, p_email = p_email,
		p_purpose = p_purpose, p_budget = p_budget)

		info.save()

	else:
		return render(request, 'createinfo.html')
	infos = Info.objects.all()
	return render(request, 'tableinfo.html' ,{'infos':infos})

def Delinfo(request, id):
	# infolist = Info.objects.get(id=del_idi)
	infolist = Info.objects.filter(id=id)
	infolist.delete()
	return render(request, 'createinfo.html')

# def Editinfo(request, id):  
#     infos = Info.objects.get(id=id)  
#     return render(request,'updateinfo.html', {'object':object})  

# def Updateinfo(request, id):  
#     object = Info.objects.get(id=id)  
#     updinfo = updform(request.POST, instance = object)  
#     if updinfo.is_valid():  
#         updinfo.save() 
#         object = Info.objects.all() 
#         return redirect("createinfo.html") 

def Editinfo(request,id):
	infos = Info.objects.get(id=id) 
	informs = Info.objects.all() 
	return render(request,'updateinfo.html',{'infos':infos,'informs':informs,})

def Updateinfo(request,id):
	informs = Info.objects.get(id = id)	
	informs.p_fname = request.POST['p_fname']
	informs.p_sname = request.POST['p_sname']
	informs.p_email = request.POST['p_email']
	informs.p_purpose = request.POST['p_purpose']
	informs.p_budget = request.POST['p_budget']
	informs.save()
	return redirect("Createinfo")


def Howtobuild(request):
	return render(request, 'howtobuild.html')

def Tips(request):
	return render(request, 'tips.html')

def Builds(request):
	bilds = Components.objects.all()
	return render(request, 'builds.html' ,{'bilds':bilds})


def Mybuild(request):
	return render(request, 'mybuild.html')


def Componentlist(request):
	if request.method == 'POST':
		procs = request.POST['procs']
		mobo = request.POST['mobo']
		gpu = request.POST['gpu']
		ram = request.POST['ram']
		psu = request.POST['psu']
		comp = Components (procs = procs, 
		mobo = mobo, gpu = gpu,
		ram = ram, psu = psu)

		comp.save()

	else:
		return render(request, 'components.html')
	bilds = Components.objects.all()
	return render(request, 'builds.html' ,{'bilds':bilds})

def Delbuild(request,id):
	bildlist = Components.objects.get(id=id)
	bildlist.delete()
	return render(request, 'builds.html')

def Service(request, id):
	return render(request, 'service.html')

def Videos(request):
	return render(request, 'videos.html')

def About(request):
	return render(request, 'about.html')

def Contact(request):
	return render(request, 'contact.html')

def Feedbacks(request):
	if request.method == 'POST':
		feedname = request.POST['feedname']
		feedmes = request.POST['feedmes']
		feeds = Feedback (feedname = feedname, 
		feedmes = feedmes)

		feeds.save()

	else:
		return render(request, 'feedback.html')
	feedsb = Feedback.objects.all()
	return render(request, 'feedback.html' ,{'feedsb':feedsb})

def Feedbackdelete(request, id):
	feedlist = Feedback.objects.filter(id=id)
	feedlist.delete()
	return render(request, 'index.html')




		

