# AI-TraderX

AI-TraderX, borsada otomatik işlem yapmak için tasarlanmış bir yapay zeka aracıdır. Geçmiş fiyat verileri ve çeşitli teknik göstergeleri kullanarak, AI-TraderX, gelecekteki fiyat hareketleri hakkında tahminler yapabilir ve bu tahminlere dayalı olarak işlemler açabilir.

AI-TraderX, hem yeni hem de deneyimli yatırımcılar için uygundur. Yeni yatırımcılar, AI-TraderX'in otomatik işlem yapma yeteneklerinden yararlanarak, piyasayı takip etmek ve doğru zamanda işlemler açmak için gereken zaman ve çabadan tasarruf edebilirler. Deneyimli yatırımcılar, AI-TraderX'in kendi stratejilerini geliştirmek ve test etmek için kullanabilirler.

AI-TraderX, ücretsiz olarak kullanılabilir. Ancak, daha gelişmiş özellikler için bir premium abonelik satın alınabilir.

## Nasıl kullanılır?

AI-TraderX'i kullanmak için, öncelikle bir hesap oluşturmanız ve bir depo yatırmanız gerekir. Ardından, AI-TraderX'e işlem yapmak istediğiniz varlıkları seçebilirsiniz. AI-TraderX, geçmiş fiyat verileri ve çeşitli teknik göstergeleri kullanarak, gelecekteki fiyat hareketleri hakkında tahminler yapabilir ve bu tahminlere dayalı olarak işlemler açabilir.

## Kurulum

1. Projeyi klonlayın veya indirin:
`git clone https://github.com/senanurpaksoy/AI-TraderX.git`

2. Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:
`pip install -r requirements.txt`

## Veritabanı Yapılandırması

Proje, MongoDB veritabanını kullanmaktadır.

- MongoDB bağlantı ayarları
- Veritabanı tabloları ve alanları

## Lisans

Proje lisans bilgilerini ve kullanım şartlarını belirtmek için bu bölümü düzenleyin:

- Lisans türü ve bağlantı
- Diğer lisans veya kullanım gereksinimleri

---
## Sınıflar
### AppTime 
 * Uygulamanın zaman çizelgesini belirliyor. Ülkelerin borsalarını kullanacaksak aktif şekilde zaman kullanmalıyız. yani UTC+4 de olan ülke 10 da başlayacak kron. Tabi ilke deneme 10-18 arası uygulamadım.
### Regression 
 * Makine tahmin algoritmalarımız burada duracak. Buradan dağıtacağız diğer sınıflara.
### StockData 
 * İnternetten çekilen verilerin kontrol mekanizmaları
### db_transactions 
 * Database işlemlerimizi buradan yapacağız.

Detaylı Bilgi için [Notes/Todo.txt](Notes/Todo.txt) bakınız


## Özellikler

* Geçmiş fiyat verileri ve çeşitli teknik göstergeleri kullanarak, gelecekteki fiyat hareketleri hakkında tahminler yapar.
* Bu tahminlere dayalı olarak işlemler açar.
* Hem yeni hem de deneyimli yatırımcılar için uygundur.
* Ücretsiz olarak kullanılabilir.
* Daha gelişmiş özellikler için bir premium abonelik satın alınabilir.

## Avantajlar

* Zaman ve çabadan tasarruf sağlar.
* Piyasayı takip etmek için gereken uzmanlık gerektirmez.
* Kendi stratejilerinizi geliştirmek ve test etmek için kullanabilirsiniz.
* Ücretsiz olarak kullanılabilir.

## Sonuç

AI-TraderX, borsada otomatik işlem yapmak için tasarlanmış bir yapay zeka aracıdır. Geçmiş fiyat verileri ve çeşitli teknik göstergeleri kullanarak, AI-TraderX, gelecekteki fiyat hareketleri hakkında tahminler yapabilir ve bu tahminlere dayalı olarak işlemler açabilir. AI-TraderX, hem yeni hem de deneyimli yatırımcılar için uygundur. Yeni yatırımcılar, AI-TraderX'in otomatik işlem yapma yeteneklerinden yararlanarak, piyasayı takip etmek ve doğru zamanda işlemler açmak için gereken zaman ve çabadan tasarruf edebilirler. Deneyimli yatırımcılar, AI-TraderX'in kendi stratejilerini geliştirmek ve test etmek için kullanabilirler.
