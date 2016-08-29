import sqlite3

conn = sqlite3.connect('mbox.sqlite')
cursor = conn.cursor();

try:
    cursor.execute('''CREATE TABLE Counts (email TEXT, count INTEGER);
    ''')
except:
    print 'Already exists'
    # cursor.execute('''DROP TABLE Counts
    # ''')
file = open('mbox.txt')
for line in file:
    l = line.strip();
    if not l.startswith('for '):
        continue
    raw_line = l.split();
#    print raw_line
    email = raw_line[1];

    cursor.execute('''select count from Counts where email = ?''', (email,))
    row = cursor.fetchone()
    if row == None:
        sql = '''insert into Counts(email, count) values(?,1)'''
        cursor.execute(sql, (email,))
    else:
        sql = '''Update Counts set count=count+1 where email=?'''
        cursor.execute(sql,(email,))
    conn.commit()

conn.close()