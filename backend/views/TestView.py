import json
from django.http import HttpResponse
from django.shortcuts import render
from common.models.Attachment import Attachment
import os.path
import uuid
from django.views.generic.base import View


class TestView(View):
    resp = {'errorcode': 100, 'detail': 'Get success'}

    def get(self, request, *args, **kwargs):
        return render(request, 'test/test.html')

    def post(self, request, *args, **kwargs):
        upfile = request.FILES.get('image', None)
        print(upfile.name)
        print(upfile.size)
        new_file_name = self._hash_filename(upfile.name)
        print(new_file_name)
        with open(os.path.join('backend/static/') + new_file_name, 'wb') as f:
            for line in upfile.chunks():
                f.write(line)
            f.close()
        response = "You're looking at the results of question %s."
        return HttpResponse(response % upfile.name)

    def _hash_filename(self, filename):
        _, suffix = os.path.splitext(filename)
        return '%s%s' % (uuid.uuid4().hex, suffix)

    