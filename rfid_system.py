from flask import Flask, request, render_template, redirect, url_for, session
import time

app = Flask(__name__)
app.secret_key = 'tajny_klic'

attendance_file = "prezence.txt"

users = {
    "0012298380": {"name": "Uzivatel 1", "status": "active"},
    "0012310619": {"name": "Uzivatel 2", "status": "blocked"}
}

def write_attendance(user_name, tag_id, entry_type, action):
    timestamp = time.strftime('%d.%m.%Y %H:%M:%S')
    with open(attendance_file, "a") as f:
        f.write(f"{user_name} (ID: {tag_id}) - {entry_type} ({action}) - {timestamp}\n")

def log_blocked_attempt(tag_id):
    timestamp = time.strftime('%d.%m.%Y %H:%M:%S')
    with open(attendance_file, "a") as f:
        f.write(f"Zablokovaný pokus: UID {tag_id} - {timestamp}\n")

@app.route('/')
def main_page():
    return render_template('mainPage.html')

@app.route('/admin')
def index():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['admin_logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Špatné přihlašovací údaje")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('main_page'))

@app.route('/add_user', methods=['POST'])
def add_user():
    tag_id = request.form.get('tag_id')
    user_name = request.form.get('user_name')
    if tag_id and user_name:
        users[tag_id] = {"name": user_name, "status": "active"}
    return redirect(url_for('index'))

@app.route('/add_user_form')
def add_user_form():
    return render_template('add_user_form.html')

@app.route('/remove_user/<tag_id>')
def remove_user(tag_id):
    if tag_id in users:
        del users[tag_id]
    return redirect(url_for('index'))

@app.route('/block_user/<tag_id>')
def block_user(tag_id):
    if tag_id in users:
        users[tag_id]["status"] = "blocked"
    return redirect(url_for('index'))

@app.route('/unblock_user/<tag_id>')
def unblock_user(tag_id):
    if tag_id in users:
        users[tag_id]["status"] = "active"
    return redirect(url_for('index'))

@app.route('/log_attendance', methods=['POST'])
def log_attendance():
    tag_id = request.form.get('tag_id')
    entry_type = request.form.get('type', 'Neznámý typ')  # Příchod nebo Odchod
    action = request.form.get('action', 'Neznámá akce')

    if tag_id:
        if tag_id in users:
            user = users[tag_id]
            if user["status"] == "blocked":
                log_blocked_attempt(tag_id)
            else:
                write_attendance(user["name"], tag_id, entry_type, action)
        else:
            return "Neznámý uživatel!", 400
    else:
        return "UID nebylo rozpoznáno!", 400

    return redirect(url_for('main_page'))

@app.route('/log_attendance_form')
def log_attendance_form():
    return render_template('log_attendance_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
