
import feedparser as fp

import codecs
import os, sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def verifyDir(dirPath):
    if not os.path.exists(dirPath):
        print "Creating", dirPath
        os.makedirs(dirPath)


class RSSFetcher:
    def __init__(self):
        self.numSaved = 0

    def dumpEntry(self, entry):
        global num
        print entry.keys()
        postsDir = "posts"
        verifyDir(postsDir)
        id = entry['id']
        title = entry['title']
        authors = entry['authors']
        datePublished = entry['published']
        dateSpec = entry['published_parsed']
        content = entry['content']
        if len(content) != 1:
            print "*** Warning not sure what to do with multiple contents"
        content = content[0]
        print "Id:", id
        print "Title:", title
        print "Published:", datePublished, dateSpec
        print "Authors:", authors
        print "Content keys", content.keys()
        ctype = content['type']
        str = content['value']
        print "ctype:", ctype
        self.numSaved += 1
        hname = "%s/%d.html" % (postsDir, self.numSaved)
        print "Saving %s" % hname
        file = codecs.open(hname, "w", "utf-8")
        file.write(str)


    def fetch(self, url):
        d = fp.parse(url)
        feed = d['feed']
        entries = d['entries']
        for entry in entries:
            self.dumpEntry(entry)
            print "----------"


if __name__ == '__main__':
    url = "http://gobeyondthefence.com/feed/"
    rf = RSSFetcher()
    rf.fetch(url)
