#!/usr/bin/env python


#recorde output info to file, default to c:/pout.txt
def myout(s_str, file='c:/pout.txt'):
    from datetime import datetime
    with open(file, mode='a', encoding='utf-8') as out:
        out.write('\n\n-------------- ' + str(datetime.now()) + ' --------------\n')
        out.write(s_str)
        
        ''' #example for ...
        for k, v in map.items():
            out.write(v.ljust(20) + ' : ' + k +'\n')
        '''


#detecting the file's encoding
def detectEncodeOfFile(filename):
    from chardet.universaldetector import UniversalDetector
    detector = UniversalDetector()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result['encoding']


#detecting encodings of multiple files --python3 =likun
def detectEncodeOfMFiles(filenames):
    from chardet.universaldetector import UniversalDetector
    
    m_files_encodes = dict()
    detector = UniversalDetector()
    for filename in filenames:
        detector.reset()
        for line in open(filename, 'rb'):
            detector.feed(line)
            if detector.done: break
        detector.close()
        m_files_encodes[filename] = detector.result['encoding']
    return m_files_encodes


# detecting character encoding of web site --python3 =likun
def detectWebSiteEncode(url='http://google.com/'):
    import urllib.request
    import chardet
    site = urllib.request.urlopen(url).read()
    print('url: ' + url)
    print(chardet.detect(site))


# advanced detecting character encoding of web site, replace detectWebSiteEncode() --python3 =likun
def detectWebSiteEncodeAV(url='http://google.com/'):
    import urllib.request
    from chardet.universaldetector import UniversalDetector
    detector = UniversalDetector()
    site = urllib.request.urlopen(url)
    for line in site.readlines():
        detector.feed(line)
        if detector.done: break
    detector.close()
    site.close()
    return detector.result['encoding']


# get files exclude svn info in dirpath --python3 =likun
def filesExcludeSvn(rootdir):
    import os
    files = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if parent.find('.svn') < 0:
                files.append(os.path.join(parent,filename))
    return files