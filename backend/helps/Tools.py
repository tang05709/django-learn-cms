import time, uuid, os.path

class Tools:
    ''''重命名文件'''
    @staticmethod
    def hash_filename(filename):
        _, suffix = os.path.splitext(filename)
        return '%s%s' % (uuid.uuid4().hex, suffix)


    ''''文件保存路径'''
    @staticmethod
    def get_path(updir):
        if(updir == ''):
            path = 'uploads/' + time.strftime("%Y%m%d", time.localtime()) + '/'
        else:
            path = 'uploads/' + updir + '/' + time.strftime("%Y%m%d", time.localtime()) + '/'

        save_path = os.path.join(path)
        isExists = os.path.exists(save_path)
        if not isExists:
            os.makedirs(save_path) 
        
        return save_path
