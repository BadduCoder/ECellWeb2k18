from django.http import JsonResponse, Http404,HttpResponse
from server.decorators.login import login_req
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Speaker
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config
import json
import xlsxwriter
import os
from django.conf import settings

@csrf_exempt
def get_speakers(request):
	response = {}
	if Speaker.objects.filter(flag=True).exists():
		speakers = Speaker.objects.all().values()
		scheme = urlsplit(request.build_absolute_uri(None)).scheme
		for speaker in speakers:
			speaker['profile_pic'] = config('HOST')+str(speaker['profile_pic'])
		speakers_list = list(speakers)
		response['success'] = True
		speakers_list = sorted(speakers_list, key=lambda i:i['year'], reverse=True)
		response['speakers'] = speakers_list
	else:
		response['success'] = False
		response['message'] = "Coming Soon"
	return JsonResponse(response)


def post_speakers(request):
	return render(request,'website/speakers.html')

@csrf_exempt
def view_speaker(request,id):
	speaker = Speaker.objects.filter(id = id).first()
	speaker = model_to_dict(speaker)
	speaker['profile_pic'] = str(speaker['profile_pic'])

	return JsonResponse({
		'success':True,
		'speaker':speaker
	})

@csrf_exempt
def add_speakers(request):
	response = {}
	response['success'] = False
	if request.method=='POST':
		req_data = json.loads(request.body)
		email = req_data['email']
		name = req_data['name']
		contact_no = req_data['contact_no']
		remarks = req_data['remarks']
		company = req_data['company']
		designation = req_data['designation']
		user = request.user
		if request.user.is_anonymous==False:
			profile = user.profile
			if profile.user_type in ["EXE","MNG","HC","OC"]:
				try:
					speaker = Speaker()
					speaker.name = name
					speaker.email = email
					speaker.contact = contact_no
					speaker.description = remarks
					speaker.company = company
					speaker.designation = designation
					speaker.save()
				except:
					print('erroer')
					response['success'] = False
					response['message'] = 'Speaker already exists.'
				else:
					print('saving')
					speaker.save()
					response['success']=True
					response['message']= 'Speaker added successfully'
			else:
				response['message'] = 'You are not authorized to add speaker.'
				print('not authorized')
		else:
			response['message'] = 'This action requires you to sign in..'
			print('not authorized')
	else:
		response['success'] = False
		response['message'] = 'Form method error'
	return JsonResponse(response)

	
def new_speaker(request):
	return render(request,'website/add_speakers.html')

def retrieve_speakers(request):
	user = request.user
	response = {}
	if user.is_superuser:	
		speakers = Speaker.objects.all()
		workbook = xlsxwriter.Workbook('Speakers.xlsx') 
		worksheet = workbook.add_worksheet() 
		worksheet.write('A1', 'Name') 
		worksheet.write('B1', 'Email') 
		worksheet.write('C1', 'Contact No') 
		worksheet.write('D1', 'Comapany Name') 
		worksheet.write('E1', 'Designation') 
		worksheet.write('F1', 'Remarks') 
		row = 1
		column =0
		for s in speakers:
			worksheet.write(row,column, s.name)
			column+=1
			worksheet.write(row,column,s.email)
			column+=1
			worksheet.write(row,column,s.contact)
			column+=1
			worksheet.write(row,column,s.company)
			column+=1
			worksheet.write(row,column,s.designation)
			column+=1
			worksheet.write(row,column,s.description)
			row+=1
			column=0
		workbook.close()
		response['success']=True
		response['message']= 'Speaker retrieved successfully'

		file_path = os.path.join(settings.BASE_DIR, 'Speakers.xlsx')
		if os.path.exists(file_path):
			with open(file_path, 'rb') as fh:
				response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
				response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
				return response
		raise Http404
	else:
		response['success'] = False
		response['message']= 'You are not authorized to access this data'
	return JsonResponse(response)
