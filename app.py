from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():

    notes = Note.query.order_by(Note.id.desc()).all()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    if content:
        db.session.add(Note(title=title, content=content))
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        # Раскомментируй db.drop_all() только если нужно сбросить базу
        # db.drop_all()
        db.create_all()
    app.run(debug=True)