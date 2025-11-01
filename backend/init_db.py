# init_db.py
import sqlite3, os
from config import DB_PATH

# 1) Klasörleri aç
os.makedirs(DB_PATH.parent, exist_ok=True)

# 2) Veritabanını aç
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 3) Tablonun taze kurulumu
cur.execute("DROP TABLE IF EXISTS questions")
cur.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    questionNumber INTEGER,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    correct TEXT
)
""")

# 4) VERİN (tamamını koy!)
db_quiz = {
  "Matematik": [
    {"questionNumber": 1, "question": "1. 5 + 7 sonucu kaçtır?", "options": ["10", "11", "12", "13"], "correct": "12"},
    {"questionNumber": 2, "question": "2. 15 - 8 işleminin sonucu nedir?", "options": ["5", "6", "7", "8"], "correct": "7"},
    {"questionNumber": 3, "question": "3. Bir üçgenin iç açıları toplamı kaç derecedir?", "options": ["90", "120", "180", "360"], "correct": "180"},
    {"questionNumber": 4, "question": "4. π sayısının yaklaşık değeri nedir?", "options": ["2.14", "3.14", "4.13", "3.41"], "correct": "3.14"},
    {"questionNumber": 5, "question": "5. 3² + 4² işleminin sonucu kaçtır?", "options": ["12", "13", "14", "15"], "correct": "25"},
    {"questionNumber": 6, "question": "6. Bir dik üçgende hipotenüsün karesi neye eşittir?", "options": ["Kenarların toplamına", "Kenarların farkına", "Dik kenarların kareleri toplamına", "Bir kenarın karesine"], "correct": "Dik kenarların kareleri toplamına"},
    {"questionNumber": 7, "question": "7. Bir saat 3600 saniye ise, 2 saat kaç saniyedir?", "options": ["3600", "7200", "1800", "6000"], "correct": "7200"},
    {"questionNumber": 8, "question": "8. Bir dairenin alanı nasıl bulunur?", "options": ["πr²", "2πr", "r²", "πr"], "correct": "πr²"},
    {"questionNumber": 9, "question": "9. x + 3 = 7 denkleminde x kaçtır?", "options": ["2", "3", "4", "5"], "correct": "4"},
    {"questionNumber": 10, "question": "10. 2x + 4 = 12 denkleminde x değeri nedir?", "options": ["3", "4", "5", "6"], "correct": "4"}
  ],
  "Tarih": [
    {"questionNumber": 1, "question": "1. Türkiye Cumhuriyeti ne zaman kuruldu?", "options": ["1918", "1920", "1923", "1938"], "correct": "1923"},
    {"questionNumber": 2, "question": "2. İstanbul hangi yılda fethedildi?", "options": ["1453", "1071", "1517", "1920"], "correct": "1453"},
    {"questionNumber": 3, "question": "3. Mustafa Kemal Atatürk nerede doğmuştur?", "options": ["Ankara", "Selanik", "İzmir", "Manisa"], "correct": "Selanik"},
    {"questionNumber": 4, "question": "4. Osmanlı Devleti ne zaman kuruldu?", "options": ["1071", "1299", "1453", "1517"], "correct": "1299"},
    {"questionNumber": 5, "question": "5. Lozan Antlaşması hangi yılda imzalandı?", "options": ["1919", "1921", "1923", "1926"], "correct": "1923"},
    {"questionNumber": 6, "question": "6. Kurtuluş Savaşı’nı başlatan olay nedir?", "options": ["Lozan Antlaşması", "Samsun’a çıkış", "Cumhuriyetin ilanı", "İzmir’in kurtuluşu"], "correct": "Samsun’a çıkış"},
    {"questionNumber": 7, "question": "7. Türkiye Cumhuriyeti’nin ilk Cumhurbaşkanı kimdir?", "options": ["İsmet İnönü", "Celal Bayar", "Mustafa Kemal Atatürk", "Adnan Menderes"], "correct": "Mustafa Kemal Atatürk"},
    {"questionNumber": 8, "question": "8. TBMM hangi yılda açıldı?", "options": ["1919", "1920", "1921", "1923"], "correct": "1920"},
    {"questionNumber": 9, "question": "9. Sakarya Meydan Muharebesi hangi yılda olmuştur?", "options": ["1919", "1920", "1921", "1922"], "correct": "1921"},
    {"questionNumber": 10, "question": "10. Cumhuriyet ne zaman ilan edildi?", "options": ["29 Ekim 1923", "23 Nisan 1920", "19 Mayıs 1919", "30 Ağustos 1922"], "correct": "29 Ekim 1923"}
  ],
  "Bilim": [
    {"questionNumber": 1, "question": "1. Su kaç derecede donar?", "options": ["0°C", "50°C", "100°C", "-10°C"], "correct": "0°C"},
    {"questionNumber": 2, "question": "2. Atomun merkezi ne olarak adlandırılır?", "options": ["Elektron", "Proton", "Nötron", "Çekirdek"], "correct": "Çekirdek"},
    {"questionNumber": 3, "question": "3. Güneş sistemi merkezinde ne vardır?", "options": ["Dünya", "Ay", "Güneş", "Mars"], "correct": "Güneş"},
    {"questionNumber": 4, "question": "4. Yerçekimini kim keşfetmiştir?", "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "correct": "Isaac Newton"},
    {"questionNumber": 5, "question": "5. Işık hangi hızla hareket eder?", "options": ["3.000 km/s", "30.000 km/s", "300.000 km/s", "3.000.000 km/s"], "correct": "300.000 km/s"},
    {"questionNumber": 6, "question": "6. İnsan vücudundaki en büyük organ nedir?", "options": ["Kalp", "Beyin", "Cilt", "Karaciğer"], "correct": "Cilt"},
    {"questionNumber": 7, "question": "7. Fotosentez hangi canlılarda gerçekleşir?", "options": ["Hayvanlar", "Bitkiler", "Mantarlar", "Bakteriler"], "correct": "Bitkiler"},
    {"questionNumber": 8, "question": "8. Elektron negatif mi pozitif mi yüklüdür?", "options": ["Pozitif", "Negatif", "Yüksüz", "Değişken"], "correct": "Negatif"},
    {"questionNumber": 9, "question": "9. DNA’nın açılımı nedir?", "options": ["Deoksiribo Nükleik Asit", "Dinamik Nükleik Alan", "Doğal Nötron Atom", "Denatüre Nükleon Asit"], "correct": "Deoksiribo Nükleik Asit"},
    {"questionNumber": 10, "question": "10. Albert Einstein’ın en ünlü denklemi nedir?", "options": ["E=mc²", "F=ma", "V=IR", "P=mv"], "correct": "E=mc²"}
  ],
  "Coğrafya": [
    {"questionNumber": 1, "question": "1. Türkiye’nin başkenti neresidir?", "options": ["İstanbul", "Ankara", "İzmir", "Bursa"], "correct": "Ankara"},
    {"questionNumber": 2, "question": "2. Ekvator nedir?", "options": ["Bir ülke", "Bir dağ", "Bir çizgi", "Bir okyanus"], "correct": "Bir çizgi"},
    {"questionNumber": 3, "question": "3. Kutup bölgelerinde genellikle hangi iklim görülür?", "options": ["Ekvatoral", "Karasal", "Tundra", "Muson"], "correct": "Tundra"},
    {"questionNumber": 4, "question": "4. Dünyanın en uzun nehri hangisidir?", "options": ["Amazon", "Nil", "Mississippi", "Yenisey"], "correct": "Nil"},
    {"questionNumber": 5, "question": "5. En yüksek dağ hangisidir?", "options": ["K2", "Everest", "Ağrı", "Alpler"], "correct": "Everest"},
    {"questionNumber": 6, "question": "6. Türkiye kaç coğrafi bölgeye ayrılmıştır?", "options": ["5", "6", "7", "8"], "correct": "7"},
    {"questionNumber": 7, "question": "7. Avrupa’nın en büyük ülkesi hangisidir?", "options": ["Fransa", "İspanya", "Rusya", "Almanya"], "correct": "Rusya"},
    {"questionNumber": 8, "question": "8. Dünyanın en büyük okyanusu hangisidir?", "options": ["Atlas", "Hint", "Buz Denizi", "Pasifik"], "correct": "Pasifik"},
    {"questionNumber": 9, "question": "9. Türkiye’nin en yüksek dağı hangisidir?", "options": ["Erciyes", "Kaçkar", "Ağrı", "Toros"], "correct": "Ağrı"},
    {"questionNumber": 10, "question": "10. Afrika kıtasında kaç ülke vardır (yaklaşık)?", "options": ["34", "44", "54", "64"], "correct": "54"}
  ],
  "Teknoloji": [
    {"questionNumber": 1, "question": "1. Python bir ... dilidir.", "options": ["Programlama", "Tasarım", "Veritabanı", "Makine"], "correct": "Programlama"},
    {"questionNumber": 2, "question": "2. HTML ne için kullanılır?", "options": ["Veritabanı yönetimi", "Web sayfası yapımı", "Donanım kontrolü", "Oyun geliştirme"], "correct": "Web sayfası yapımı"},
    {"questionNumber": 3, "question": "3. Bilgisayarın merkezi işlem birimi hangisidir?", "options": ["RAM", "GPU", "CPU", "SSD"], "correct": "CPU"},
    {"questionNumber": 4, "question": "4. İnternetin temeli hangi teknolojidir?", "options": ["Wi-Fi", "TCP/IP", "Bluetooth", "Ethernet"], "correct": "TCP/IP"},
    {"questionNumber": 5, "question": "5. Yapay zeka hangi alanla ilgilidir?", "options": ["Resim çizme", "Veri analizi ve öğrenme", "Donanım onarımı", "Ses kaydı"], "correct": "Veri analizi ve öğrenme"},
    {"questionNumber": 6, "question": "6. RAM ne işe yarar?", "options": ["Veri depolama", "Veri işleme", "Geçici bellek", "Ekran kartı görevi"], "correct": "Geçici bellek"},
    {"questionNumber": 7, "question": "7. İlk bilgisayar hangi yılda icat edilmiştir (yaklaşık)?", "options": ["1920", "1936", "1945", "1955"], "correct": "1945"},
    {"questionNumber": 8, "question": "8. JavaScript genellikle ne için kullanılır?", "options": ["Veritabanı yönetimi", "Web etkileşimi", "Donanım kontrolü", "Dosya yönetimi"], "correct": "Web etkileşimi"},
    {"questionNumber": 9, "question": "9. SSD ve HDD arasındaki fark nedir?", "options": ["Hız", "Renk", "Boyut", "Isı"], "correct": "Hız"},
    {"questionNumber": 10, "question": "10. Yapay zekada 'machine learning' ne anlama gelir?", "options": ["Makine öğrenmesi", "Veri depolama", "Donanım kontrolü", "Oyun geliştirme"], "correct": "Makine öğrenmesi"}
  ]
}

# 5) Güvenlik: verinin boş olmadığını doğrula
total_expected = sum(len(v) for v in db_quiz.values())
assert total_expected > 0, "db_quiz boş! Lütfen verileri ekleyin."

# 6) Insert
for category, questions in db_quiz.items():
    for q in questions:
        cur.execute("""
            INSERT INTO questions (category, questionNumber, question, option1, option2, option3, option4, correct)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            category,
            q["questionNumber"],
            q["question"],
            q["options"][0],
            q["options"][1],
            q["options"][2],
            q["options"][3],
            q["correct"]
        ))

conn.commit()

# 7) Doğrulama logları
cur.execute("SELECT COUNT(*) FROM questions")
count = cur.fetchone()[0]
cur.execute("SELECT category, COUNT(*) FROM questions GROUP BY category")
by_cat = cur.fetchall()

conn.close()
print(f"✔ DB path: {DB_PATH}")
print(f"✔ Toplam satır: {count}")
print(f"✔ Kategori bazında: {by_cat}")
