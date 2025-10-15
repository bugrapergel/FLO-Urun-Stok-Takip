

# **FLO Ürün Stok Takip ve Raporlama Sistemi**

Bu proje, bir perakende mağazası için geliştirilmiş, basit bir konsol tabanlı stok takip ve raporlama uygulamasıdır. `main.py` dosyasını çalıştırarak bir menü üzerinden ürün ekleme, stok güncelleme ve mevcut envanterin raporunu oluşturma gibi temel işlemleri gerçekleştirebilirsiniz.

## **Proje Özellikleri**

  * **Ürün Yönetimi:** Yeni ürünler ekleme ve mevcut ürünlerin stoklarını güncelleme.
  * **Envanter Takibi:** Ürünlerin anlık stok durumunu takip etme.
  * **Raporlama:** Tüm ürünlerin güncel stok ve fiyat bilgilerini listeleyen bir rapor oluşturma.

## **Kullanılan Teknolojiler**

  * **Python:** Projenin ana programlama dilidir.
  * **JSON:** Ürün verilerini depolamak için hafif ve taşınabilir bir format olan JSON kullanılmıştır.

## **Kurulum ve Kullanım**

1.  Bu depoyu yerel makinenize klonlayın:
    ```bash
    git clone https://github.com/KullaniciAdin/flo-urun-stok-takip-sistemi.git
    ```
2.  Proje klasörüne gidin:
    ```bash
    cd flo-urun-stok-takip-sistemi
    ```
3.  Uygulamayı çalıştırmak için `main.py` dosyasını terminalden çalıştırın:
    ```bash
    python main.py
    ```

Uygulama, çalıştırıldığında bir `data` klasörü ve içinde `products.json` dosyasını otomatik olarak oluşturur.

## **Gelecek Planları**

Bu proje, temel işlevselliği sergilemek üzere tasarlanmıştır. Gelecekte, bir veritabanı sistemi (örneğin SQL) entegrasyonu ve daha gelişmiş bir kullanıcı arayüzü (GUI) eklenerek daha kapsamlı bir hale getirilebilir.
