#coding=utf-8
'''
Created on 2016年4月12日

@author: PI
'''
from baike_spider import url_manger, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print "craw %s:%d" % (count, new_url)
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url,html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            
            if count == 1000:
                break
            count+=1
        self.outputer.output_html()
    
    



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm#1"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    