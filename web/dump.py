import sqlite3

db = 'db.sqlite3'
print "Dumping info about", db
con = sqlite3.connect(db)
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
names = []
for line in cursor.fetchall():
    names.append(line[0])

print "Tables:"
for name in names:
    print name
print
print
print "Tables and columns:"
for name in names:
    print name
    com = "PRAGMA table_info(%s)" % name
    cursor.execute(com)
    for row in cursor:
        print "  ", row
    print


