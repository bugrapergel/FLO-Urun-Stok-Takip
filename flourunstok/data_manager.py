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