import json, time, uuid, os.path
from django.http import HttpResponse
from django.views.generic.base import View
from common.models.Attachment import Attachment


class UploadFileView(View):
    

    def post(self, request, *args, **kwargs):
        resp = {'errno': 100, 'data': '请选择图片'}
        #upfile = request.FILES.get('image', None)
        upfiles = request.FILES.getlist('image', None)
        updir = request.POST.get('updir', 'common')

        if(upfiles == None):
            return HttpResponse(json.dumps(resp), content_type="application/json")
        
        resUrls = []
        resIds = []
        for up in upfiles:
            upfileres = self._upload(up, updir)
            resUrls.append(upfileres['url'])
            resIds.append(upfileres['id'])

        #前端使用的plopload上传，一次上传一张，多张分多次上传, 使用的wangeditor，是多张图片是一次上传的
        if updir == 'detail':
            resp = {'errno': 0, 'data': resUrls}
        else:
            resp = {'errno': 200, 'id': resIds[0], 'url': resUrls[0]}
 

        return HttpResponse(json.dumps(resp), content_type="application/json")

    def _upload(self, upfile, updir):
        new_file_name = self._hash_filename(upfile.name)
        res_save_path = self._get_path(updir)
        save_path = res_save_path['save_path']
        local_save_path = res_save_path['local_save_path']
        local_save_file = local_save_path + new_file_name
        save_file = save_path + new_file_name
        url = 'http://127.0.0.1:8000/' + save_file
        
        with open(local_save_file, 'wb') as f:
            for line in upfile.chunks():
                f.write(line)
            f.close()
        
        model = Attachment()
        model.original_name = upfile.name
        model.name = new_file_name
        model.url = save_file
        model.status = 0
        model.save()
        return {'id': model.id, 'url': url}

    def _hash_filename(self, filename):
        _, suffix = os.path.splitext(filename)
        return '%s%s' % (uuid.uuid4().hex, suffix)

    def _get_path(self, updir):
        if(updir == ''):
            path = 'images/' + time.strftime("%Y%m%d", time.localtime()) + '/'
        else:
            path = 'images/' + updir + '/' + time.strftime("%Y%m%d", time.localtime()) + '/'
        # 本地储存路径
        local_save_path = os.path.join('frontend/static', path) 
        # 数据库存储路径
        save_path = os.path.join(path)
        isExists = os.path.exists(local_save_path)
        if not isExists:
            os.makedirs(local_save_path) 
        
        return {'save_path': save_path, 'local_save_path': local_save_path}


    