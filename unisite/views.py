from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from uni_depart_site.models import UniInfo
from django.views.generic.edit import BaseDeleteView, BaseCreateView
import json
from django.http import JsonResponse, HttpResponse

class SiteMain(ListView):
    model = UniInfo
    template_name = 'mainview_v3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        uni_name = UniInfo.objects.values('university', 'uni_code', 'province').distinct()
        uni_depart = UniInfo.objects.values('id', 'uni_code', 'department', 'university')
        uni_standard = UniInfo.objects.values('standard_max_field', 'standard_mid_field').distinct()
        uni_standard_min = UniInfo.objects.values('standard_min_field', 'standard_mid_field').distinct()
        max_min = UniInfo.objects.values('standard_max_field', 'standard_min_field').distinct()
        uni_standard_max = UniInfo.objects.values('standard_max_field').distinct()
        context["university"] = uni_name
        context["depart"] = uni_depart
        context["standard"] = uni_standard
        context["standard_min"] = uni_standard_min
        context["standard_max"] = uni_standard_max
        context["standard_max_min"] = max_min
        #print(max_min)
        return context
        
class MainDepartStatus(ListView):  
    model = UniInfo
    template_name = 'mainview_v4.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uni_name = UniInfo.objects.values('university', 'uni_code', 'province').distinct()
        uni_depart = UniInfo.objects.values('id', 'uni_code', 'department', 'university', 'standard_min_field')
        uni_standard = UniInfo.objects.values('standard_max_field', 'standard_mid_field').distinct()
        all_standard = UniInfo.objects.values('standard_max_field', 'standard_mid_field', 'standard_min_field').distinct()
        #uni_standard_min = UniInfo.objects.values('standard_min_field', 'standard_mid_field').distinct()
        max_min = UniInfo.objects.values('standard_max_field', 'standard_min_field').distinct()
        uni_standard_max = UniInfo.objects.values('standard_max_field').distinct()
        uni_standard_min = UniInfo.objects.values('standard_min_field').distinct()
        province_list = UniInfo.objects.values('province').distinct()
        context["university"] = uni_name
        context["depart"] = uni_depart
        context["all_standard"] = all_standard
        context["standard"] = uni_standard
        #context["standard_min"] = uni_standard_min
        context["standard_max"] = uni_standard_max
        context["standard_max_min"] = max_min
        context["standard_min"] = uni_standard_min
        context["province_list"] = province_list
        #print(max_min)
        return context
        # university = UniInfo.objects.all().distinct()
        # depart_status = UniInfo.objects.values('department', 'university', 'depart_state', 'standard_min_field', 'uni_year').distinct()
        # standard = UniInfo.objects.values('standard_max_field', 'standard_mid_field', 'standard_min_field').distinct()
        
        # context["university"] = university
        # context["depart_status"] = depart_status
        # context["standard"] = standard
        # return context    



class Button_Event(BaseCreateView):
    model = UniInfo
    
    def get(self, request, *args, **kwars):
        #print(request.GET['min'])
        print(request.GET['pro'])
        getid = request.GET['min']
        getpro = request.GET['pro']
        if request.GET['min'] == "":
            dict_data = None
            print("222222")
        elif request.GET['pro'] == "" or request.GET['pro'] == "전체":
            dict_data = list(UniInfo.objects.filter(standard_min_field__icontains=getid).values('university', 'department', 'province').distinct())

        else:
            dict_data = list(UniInfo.objects.filter(standard_min_field__icontains=getid, province__icontains=getpro).values('university', 'department', 'province').distinct())
        #print(dict_data)
        return JsonResponse(data=dict_data, safe=False)

    
   
class Tableau(TemplateView):
    template_name="tableau.html"
