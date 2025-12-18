from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suhu = db.Column(db.Float)
    kelembapan = db.Column(db.Float)
    pompa = db.Column(db.String(10))  # ON / OFF
    waktu = db.Column(db.DateTime, default=datetime.utcnow)
