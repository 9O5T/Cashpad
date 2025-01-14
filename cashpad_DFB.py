import sqlite3

def database_build():
    # Veritabanı bağlantısı oluştur
    conn = sqlite3.connect('CDF.db')
    cursor = conn.cursor()

    # exam_class_one tablosunu oluştur
    cursor.execute('''CREATE TABLE IF NOT EXISTS payment_base (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date VARCHAR(20) NOT NULL,
                        user VARCHAR(20) NOT NULL,
                        type VARCHAR(20) NOT NULL,
                        status VARCHAR(20) NOT NULL,
                        info VARCHAR(20) NOT NULL,
                        payment VARCHAR(20) NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS company_data (
                        company_name VARCHAR(20) NOT NULL,
                        company_owner VARCHAR(20) NOT NULL,
                        manager_name VARCHAR(20) NOT NULL
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS sch_payments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date VARCHAR(20) NOT NULL,
                        user VARCHAR(20) NOT NULL,
                        type VARCHAR(20) NOT NULL,
                        status VARCHAR(20) NOT NULL,
                        info VARCHAR(20) NOT NULL,
                        payment VARCHAR(20) NOT NULL
                    )''')

    # Veritabanı değişikliklerini kaydet
    conn.commit()

    # Veritabanı bağlantısını kapat
    conn.close()
