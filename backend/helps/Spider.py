import requests
from bs4 import BeautifulSoup
import random, time
from backend.helps.Tools import Tools
from django.db import connection

class SoupLearn:
    def getArticleList(self, page):
        if page == 1:
            req = requests.get("https://ptorch.com")
        else:
            req = requests.get("https://ptorch.com/?page=" + str(page))

        if req is not None:
            text = req.text
            soup = BeautifulSoup(text, 'lxml')
            uls = soup.find('div' , class_= 'main-content-left').ul
            for li in uls.find_all('li'):
                a_attrs = li.find('h5').find('a').attrs

                if 'href' in a_attrs:
                    self.saveArticleContent(a_attrs['href'])


        
    def saveArticleContent(self, href):
        cids = [7, 10, 11, 12]
        content = requests.get(href)
        if content is not None:
            content_text = content.text
            content_soup = BeautifulSoup(content_text, 'lxml')
            content_body = content_soup.find('div' , class_= 'main-content-article')
            title = content_body.h1.string
            content_img_attrs = content_body.img.attrs
            save_img = 0
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if 'src' in content_img_attrs:
                content_img_src = content_img_attrs['src']
                down_image = self.downloadPic(content_img_src, 'article')
                if down_image is not None:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO attachment (`created_at`, `updated_at`, `original_name`, `name`, `url`, `status`) Values(%s, %s, %s, %s, %s, %s)", 
                        [current_time, current_time, content_img_src, down_image['filename'], down_image['save_file'], 0])
                        lastSql = cursor.execute("SELECT last_insert_id()")
                        row = cursor.fetchone()
                        if len(row) > 0:
                            save_img = row[0]
                         
                
            content_detail = content_body.find('div' , class_= 'main-content-article-msg')
            
            cid_index = random.randint(0,3)
            if title is not None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO article (`created_at`, `updated_at`, `title`, `url`, `status`, `seo_title`, `seo_keywords`, `seo_description`, `click`, `sort`, `content`, `category_id`, `image_id`) " + 
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    [current_time, current_time, title, '', 0, title, title, title, 0, 0, content_detail, cids[cid_index], save_img])
                    print("save article:  {0}".format(title))


            
           
                
            
            
        
    
    def downloadPic(self, url, souptype):
        new_file_name = Tools.hash_filename(url)
        res_save_path = Tools.get_path(souptype)
        save_file = res_save_path + new_file_name
            
        r = requests.get(url)
        if r.status_code == 200:
            with open(save_file, 'wb') as f:
                f.write(r.content)
            return {'filename': new_file_name, 'save_file': save_file}
        return None
            

        
        
