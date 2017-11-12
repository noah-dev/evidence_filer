from django.db import models

class DocMetadata(models.Model):
    doc_id = models.TextField()
    doc_dept = models.TextField()
    doc_year = models.TextField()
    doc_name = models.TextField()
    hlc_cat = models.TextField()
    hlc_cmpt = models.TextField()
    justification = models.TextField()
    submitter = models.EmailField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.doc_id

    def __str__(self):
        return self.doc_id

    def to_dict(self):
        keys = [field.name for field in self._meta.fields + self._meta.many_to_many]
        model_dict = {}
        for key in keys:
            model_dict[key]=getattr(self, key)
        return model_dict