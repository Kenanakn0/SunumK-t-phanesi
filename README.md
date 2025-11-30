# Python REST API

Basit bir Python tabanlı REST API uygulaması. Flask framework kullanılarak geliştirilmiştir.

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. API'yi başlatın:
```bash
python app.py
```

API http://localhost:5000 adresinde çalışacaktır.

## API Endpoints

### Ana Sayfa
- **GET** `/` - API bilgileri ve mevcut endpoint'leri listeler

### Kullanıcı İşlemleri
- **GET** `/users` - Tüm kullanıcıları listeler
- **GET** `/users/<id>` - Belirli bir kullanıcıyı getirir
- **POST** `/users` - Yeni kullanıcı ekler
- **PUT** `/users/<id>` - Kullanıcı bilgilerini günceller
- **DELETE** `/users/<id>` - Kullanıcıyı siler

### İstatistikler
- **GET** `/stats` - Kullanıcı istatistiklerini gösterir (toplam sayı, email domainleri, son kullanıcı)

### Sistem
- **GET** `/health` - API durumunu kontrol eder

## Kullanım Örnekleri

### Tüm kullanıcıları listele
```bash
curl http://localhost:5000/users
```

### Yeni kullanıcı ekle
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Yeni Kullanıcı", "email": "yeni@example.com"}'
```

### Kullanıcı güncelle
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Güncellenmiş İsim", "email": "guncellenmis@example.com"}'
```

### Kullanıcı sil
```bash
curl -X DELETE http://localhost:5000/users/1
```

### İstatistikleri görüntüle
```bash
curl http://localhost:5000/stats
```

## Test

API'yi test etmek için test scripti çalıştırın:
```bash
pip install requests
python test_api.py
```

## Özellikler

- CRUD operasyonları (Create, Read, Update, Delete)
- JSON formatında veri alışverişi
- Hata yönetimi
- Health check endpoint'i
- Türkçe hata mesajları
- Basit kullanıcı veri modeli

## Teknik Detaylar

- **Framework**: Flask 2.3.3
- **Port**: 5000
- **Host**: 0.0.0.0 (tüm network interface'lerden erişilebilir)
- **Debug Mode**: Aktif (geliştirme için)