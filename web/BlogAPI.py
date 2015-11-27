"""
This class is a thin wrapper around the zinnia/django database to 
try and present an API for edititing the posts, such as deleting
or adding them programmatically.

It was first written for PaloAltoCSM and seemed to work on that
and works for this repo enough to do somethings, but not all this
has been tested.
"""

import sys, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

import zinnia.models

from zinnia.views.quick_entry import timezone
from zinnia.views.quick_entry import *
#from mysite.models import User, EntryMailData
#from models import User, EntryMailData
from mysite.models import User
from django.db import connection

class Blog:
    def __init__(self):
        #self.dump()
        pass

    def deleteAllEntries(self):
        print "delteAllEntries"
        """
        This should work but with sqlite3 it gets error
        'too many variables'  This seems very junky to me. :(
        """
        zinnia.models.Entry.objects.all().delete()
        """
        Instead we will do this
        """
        '''
        cursor = connection.cursor()
        #com = 'TRUNCATE TABLE "{0}"'.format(
        com = 'DELETE FROM "{0}"'.format(
                zinnia.models.Entry._meta.db_table)
        print "com:", com
        cursor.execute(com)
        '''

    def dump(self):
        self.dumpUsers()
        print "------------------"
        self.dumpEntries()

    def findUser(self, username):
        user = User.objects.filter(username=username).all()
        print user
        if not user:
            return None
        return user[0]

    def checkUser(self, username, realname, email):
        user = self.findUser(username)
        if user:
            return user
        parts = realname.split()
        if len(parts) == 1:
            first_name = parts[0]
            last_name = ""
        else:
            first_name = parts[0]
            last_name = parts[1]
        user = User(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        user.save()

    def dumpUsers(self):
        print "Users:"
        for user in User.objects.all():
            print user, user.email
            #print "email: %s" % (user.email,)
            print

    def dumpEntries(self):
        print "Entries:"
        entries = zinnia.models.Entry.objects.all()
        for ent in entries:
            authors = ent.authors.all()
            print ent.pk, ent
            for author in authors:
                print "  ", author

    def findEntryByMsgId(self, msgId):
        #print "findEntryByMsgId", msgId
        data = EntryMailData.objects.filter(msg_id=msgId);
        if data:
            #print "found data", data
            return data[0].entry
        #print "No entry found"
        return None

    def addEntry(self, author, title, content, date=None, msgId=None):
        print "Adding entry to blog", author, title
        user = self.findUser(author)
        if date == None:
            date = timezone.now()
        if msgId:
            entry = self.findEntryByMsgId(msgId)
            if entry:
                print "Already have entry:", entry
                return
        if not user:
            return "Can't find user"
        data = {'title': title,
                'slug': slugify(title),
                'status': PUBLISHED,
                'sites': [Site.objects.get_current().pk],
                'authors': [user.pk],
                'content_template': 'zinnia/_entry_detail.html',
                'detail_template': 'entry_detail.html',
#                'creation_date': timezone.now(),
                'creation_date': date,
                'last_update': timezone.now(),
                'content': content,
                'tags': "dummy"}

        form = QuickEntryForm(data)
        if form.is_valid():
            form.instance.content = linebreaks(form.cleaned_data['content'])
            entry = form.save()
            print "Added and saved"
            """
            obj = EntryMailData(msg_id=msgId, entry=entry)
            obj.save()
            print "Saved link %s %s" % (entry.pk, msgId)
            """
        else:
            print "problem with entry"


testContent = """
This is the body
of the third multiline
dummy test article.
"""

def clear():
    b = Blog()
    b.deleteAllEntries()

def test():
    b = Blog()
    b.dump()
    date = timezone.now()
    print "date:", date
    b.addEntry(author="kimber", title="a test post", content=testContent, date=date)


if __name__ == '__main__':
    clear()
    test()
#     print "That's all..."



