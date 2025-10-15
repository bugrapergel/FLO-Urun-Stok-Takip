import data_manager

def generate_report():
    """Tüm ürünlerin stok raporunu oluşturur."""
    products = data_manager.load_products()
    print("\n--- FLO Ürün Stok Raporu ---")
    if not products:
        print("Envanterde hiç ürün bulunmamaktadır.")
        return
    for name, details in products.items():
        print(f"Ürün Adı: {name}, Stok: {details['stock']}, Fiyat: {details['price']} TL")
    print("-----------------------------\n")