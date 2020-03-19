import requests
from bs4 import BeautifulSoup
import random
from backend.helps.Tools import Tools
from common.models.Article import Article
from common.models.Attachment import Attachment

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
            if 'src' in content_img_attrs:
                content_img_src = content_img_attrs['src']
                down_image = self.downloadPic(content_img_src, 'article')
                if down_image is not None:
                    attachment_model = Attachment()
                    attachment_model.original_name = content_img_src
                    attachment_model.name = down_image['filename']
                    attachment_model.url = down_image['save_file']
                    attachment_model.status = 0
                    attachment_model.save()
                    save_img = attachment_model.id 
                         
                
            content_detail = content_body.find('div' , class_= 'main-content-article-msg')
            
            article_model = Article()
            cid_index = random.randint(0,3)
            article_model.category_id = cids[cid_index]
            article_model.title = title
            article_model.url = ''
            article_model.status = 0
            article_model.seo_title = title
            article_model.seo_keywords = title
            article_model.seo_description = title
            article_model.click = 0
            article_model.sort = 0
            article_model.content = content_detail
            article_model.image_id = save_img
            print(article_model)
            article_model.save()
            print(article_model.id)
                
            
            
        
    
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
            

        
        
