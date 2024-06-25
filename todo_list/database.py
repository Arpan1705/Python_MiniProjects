import sqlite3

def connect_db():
    return sqlite3.connect("todo.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            duration INTEGER
        )
        '''
    )
    conn.commit()
    conn.close()

def add_task(task, duration=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, duration) VALUES (?, ?)', (task, duration))
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()    

    return tasks

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
