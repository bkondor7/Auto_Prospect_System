import sqlite3

# Database
def create_database():
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()
    cursor.execute("'CREATE TABLE IF NOT EXISTS listings(id INTEGER PRIMARY KEY, title TEXT, price TEXT, contact TEXT)")
    conn.commit()
    conn.close()
    
def save_listings(listings):
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()
    for listing in listings:
        cursor.execute('INSERT INTO listings(title, price, contact) VALUES(?, ?, ?)', (listing['title'], listing['price'], listing['contact']))
        conn.commit()
        conn.close()

# Filter/Analyze
def filter_listings(min_price, max_price):
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM listings WHERE price BETWEEN ? AND ?', (min_price, max_price))
    filtered_listings = cursor.fethchall()
    conn.close()
    
    return filtered_listings