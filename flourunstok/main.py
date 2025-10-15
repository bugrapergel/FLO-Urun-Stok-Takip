import json
import os

DATA_DIR = 'data'
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.json')


def create_data_dir():
    """Veri klasörünü oluşturur."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def load_products():
    """JSON dosyasından ürün verilerini yükler."""
    if not os.path.exists(PRODUCTS_FILE):
        return {}
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_products(products):
    """Ürün verilerini JSON dosyasına kaydeder."""
    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)


def add_product(name, stock, price):
    """Yeni bir ürün ekler."""
    products = load_products()
    products[name] = {"stock": stock, "price": price}
    save_products(products)
    print(f"'{name}' ürünü başarıyla eklendi.")


def update_stock(name, new_stock):
    """Bir ürünün stok miktarını günceller."""
    products = load_products()
    if name in products:
        products[name]["stock"] = new_stock
        save_products(products)
        print(f"'{name}' ürününün stoğu {new_stock} olarak güncellendi.")
    else:
        print(f"'{name}' ürünü bulunamadı.")


def generate_report():
    """Tüm ürünlerin stok raporunu oluşturur."""
    products = load_products()
    print("\n--- FLO Ürün Stok Raporu ---")
    if not products:
        print("Envanterde hiç ürün bulunmamaktadır.")
        return
    for name, details in products.items():
        print(f"Ürün Adı: {name}, Stok: {details['stock']}, Fiyat: {details['price']} TL")
    print("-----------------------------\n")


def main_menu():
    """Ana menüyü gösterir ve kullanıcıdan işlem seçmesini ister."""
    while True:
        print("\n### FLO Mağaza Yönetim Sistemi ###")
        print("1. Ürün Ekle")
        print("2. Stok Güncelle")
        print("3. Rapor Oluştur")
        print("4. Çıkış")

        choice = input("Lütfen bir işlem seçin: ")

        if choice == '1':
            name = input("Ürün adını girin: ")
            stock = int(input("Stok miktarını girin: "))
            price = float(input("Fiyatını girin: "))
            add_product(name, stock, price)
        elif choice == '2':
            name = input("Güncellenecek ürün adını girin: ")
            new_stock = int(input("Yeni stok miktarını girin: "))
            update_stock(name, new_stock)
        elif choice == '3':
            generate_report()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    create_data_dir()
    main_menu()