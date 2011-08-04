import glob
import os

'''filenames = glob.glob("c:/jsp/")
for name in filenames:
    print(name)
    os.mkdir()
    '''

def messageAnalyse():
    '''
    analyse message's sending and response
    especially has no respone
    '''
    f = 'c:/message2.txt'   #message file
    m_port = 'N27211e'      #message port
    d = {}                  #
    with open(f, 'r', encoding='utf-8') as f:
        for line in f:
            if line.find(m_port) == -1:
                continue
            index_s = line.find(m_port) + 9
            webseqno = line[index_s:index_s + 7]
            if webseqno != '':
                d[webseqno] = d.get(webseqno, 0) + 1
                
    for k, v in d.items():
        print(k, v)


if __name__ == '__main__':
    messageDo()