# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request
import os,json,sys
from deadshot import TNT,deadshot
sys.setrecursionlimit(65000) #ทำให้ overstep recurtive

class wiki:
    set_link=list()
    set_next_link=None
    count=0
    defus_url="https://meta.wikimedia.org/wiki/Special:AllPages" # link เริ่มต้น
    url=None
    url_next=None
    
    def __init__(self):
        
        self.link_all={}
        self.link_all_1=list()
        
    
        
    def __str__(self,url):
        return (url)
    
    #เก็บลิ้งในหมวดต่างๆ
    
    def get_link_p(self,url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        requ=soup.find('div',attrs={'class': "mw-allpages-body"}).find_all('a', href=True)
        for i in requ:
            self.link_all['link']=(self.__str__('https://meta.wikimedia.org'+i.attrs['href']))
            self.set_link.append(self.link_all['link'])

        return self.set_link

            
    #เก็บ next page
    
    def find_to_next(self,url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        req_next=soup.find('div',attrs={'class': "mw-allpages-nav"}).find_all('a', href=True)
        for j in req_next:
            self.link_all['next']=(self.__str__('https://meta.wikimedia.org'+j.attrs['href']))
        self.set_next_link=self.link_all['next']
        return self.set_next_link

    #รวมการทำงานของ 2โปรแกรมด้านบน        
    def all_find(self,url):
        link=self.get_link_p(url)
        next_link=self.find_to_next(url)
        return link,next_link
        

    def crawler_link(self,set_next_link='https://meta.wikimedia.org/wiki/Special:AllPages'): #fuction ดึง link แล้วเก็บไว้ใน json 
        self.url=set_next_link
        url_1,next_link_1=self.all_find(self.url)
        return url_1,next_link_1
                
                #return ออกมาสองตัว คือ link and next_link
        #self.save_file_json(self.file)   


wiki_leak=wiki()
c=deadshot() 
tnt=TNT()
a,b=wiki_leak.crawler_link() 
while(b not None)                   
    a,b=wiki_leak.crawler_link(b) 
    ans_link=c.link_2_dit(a)
    
    n=tnt.crawler_linke(ans_link)