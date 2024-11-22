from database import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'titulo': self.titulo, 'autor': self.autor}
