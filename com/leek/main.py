#!/usr/bin/env python

import os
import os.path
import chardet

'''from io import open
p = 'D:\\workspace\\ebank-dev\\EasyBankingWeb\\EasyBankingWeb\\WebContent\\jsp\\golddeferdepothisquery\\golddeferdepothisquery-gold-defer-depot-his-query-init-form-view.jsp'
f = open(p, 'r', None, 'UTF8')
print(f.read(1000))'''

p = 'D:\\workspace\\ebank-dev\\EasyBankingWeb\\EasyBankingWeb\\WebContent\\jsp'

def selectedFile():
    fn = 0
    u8 = 0
    ot = 0
    for parent, dirnames, filenames in os.walk(p):
        #print(strparent.)
        '''if parent.find('.svn') == -1:
            print(dirnames)'''
        for filename in filenames:
            #if parent.find('.svn') == -1:
            if not parent.endswith('jsp') and filename.endswith('.jsp'):
                #print (os.path.join(parent,filename))
                # chardet.detect
                with open(os.path.join(parent,filename), 'r',-1, 'UTF8') as f:
                    try:
                        if f.read(10000).find('disableButton'):
                            fn = fn+1
                    except Exception as ex:
                        print(f)
                        ot = ot+1
                        
                        
            #print ( " filename with full path:" + os.path.join(parent,filename)) 
    
    print(fn)
    print(ot)



def restoreMap(filename='c:/ebank_jsp_encode2.txt'):
    map = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            map[line[23:-1].strip()] = line[0:19].strip()
    return map

# 
if __name__ == '__main__':
    from com.leek import util
    
    map = restoreMap()
    for k, v in map.items():
        with open(k, 'r', encoding=v) as f:
            txt = f.read()
            if txt.find('disableButton')>0 and txt.find('html:form')>0 and txt.find('html:select')>0:
                print(k)
    

