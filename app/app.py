from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
import os
import pandas as pd
from werkzeug.utils import secure_filename
from config import Config
from .scheduler import scheduler, schedule_messages_from_df
from .utils import ensure_logs_dir, log_message

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
ALLOWED_EXTENSIONS = {'csv'}

ensure_logs_dir(Config.LOG_PATH)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.getenv("FLASK_SECRET", "CHANGE_ME_SECRET_KEY")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html", default_schedule=Config.DEFAULT_SCHEDULE)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    if 'contacts_file' not in request.files:
        flash("No file part")
        return redirect(url_for('index'))
    file = request.files['contacts_file']
    if file.filename == '':
        flash("No selected file")
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        df = pd.read_csv(path)
        schedule_messages_from_df(df, default_schedule=Config.DEFAULT_SCHEDULE)
        flash(f"Uploaded and scheduled {len(df)} contacts.")
        return redirect(url_for('index'))
    flash("Invalid file type")
    return redirect(url_for('index'))

@app.route('/preview', methods=['POST'])
def preview():
    name = request.form.get('name', 'RECIPIENT')
    message = request.form.get('message', '')
    email = request.form.get('email', '')
    whatsapp = request.form.get('whatsapp', '')
    return render_template("preview.html", name=name, message=message, email=email, whatsapp=whatsapp)

@app.route('/logs')
def logs():
    log_path = Config.LOG_PATH
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            data = f.read()
    else:
        data = "No logs yet."
    return "<pre>{}</pre>".format(data.replace("<", "&lt;"))

if __name__ == '__main__':
    scheduler.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
