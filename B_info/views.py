from django.forms.forms import Form
from django.shortcuts import render,redirect,get_object_or_404
from .models import Business
from .forms import BusinessForm
from django.views.generic import ListView,DetailView

# Create your views here.
from django.http import HttpResponse

class IndexView(ListView):
    model= Business
    template_name= "info/index.html"
    context_object_name= 'business_list'

    def get_queryset(self):
        return Business.objects.all()

    


class ContactDetailView(DetailView):
    model= Business
    template_name= "info/detail.html"
    context_object_name= 'detail1'

    


    



def create(request):
    if request.method=='POST':
        form= BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form= BusinessForm()

    return render(request,'info/create.html',{'form':form})


def edit(request,pk,template_name='info/edit.html'):
    busi= get_object_or_404(Business,pk=pk)
    form= BusinessForm(request.POST or None, instance=busi)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, template_name,{'form':form})

def delete(request, pk , template_name='info/confirm_delete.html'):
    busi= get_object_or_404(Business,pk=pk)
    if request.method=='POST':
        busi.delete()
        return redirect('index')

    return render(request, template_name, {'object':busi})


