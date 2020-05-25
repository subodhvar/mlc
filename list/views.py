from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import *
from django.utils import timezone
# Create your views here.
# def index(request):
#     #items=list.objects.filter(NAME__startswith="IMARAN",TEHSIL__startswith="TUNDLA")
#     items=list.objects.all()
#     context={
#         'items': items,
#     }
#     return render(request,'index.html',context)

def home(request):
    return render(request,'home.html')

def Agra_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Agra.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )
    if(items):
        context={
        'items': items,

                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Aligarh_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Aligarh.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )
    if(items):
        context={
           'items': items,
           'header':id,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Auraiya_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Auraiya.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Kasganj_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Kasganj.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Kannauj_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Kannauj.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Farrukhabad_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Farrukhabad.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Mathura_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Mathura.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Hathras_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Hathras.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Mainpuri_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Mainpuri.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Etah_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Etah.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def Etawah_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Etawah.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')


def Firozabad_d(request):
    id=request.GET.get('search')
    name=request.GET.get('tehsil')
    items=Firozabad.objects.filter(name_english__iexact=id,TEHSIL__startswith=name )

    if(items):
        context={
        'items': items,
                 }
        return render(request,'index.html',context)
    else:
        return HttpResponse('<h1 >Data Not found !!</h1><h2>Try again!!</h2>')

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST,)
        # form.Booth=item.Booth
        # form.section=item.section
        #
        # form.name_english=item.name_english
        if form.is_valid():
            data= form.cleaned_data.get("pk")
            form.save()
            return HttpResponse('<h4>Information Saved</h4>')
        else:
            return HttpResponse('<h4>Please Add Valid Data</h4>')
    else:
        form = cls(instance=item)
        return render(request, 'edit_item.html', {'form': form})

def edit_Aligarh(request,pk):
    return edit_item(request,pk,Aligarh,AligarhForm)
# def add(request):
#     if request.method="POST":
#         form=list(request.POST)
#
#         if foriexact():
#             form.save
#             return redirect('index')
#
#     else:
#         form=list()
#         return render(request,'add_mobile.html',{'form':form})
