
from BlogAPI import Blog

str = raw_input("Really clear database?")
if str.lower() in ['yes', 'y']:
    b = Blog()
    b.deleteAllEntries()


