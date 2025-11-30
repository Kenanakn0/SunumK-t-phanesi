from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ahmet Yılmaz", "email": "ahmet@example.com"},
    {"id": 2, "name": "Ayşe Demir", "email": "ayse@example.com"},
    {"id": 3, "name": "Mehmet Kaya", "email": "mehmet@example.com"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Python REST API Çalışıyor",
        "timestamp": datetime.now().isoformat(),
        "endpoints": [
            "GET /users - Tüm kullanıcıları listele",
            "GET /users/<id> - Belirli kullanıcıyı getir",
            "POST /users - Yeni kullanıcı ekle",
            "PUT /users/<id> - Kullanıcı güncelle",
            "DELETE /users/<id> - Kullanıcı sil"
        ]
    })

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users, "count": len(users)})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "Kullanıcı bulunamadı"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name ve email gerekli"}), 400
    
    new_id = max([u["id"] for u in users]) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Kullanıcı bulunamadı"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Veri gerekli"}), 400
    
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "Kullanıcı bulunamadı"}), 404
    
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "Kullanıcı silindi"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)