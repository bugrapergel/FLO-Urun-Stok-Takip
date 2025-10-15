import data_manager
import reporter


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
            data_manager.add_product(name, stock, price)
        elif choice == '2':
            name = input("Güncellenecek ürün adını girin: ")
            new_stock = int(input("Yeni stok miktarını girin: "))
            data_manager.update_stock(name, new_stock)
        elif choice == '3':
            reporter.generate_report()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    data_manager.create_data_dir()
    main_menu()