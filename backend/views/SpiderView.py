from django.shortcuts import redirect, render
from django.views.generic.base import View
from backend.helps.Spider import SoupLearn
import time

class SpiderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'spider/index.html')

    def post(self, request, *args, **kwargs):
        page_size = int(request.POST.get('page_size', 1))
        time_sleep = int(request.POST.get('time_sleep', 1))

        soup_learn = SoupLearn()
        if page_size > 1:
            for page in range(1, page_size + 1):
                soup_learn.getArticleList(page)
                time.sleep(time_sleep)
        else:
            soup_learn.getArticleList(1)
            time.sleep(time_sleep)
        return redirect('/spider/index')