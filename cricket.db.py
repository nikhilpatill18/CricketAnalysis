import sqlite3

# conn=sqlite3.connect('cricket.db')
# cursor =conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS Champions (
#     Year INTEGER PRIMARY KEY,
#     Host TEXT,
#     Teams INTEGER,
#     Champion TEXT,
#     RunnerUp TEXT,
#     Player_of_Series TEXT,
#     Highest_Run_Scorer TEXT,
#     Highest_Wicket_Taker TEXT,
#  )''')

# conn.commit()
# conn.close()
# import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("cricket.db")
cursor = conn.cursor()

# Query to get column names of the table
cursor.execute("PRAGMA table_info(Champions);")

# Fetch all columns information
columns = cursor.fetchall()

# Extract and print column names
column_names = [column[1] for column in columns]  # column[1] holds the column name
print("Column Names:", column_names)

# Close the connection
conn.close()
