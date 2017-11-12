from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.http import HttpResponse

from .models import DocMetadata

import os, json, datetime, collections

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_FOLDER = os.path.join(BASE_DIR, "files/")

# Create your views here.
def index(request):
    return HttpResponse("Hello")
def upload(request):
    if request.POST and request.FILES:
        # Get the text inputs
        doc_hlc = request.POST["hlc"]
        doc_dept = request.POST["deptname"]
        doc_year = request.POST["docyear"]
        doc_just = request.POST["justification"]
        doc_submitter = request.POST['submitter']

        # Get the file input
        file = request.FILES["uploadfile"]

        # Split up the file name from the extension
        name_ext_split_index = file.name.rfind('.')
        if name_ext_split_index != -1:
            file_name = file.name[0:name_ext_split_index]
            file_ext = file.name[name_ext_split_index:]
        else:
            # The file has no extension
            file_name = file.name
            file_ext = ""
        
        save_file_name = doc_dept + "_" + file_name + "_" + doc_year + file_ext
        file_dest = os.path.join(FILES_FOLDER, doc_hlc + "/" + save_file_name)

        with open(file_dest, 'wb+') as dst:
            for chunk in file.chunks():
                dst.write(chunk)

        doc_id = doc_hlc + "_" + save_file_name
        # Could be refactored to use django forms
        new_doc = DocMetadata(  doc_id = doc_id,
                                doc_dept = doc_dept,
                                doc_year = doc_year,
                                doc_name = save_file_name,
                                hlc_cat = doc_hlc,
                                hlc_cmpt = "_",
                                justification = "_",
                                submitter = "blank@localhost.local",
                                upload_time = 0)
        new_doc.save()
                
    return HttpResponseRedirect("/aaw/upload")
def retrival(request):
    hlc_category = "cr1"
    # docs = DocMetadata.objects.filter(hlc_cat=hlc_category).values()
    docs = DocMetadata.objects.values()
    return JsonResponse(list(docs), safe=False)

# https://stackoverflow.com/questions/36392510/django-download-a-file
from django.views.static import serve
from django.conf import settings
def serve_file(request):    
    try:
        hlc = request.GET['hlc']
        file_name = request.GET['file_name']
        hlc_file_name = hlc + "/" + file_name
    except:
        hlc_file_name = "cr1/CS_p_2016.pptx"
        
    file_path = os.path.join(FILES_FOLDER, hlc_file_name)

    with open(file_path, 'rb') as src:
        response = HttpResponse(src.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    raise Http404

#
def taxonomy(request):
    docs =  list(DocMetadata.objects.values())
    # by_year = list(docs.values('doc_year'))
    # by_dept = list(docs.values('doc_dept'))
    # by_hlc = list(docs.values('hlc_cat'))

    by_year, by_dept, by_hlc = {}, {}, {}

    # https://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
    for doc in docs:
        for key in doc:
            if key == "doc_year":
                year = doc[key]
                by_year[year] = by_year.get(year, 0) + 1
            if key == "doc_dept":
                dept = doc[key]
                by_dept[dept] = by_dept.get(dept, 0) + 1
            if key == "hlc_cat":
                hlc_cat = doc[key]
                by_hlc[hlc_cat] = by_hlc.get(hlc_cat, 0) + 1

    counts = {"by_year": by_year, "by_dept": by_dept, "by_hlc": by_hlc}
    
    return JsonResponse(counts, safe=False)