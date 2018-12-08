# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:37:25 2018

@author: ratchanonth
"""

from langdetect import detect

from bs4 import BeautifulSoup
import urllib.request
import os,json,sys,datetime,requests






class deadshot():
    #####
   
    dit={}
    
    
    def link_2_dit(self,link): 
            not_in_list=list()
            web_in_list=list()
            
            grp =list()
            no_grp =list()
            for data in link:
               tag=data.split('wiki/') 
               try:
                   group=tag[1].split('/')
                   if(group[0] != ''):
                       if (detect(group[0]) == 'en'):
                          grp.append(group[0])
                       else:
                           pass
                   #dict_data[group[0]]=group[1:] 
               except:
                   no_grp.append(tag[0])
            grp = list(set(grp))
            for i in grp:
                for j in link:
                    if i in j:
                        web_in_list.append(j)
                    else:
                        not_in_list.append(j)
                        #print(list_1)
                #print('key=',i,' value = ',web_in_list)
                self.dit[i]=web_in_list.copy()
                web_in_list.clear()
            print("Classifile_succ!!!\n"); 
            return self.dit
        
   
   
    
                
class TNT():
    
   
    text_read={}          
    list_url=list()
    description=list()
    data_set=list()

 
    def crawler_linke(self,clf_link):
        clf_linked=clf_link
        for _,j in clf_linked.items():
            for link_ in j:
                
                try:
                    page = urllib.request.urlopen(link_)
                except Exception as s:
                    print('HTTP -404\n',s.args)
                    pass
                soup = BeautifulSoup(page, 'html.parser')
                requ=soup.find('div',attrs={'id': "mw-content-text"})
                head=soup.find('h1', {'id' : 'firstHeading'})
                if requ is not None : # เช็ค ว่ามี text ส่งมาไหม
                        try:
                            lang=detect(head.text)
                            print(lang)     
                        except Exception as s:
                            print("Error-->",s.args)
                            
                        inside_={lang:requ.get_text()}
                        self.description.append(inside_)
                        head_=head.text
                        self.list_url.append(link_)
                        date=self.get_dateTime()
                        self.text_read={'Topic':head_,'link':self.list_url,'description':self.description,'date':date}
                        
                else:
                         pass
                     
              
            if len(self.text_read['link']) == 0:
                pass
        print(self.text_read)
        return self.text_read
                        
         
    
        


    def get_dateTime(self):
            now_ = datetime.datetime.now()
            datetime_ = '('+str(now_.year)+'-'+str(now_.month)+'-'+str(now_.day)+' '+str(now_.hour)+':'+str(now_.minute)+':'+str(now_.second)+')'
            return datetime_
        
    
    
   
   
            

if __name__=="__main__":
    a=TNT()
    a
    ###############___main___##################
    ##
    '''
    check_dir()                              ##
    feed=list()                              ##                        
    file_link=openfile(path_and_linke)       ##
    clf_en= link_2_dit(file_link)
    file_clf_en=file_new(path_get_data)               ###
                              ##
    #clf_linked=clf_linke(file_link) 
    #alon,grop=clf_link_group(clf_linked)
    #print(alon)
    ########################################           
    try:           
        print_text(clf_en,file_link)
        print("F")
    except KeyboardInterrupt:
       print("------KeyboardInterrupt------")
       sys.exit(0)
                #a.write(json.dumps(feed,ensure_ascii=False,indent=3))
     '''
                 