from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = "postgresql://user:password@db:5432/mydb"
engine = create_engine(DATABASE_URL)

@app.route('/api/users', methods=['GET'])
def get_users():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users"))
        users = [dict(row._mapping) for row in result]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
