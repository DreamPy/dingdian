base = "http://www.x23us.com/html/26/26612/"
import re
import time
import random
import urllib.request
def getChapterAndUrl(url):
    html = download(url)
    pa = """<a href="([0-9]+.html)">(第[^<>]*?章[^<>]*?)</a>"""
    r = re.findall(pa,html)
    if len(r) == 0:
        print("getChapterAndUrl Error")
    else:
        return r
def getParams(r,base):
    for url,name in r:
        yield [base+url,name]
def download(url,encoding="GBK"):
    time.sleep(random.choice(range(30))/1000)
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57."}
    req = urllib.request.Request(url,headers=headers)
    try:
        response = urllib.request.urlopen(req).read()
        encodings=[encoding,'GB2312','utf-8']
        for coding in encodings:
            try:
                
                return response.decode(coding,'ignore')
            except UnicodeDecodeError as e:
                
                print(e)
                continue
        return response
    except urllib.error.HTTPError as e:
        print(e.code)
def writeToFile(fileName,contents,title):
    with open(fileName,'a') as f:
        f.write("------>"+title+"\n")
        f.write(contents+"\n")
        f.write("...........ending\n")
def getContent(html):
    pac = """<dd id="contents">(.*?)</dd>"""
    r = re.findall(pac,html)
    if len(r) == 0 or len(r) >1:
        print("getContent Error")
        return False
    else:
        return r[0]
def dealStyle(content):
    return content.replace("&nbsp;",' ').replace("<br /><br />",'\n')
        
# def tasks(params=getParams(r,),filename="莽荒纪.txt"):
#     for url,name in params:
#         html = download(url)
#         content = getContent(html)
def continueTasks(chapterName,allChapter):
    i=0

    for url,name in getParams(allChapter,base):
        
        if chapterName == name:
            
            i+=1
            continue
        if i == 1:
            for j in range(5):
                try:
                    task(url,name)
                    break
                except Exception as e:
                    
                    continue
def allTasks(curls,filename,base):
    for url,name in getParams(curls,base):
        for j in range(10):
            try:
                task(url,name,filename)
                break
            except Exception as e:
                if j == 9:
                    writeEorror(url,name)
                    insertError(filename,url,name)
                else:
                    continue
def writeEorror(url,name):
    with open("downloadFail.txt",'a') as f:
        f.write(url)
        f.write(",")
        f.write(name)
        f.write("\n")
def insertError(fileName,url,name):
    with open(fileName,'a') as f:
        f.write("[Error]")
        f.write(url)
        f.write(",")
        f.write(name)
        f.write("\n")
        
def task(url,name,filename="莽荒纪3.txt"):
    print("task {0}{1}".format(url,name))
    html = download(url)
    content = getContent(html)
    text = dealStyle(content)
    writeToFile(filename,text,name)
