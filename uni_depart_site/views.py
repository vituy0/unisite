from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from uni_depart_site.models import UniInfo
from uni_depart_site.forms import * 
from django.urls import resolve
from urllib.parse import urlparse
import re
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator, PageNotAnInteger
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


class Search(FormView):
    form_class = SearchForm
    template_name = 'uni_depart_site/search.html'
    # queryst = ""
    # def dictToQueryset(self, **queryset):
    #     try:
    #         local_result = queryset['search_result']
    #         self.queryst = local_result
    #         return local_result
    #     except KeyError:
    #         return self.queryst    
        
    def form_valid(self, form):
        search_result = form.cleaned_data['search_keyword']
        result_list = UniInfo.objects.filter(Q(university__icontains=search_result)).values('university', 'uni_code').distinct()
        
        context = {}
        #context['test'] = result_list.__dict__
        # search_dict = {'search_result' : search_result}
        # self.dictToQueryset(**search_dict)
        # context = self.get_context_data(**search_dict)

        context['search_word'] = search_result
        context['object_list'] = result_list
        print("---------", context, "-----------")
        return render(self.request, self.template_name, context)    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     result_list = UniInfo.objects.all()
    

    #     paginator = Paginator(result_list, 3) 
    #     page = self.request.GET.get('page')  
    #     try:
    #         result_list = paginator.page(page)
    #     except PageNotAnInteger:
    #         result_list = paginator.page(1)
        
    #     context['object_list'] = result_list
    #     return context
    

    
class TestList(ListView):
    model = UniInfo
    template_name = 'uni_depart_site/list_all.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unidata = UniInfo.objects.all() 
        uniname = UniInfo.objects.values('university', 'uni_code').distinct() # 중복 거르기 
        context['data'] = unidata
        context["university"] = uniname
        #print(uniname)
        return context
    
    # def data(request):
    #     university_name = UniInfo.objects()
    #     unidata = UniInfo.objects.filter(university__icontains='가천대학교')
    #     context = {}
    #     context['university'] = unidata
    #     return render(request, 'uni_depart_site/list_all.html', context)

class UniInfoView(ListView):
    model = UniInfo
    template_name = 'uni_depart_site/step2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        current_url = self.request.path
#        getcode = urlparse(current_url)
        current_code = int(re.findall('\d', current_url)[0])
        data = UniInfo.objects.filter(uni_code=current_code)
        context['data'] = data
        print("url = ", current_url)
        return context

    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     info = UniInfo.objects.filter(uni_code=a)
    #     context[""] = 
    #     return context
    
class DepartDetail(DetailView):
    model = UniInfo
    template_name = 'uni_depart_site/depart_detail.html'
