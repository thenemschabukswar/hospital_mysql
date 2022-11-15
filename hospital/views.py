from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .serializer import patient_serializer
from .serializer import hosp_serializer
# from .serializer import del_bed_serializer
from rest_framework import status
# Create your views here.
from .models import patient
from .models import hosp
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

def home(request):
    return HttpResponse("A very normal Home Page")

@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patient_info = patient.objects.all()
        serializer = patient_serializer(patient_info, many=True)
        return JsonResponse({'patients':serializer.data})
    elif request.method == 'POST':
        serializer = patient_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'PUT'])
def add_beds(request):
    if request.method == 'GET':
        rem = hosp.objects.all()
        serializer = hosp_serializer(rem, many=True)
        return JsonResponse({'beds':serializer.data})

    elif request.method == 'POST':
        # return HttpResponse(request.data)
        # tot = request['single'] + request['double']*2 + request['triple']*3
        hs = hosp_serializer(data=request.data)
        
        if hs.is_valid():
            x = hs.data
            cond1 = x['single'] < 0
            cond2 = x['double'] < 0
            cond3 = x['triple'] < 0
            if cond1 or cond2 or cond3:
                return HttpResponse("Values cannot be less than zero")
            hs.save()
            return JsonResponse(hs.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse("Bad request ", status=status.HTTP_400_BAD_REQUEST)

            # return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
    # '''
    # if request.method == 'POST':
    #     serializer = hosp_serializer(hosp, data=hosp.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         json = JSONRenderer().render(serializer.data)
    #         return JsonResponse(json)
    #     else:
    #         return HttpResponse("Bad req")
    # '''
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def rem_beds(request):
    if request.method == 'GET':
        rem = hosp.objects.all()
        serializer = hosp_serializer(rem, many=True)
        return JsonResponse({'beds':serializer.data})
    elif request.method == 'POST':
        serializer = hosp_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            x = serializer.data
            cond1 = x['single'] < 0
            cond2 = x['double'] < 0
            cond3 = x['triple'] < 0
            if cond1 or cond2 or cond3:
                return HttpResponse("Values cannot be less than zero")
            tot = x['single']
            tot += x['double']*2
            tot += x['triple']*3
            pats = patient.objects.count()
            if pats > tot:
                return HttpResponse('Cannot add Hospital, as number of rooms(' + str(tot) +') is less than total number of patients('+ str(pats)+')')
            return HttpResponse("Remaining beds: " + str(tot-pats))
        else:
            return HttpResponse("Bad req")

@api_view(['GET', 'DELETE'])
def del_bed(request,id):
    if request.method == 'GET':
        rem = hosp.objects.all()
        serializer = hosp_serializer(rem, many=True)
        return JsonResponse({'beds':serializer.data})
    elif request.method == 'DELETE':
        # serializer = del_bed_serializer(data=request.data)
        instance = hosp.objects.get(r_id=id)
        instance.delete()
        return HttpResponse("Success!")