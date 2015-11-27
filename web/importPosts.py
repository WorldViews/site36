
import feedparser as fp
import BlogAPI

import os, sys, codecs, datetime
from time import mktime
from datetime import datetime

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def verifyDir(dirPath):
    if not os.path.exists(dirPath):
        print "Creating", dirPath
        os.makedirs(dirPath)

def tweakDate(dateTup):
    #print dateTup
    t = mktime(dateTup)
    #print "t:", t
    dt = datetime.fromtimestamp(t)
    #print "dt:", dt
    return dt

class Importer:
    def __init__(self):
        self.blog = BlogAPI.Blog()
        self.numPosts = 0

    def importEntry(self, entry):
        global num
        print entry.keys()
        postsDir = "posts"
        verifyDir(postsDir)
        id = entry['id']
        title = entry['title']
        authors = entry['authors']
        authorName = authors[0]['name']
        datePublished = entry['published']
        dateTuple = entry['published_parsed']
        date = tweakDate(dateTuple)
        content = entry['content']
        if len(content) != 1:
            print "*** Warning not sure what to do with multiple contents"
        content = content[0]
        print "Id:", id
        print "Title:", title
        print "Published:", datePublished, dateTuple, date
        print "Authors:", authors
        print "AuthorName:", authorName
        print "Content keys", content.keys()
        ctype = content['type']
        htmlStr = content['value']
        print "ctype:", ctype
        self.numPosts += 1
        hname = "%s/%d.html" % (postsDir, self.numPosts)
        print "Saving %s" % hname
        file = codecs.open(hname, "w", "utf-8")
        file.write(htmlStr)
        self.blog.addEntry(author=authorName, title = title, content=htmlStr, date=date)

    def importFeed(self, url):
        d = fp.parse(url)
        entries = d['entries']
        for entry in entries:
            self.importEntry(entry)
            print "----------"


if __name__ == '__main__':
    im = Importer()
    im.blog.deleteAllEntries()
    url = "http://gobeyondthefence.com/feed/"
    im.importFeed(url)



