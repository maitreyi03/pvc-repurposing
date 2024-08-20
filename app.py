import sqlite3

conn = sqlite3.connect('pvc_reuse.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE projects (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    image BLOB NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')

conn.commit()

def save_project(title, description, image):
    query = "INSERT INTO projects (title, description, image) VALUES (?, ?, ?)"
    cursor.execute(query, (title, description, image))
    conn.commit()

with open('path_to_image.jpg', 'rb') as file:
    binary_image = file.read()
    save_project('Creative Planters', 'A local artist...', binary_image)

cursor.close()
conn.close()
