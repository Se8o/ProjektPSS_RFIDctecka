from flask import Flask, request, render_template, redirect, url_for
import time

app = Flask(__name__)

# Cesta k souboru s přítomností
attendance_file = "prezence.txt"

# Seznam uživatelů a jejich UID, stav "active" nebo "blocked"
users = {
    "0012298380": {"name": "Uzivatel 1", "status": "active"},
    "0012310619": {"name": "Uzivatel 2", "status": "blocked"}
}

def write_attendance(user_name, tag_id):
    """Funkce pro zápis přítomnosti do souboru"""
    with open(attendance_file, "a") as f:
        f.write(f"{user_name} (ID: {tag_id}) - {time.ctime()}\n")

def log_blocked_attempt(tag_id):
    """Funkce pro zaznamenání pokusu zablokovaného uživatele"""
    with open(attendance_file, "a") as f:
        f.write(f"Zablokovaný pokus: UID {tag_id} - {time.ctime()}\n")

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    tag_id = request.form.get('tag_id')
    user_name = request.form.get('user_name')
    if tag_id and user_name:
        users[tag_id] = {"name": user_name, "status": "active"}
    return redirect(url_for('index'))

@app.route('/add_user_form')
def add_user_form():
    """Route to display the user addition form"""
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
    if tag_id:
        if tag_id in users:
            user_name = users[tag_id]["name"]
            status = users[tag_id]["status"]
            if status == "blocked":
                log_blocked_attempt(tag_id)
            else:
                write_attendance(user_name, tag_id)
        else:
            return "Neznámý uživatel!", 400
    return redirect(url_for('index'))

@app.route('/log_attendance_form')
def log_attendance_form():
    """Route to display the attendance logging form"""
    return render_template('log_attendance_form.html')

if __name__ == '__main__':
    app.run(debug=True)
