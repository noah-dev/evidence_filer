from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import DocMetadata
import os


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

        with open(file_dest, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

        doc_id = doc_hlc + save_file_name
        # Could be refactored to use django forms
        new_doc = DocMetadata(  doc_id = doc_id,
                                doc_dept = doc_dept,
                                doc_year = doc_year,
                                doc_name = save_file_name,
                                hlc_cat = doc_hlc,
                                hlc_cmpt = "",
                                justification = "",
                                submitter = "blank@localhost.local")
        new_doc.save()
                
    return HttpResponseRedirect("/aaw/upload")