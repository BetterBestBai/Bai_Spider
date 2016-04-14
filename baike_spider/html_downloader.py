#coding=utf-8
'''
Created on 2016年4月12日

@author: PI
'''
import urllib2


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() !=200:
            return None
        return response.read()
    
    



