from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Startup, StartupRegister
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from django.contrib.auth.decorators import login_required


@csrf_exempt
def get_startups(request):
	startups = Startup.objects.all().values()
	scheme = urlsplit(request.build_absolute_uri(None)).scheme
	for startup in startups:
		startup['pic'] = scheme+'://'+request.META['HTTP_HOST']+'/'+str(startup['pic'])
	startups_list = list(startups)
	return JsonResponse({
		'success' : True,
		'startups': startups_list
		 },safe=False)

def post_startups(request):
	return render(request,'startup.html')

@csrf_exempt
def view_startup(request,id):
	try:
		 startup = Startup.objects.filter(id=id).first()
	except:
		return JsonResponse({
			'success':False,
			'message':'No Startup with such ID'
		})
	startup = model_to_dict(startup)
	startup['pic'] = str(startup['pic'])
	return JsonResponse({
		'success':True,
		'startup':startup
	})


@csrf_exempt
@login_required
def startupregister(request,id):
	user = request.user
	if user.profile.status == True:

		registered = StartupRegister.objects.filter(profile=user.profile)
		print(registered.count())
		count = registered.count()
		if(count<2):
			ctr = 0
			for i in registered:
				if(i.startup.id == id):
					ctr = ctr + 1
			if(ctr>0):
				return JsonResponse({
				'success':False,
				'message':'Already registered'
				
			})
			else:
				startup = Startup.objects.get(id=id)
				print(startup)
				startupregister = StartupRegister()
				startupregister.startup = startup
				profile = user.profile
				startupregister.profile = profile
				print(startupregister.startup)
				startupregister.save()
				return JsonResponse({
					'success':True,
					'message':'Registered successfully'
					
				})
		else:
			return JsonResponse({
				'success':False,
				'message':"You cannot register for more than two startups"
			})

	else:
		print("Verify your contact no")
		return JsonResponse({
			'success':False,
			'message':'Please verify your contact no'

			})

@login_required
def startupunregister(request,id):
	user = request.user
	registered = StartupRegister.objects.filter(profile=user.profile)
	count = registered.count()
	if(count==0):
		return JsonResponse({
			'success':False,
			'message':'Not registered for any startup'

			})
	else:
		ctr = 0
		for i in registered:
			if(i.startup.id == id):
				i.delete()
				ctr = ctr +1
			
				return JsonResponse({
				'success':True,
				'message':'Unregistered for the startup'

				})
		if(ctr==0):
			return JsonResponse({
				'success':False,
				'message':'Not registered for the startup'

				})


		return JsonResponse({
				'success':True,
				'message':'Unregistered for the startup'

				})
			

@csrf_exempt
@login_required
def userstartups(request):
	user = request.user
	registered = StartupRegister.objects.filter(profile=user.profile)
	Registered = {}
	Registered['success'] = True
	Registered['id'] = [i.startup.id for i in registered]
	Registered['startup'] = [i.startup.name for i in registered]
	return JsonResponse(Registered)



