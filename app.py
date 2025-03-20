from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data dari file CSV
data = pd.read_csv('data_kegiatan_siswa.csv') 

@app.route('/data', methods=['GET'])
def get_data():
    # Ubah data ke format JSON dan kembalikan
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)