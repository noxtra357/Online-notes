import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных в папке проекта
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель заметки
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(200), nullable=False)

# Главная страница (список заметок)
@app.route('/')
def index():
    notes = Note.query.order_by(Note.id.desc()).all()
    return render_template('index.html', notes=notes)

# Добавление новой заметки
@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    if content:
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('index'))

# Удаление заметки
@app.route('/delete/<int:id>')
def delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        # Это создаст базу данных, если её нет
        db.create_all()
    app.run(debug=True)