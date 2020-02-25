from django.shortcuts import render

from minigame.models import Position
# from django.http import HttpResponse

def index(request):
	a=Position.objects.get()
	a.pos=0
	a.save()
	PageList={'first',
	'second',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'10',
	}
	print(a.pos)
	return render(request ,'minigame/list.html',{'PageList':PageList})

def page1(request):
	a=Position.objects.get()
	PageList={'first',
	'5',
	'6',
	'8',
	'10',}
	print(a.pos)
	return render(request ,'minigame/page.html',{'PageList':PageList})

def page2(request):
	a=Position.objects.get()
	a.pos+=1
	a.save()
	PageList={'second',
	'6',
	'9',
	'10',}
	print(a.pos)
	return render(request ,'minigame/page2.html',{'PageList':PageList})
def page2n(request):
	PageList={'second',
	'6',
	'9',
	'10',}
	a=Position.objects.get()
	print(a.pos)
	return render(request ,'minigame/page2.html',{'PageList':PageList})

def page3(request):
	a=Position.objects.get()
	a.pos+=2
	a.save()
	PageList={'3',
	'6',
	'7',
	'8',
	'9',
	'10',}
	print(a.pos)
	return render(request ,'minigame/page3.html',{'PageList':PageList})
def page3n(request):
	PageList={'3',
	'6',
	'7',
	'8',
	'9',
	'10',}
	a=Position.objects.get()
	print(a.pos)
	return render(request ,'minigame/page3.html',{'PageList':PageList})

def page4(request):
	a=Position.objects.get()
	a.pos+=3
	a.save()
	PageList={'4',
	'5',
	'7',
	'8',
	'9',
	'10',}
	print(a.pos)
	return render(request ,'minigame/page4.html',{'PageList':PageList})
def page4n(request):
	a=Position.objects.get()
	PageList={'4',
	'5',
	'7',
	'8',
	'9',
	'10',}
	print(a.pos)
	return render(request ,'minigame/page4.html',{'PageList':PageList})

def page5(request):
	a=Position.objects.get()
	a.pos+=4
	a.save()
	position=a.pos
	PageList=['first',
	'second',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'10',
	]
	Item=PageList[position-1]
	print(a.pos)
	return render(request ,'minigame/page5.html',{'PageList':PageList,'position':Item})
def page5n(request):
	a=Position.objects.get()
	position=a.pos
	PageList=['first',
	'second',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'10',
	]
	# Page_list=list(PageList)
	Item=PageList[position-1]
	return render(request ,'minigame/page5.html',{'PageList':PageList,'position':Item})
