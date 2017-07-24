from django.views import generic
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Data
from . import plots
from .forms import FileFieldForm
from django.views.generic import View
import pandas as pd
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
import pandas
from django.http import JsonResponse
from django.core import serializers


your_media_root = settings.MEDIA_URL

class IndexView(generic.ListView):
    template_name = 'analyse/index.html'
    def get_queryset(self):
        print(self.request.user)
        return Data.objects.all().filter(uploader=self.request.user)


class DataDelete(DeleteView):
    model = Data
    success_url = reverse_lazy('analyse:index')
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DataDelete, self).get_object()
        if not obj.uploader == self.request.user:
            raise Http404
        return obj



    #model = Data
    #success_url = reverse_lazy('analyse:index')
    #print("ddd")
    #def get(self, request):
        #if model.uploader == request.user:
            #print("wew")
            #return CreateView.get(self, request)

#@login_required(login_url='/account/login')
def DataEdit(request, file_name = ""):
    print(1)


class DataCreate(CreateView):
    model = Data
    fields = ['table_name', 'album_logo', 'discription']
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.uploader = self.request.user
        obj.save()
        return super(DataCreate, self).form_valid(form)


def DataAnalyse(request, file_name = ""):
    gg = pd.read_csv(your_media_root+file_name, header=None, sep='\t',engine='python').as_matrix()
    if len(gg[0]) == 1:
        gg = pd.read_csv(your_media_root + file_name, header=None).as_matrix()
    head = list(i for i in gg[0])

    ggg = pd.read_csv(your_media_root + file_name, header=None)
    head2 = ggg
    #print(head2)
    tt = head2.to_json()

    return render(request, 'analyse/cal.html', {'data_list': gg, 'file_name' : file_name, "head": head, 'tt': tt})

def Graph(request, toggle = 0, file_name = ""):
    gg = pd.read_csv(your_media_root+file_name, header=None).as_matrix()
    ggg = pd.read_csv(your_media_root + file_name, header=None)
    head = list(i for i in gg[0])
    #print(len(ggg))
    head2 = ggg[0][:1]
    print(head2)
    tt = head2.to_json()
    return render(request, 'analyse/graph.html', {'data_list': gg, 'file_name': file_name, "head": head, 'tt': tt})