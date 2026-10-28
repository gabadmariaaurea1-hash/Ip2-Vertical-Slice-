import sqlite3

c = sqlite3.connect("Api/verticalslice.db")

print("TABLES:")
for row in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
    print(row[0])

print("\nCOURSES SCHEMA:")
row = c.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='Courses'").fetchone()
print(row[0] if row else "Courses table not found")

c.close()
