import urllib
import re

#handling the page tags
class Tool:
    #remove img tags,7 chars space
    removeImg = re.compile('<img.*?>| {7}|')
    #remove hyperlink tags
    removeAddr = re.compile('<a.*?>|</a>')
    #new line as \n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #<td> as \t
    replaceTD= re.compile('<td>')
    #starter with two space 
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    #remove other tags
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #use strip()delete the unwilling parts
        return x.strip()

#crawling Tieba Class
class BDTB:

    #Initialization
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
    #pass the page number, get the info
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print (u"can not connect the Tieba Website, for reasons:",e.reason)
                return None

    #get the title of the article
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #test for the output
            return result.group(1).strip()
        else:
            return None

    #get the number of the page
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            #print result.group(1)  #test for the output
            return result.group(1).strip()
        else:
            return None

    #get the information of each block
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        #for item in items:
        #  print item
        print (self.tool.replace(items[1]))

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getContent(bdtb.getPage(1)) 
