import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    print("=== Python REST API Test ===\n")
    
    print("1. Ana sayfa kontrolü:")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("2. Tüm kullanıcıları listele:")
    response = requests.get(f"{BASE_URL}/users")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("3. Belirli kullanıcı getir (ID: 1):")
    response = requests.get(f"{BASE_URL}/users/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("4. Yeni kullanıcı ekle:")
    new_user = {"name": "Fatma Özkan", "email": "fatma@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("5. Kullanıcı güncelle (ID: 2):")
    update_data = {"name": "Ayşe Demir Güncellendi", "email": "ayse.updated@example.com"}
    response = requests.put(f"{BASE_URL}/users/2", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("6. İstatistikleri görüntüle:")
    response = requests.get(f"{BASE_URL}/stats")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")
    
    print("7. Health check:")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("API sunucusu çalışmıyor. Önce 'python app.py' ile başlatın.")
    except Exception as e:
        print(f"Hata: {e}")