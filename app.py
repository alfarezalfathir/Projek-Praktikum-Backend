# Setup awal
from flask import Flask, request, jsonify, render_template
from models import db, Sensor
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()


# Api Kirim data ke sensor
@app.route("/api/kirim", methods=["POST"])
def kirim_data():
    data = request.get_json()

    suhu = data.get("suhu")
    kelembapan = data.get("kelembapan")

    # LOGIKA OTOMATIS
    if suhu >= 30 and kelembapan <= 60:
        pompa = "ON"
    else:
        pompa = "OFF"

    sensor = Sensor(
        suhu=suhu,
        kelembapan=kelembapan,
        pompa=pompa
    )

    db.session.add(sensor)
    db.session.commit()

    return jsonify({
        "suhu": suhu,
        "kelembapan": kelembapan,
        "pompa": pompa
    })

# Api ambil data
@app.route("/api/data", methods=["GET"])
def get_data():
    data = Sensor.query.all()
    hasil = [{
        "suhu": d.suhu,
        "kelembapan": d.kelembapan,
        "pompa": d.pompa,
        "waktu": d.waktu
    } for d in data]

    return jsonify(hasil)

# Halaman web
@app.route("/")
def home():
    return render_template("index.html")

# Jalankan server
if __name__ == "__main__":
    app.run(debug=True)