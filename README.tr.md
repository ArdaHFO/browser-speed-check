Bu proje, bir web tarayıcısının indirme, yükleme ve bağlantı gecikmesini nasıl ölçtüğünü araştırır.

<h1 align="center">Browser Network Lab</h1>

<p align="center"><strong>Aktarımı izle. Zamanlamayı anla.</strong></p>
<p align="center">Tarayıcı tarafında indirme, yükleme ve HTTP gidiş-dönüş sürelerini inceleyen eğitsel Flask ve JavaScript prototipi.</p>

<p align="center">
  <a href="README.md">English</a> · <strong>Türkçe</strong><br />
  <a href="#yerel-arayüzü-çalıştır"><strong>Yerel arayüzü çalıştır</strong></a> ·
  <a href="#projede-neler-var">Özellikler</a> ·
  <a href="#doğrulama-ve-mevcut-sınırlar">Mevcut sınırlar</a>
</p>

---

Browser Network Lab, zamanlama mantığını tarayıcıda çalıştırır. JavaScript istekleri başlatır, geçen süreyi kaydeder ve aktarım boyutu ile süre alanlarını gösterir. Flask ise sayfayı ve küçük bir uç nokta grubunu sunar.

**Bu, bir ders prototipidir ve doğrulanmış bant genişliği ölçüm aracı değildir.** İlk proje belgesi Kasım 2023 tarihli teslim süresini kaydeder. Ayrı bir proje olan [Network Transfer Lab](https://github.com/ArdaHFO/network-transfer-lab), tarayıcı arayüzünün yanında sunucu tarafındaki aktarımları inceler.

## Yerel arayüzü çalıştır

| Gereksinim | Amaç |
| --- | --- |
| pip ve venv içeren Python 3 | Geliştirme ortamı |
| Flask 3.0.0 | Sunucu ve Jinja şablonları |
| JavaScript destekli tarayıcı | İstek zamanlaması ve sonuç gösterimi |

```text
git clone https://github.com/ArdaHFO/browser-network-lab.git
cd browser-network-lab
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir ve çalıştır.

```text
python -m pip install Flask==3.0.0
python -m flask --app app run --host 127.0.0.1 --port 8000
```

[localhost:8000](http://127.0.0.1:8000) adresini aç. CLI, 8000 numaralı portta yerel önizleme başlatır. Uygulamanın ana başlatıcısı da debug kapalı ve yalnızca yerel erişimle çalışacak şekilde tanımlıdır.

Bu sürümün uygulama kodu yalnızca Flask'ı içe aktarır. [requirements.txt](requirements.txt), uygulama dosyalarının çağırmadığı speedtest-cli dahil daha geniş bir geçmiş ortam kaydını korur.

## Projede neler var?

- **Tarayıcıda zamanlama.** İndirme ve yükleme kontrolleri XMLHttpRequest ile tarayıcıda geçen süreyi kullanır.
- **Aktarım boyutu gösterimi.** Biçimlendirme işlevi, boyutları sonuçların yanında okunabilir birimlere dönüştürür.
- **HTTP gidiş-dönüş süresi.** `GET /ping`, istek süresi deneyi için `Pong` yanıtını verir.
- **Küçük Flask yapısı.** Ana sayfa, alternatif `/views/` sayfası ve bayt sayan yükleme işleyicisi bulunur.
- **Yerel örnek dosyalar.** Geliştirme için görseller ve statik aktarım dosyaları yer alır.

## Deneyin işleyişi

| Arayüz eylemi | İstek | Mevcut kaynak davranışı |
| --- | --- | --- |
| İndir | `GET /download` | Paketlenmiş `20MB.png` dosyasını önbelleksiz sunar |
| Yükle | `POST /upload` | Uygulama dosyası kaydetmeden alınan bayt sayısını döndürür |
| Ping | `GET /ping` | Kısa HTTP yanıtı döndürür |
| Yenile | Sayfa yenileme | Sayfayı sıfırlar |

HTTP gidiş-dönüş süresi, tarayıcıdan uygulamaya gecikmeyi ölçer. Ağ aktarımı dışındaki süreleri de içerir ve ICMP ping değildir. Yerel sunucu ağırlıklı olarak yerel bağlantıyı sınar.

## Doğrulama ve mevcut sınırlar

Kaynak statik olarak incelendi. Bu değişiklikler için uygulama, otomatik test, aktarım ölçümü veya performans deneyi çalıştırılmadı.

- İndirme zamanlaması paketlenmiş `20MB.png` dosyasının gerçek bayt boyutunu kullanır. Hesaplar geçen saniyeyi ve ondalık Mbps dönüşümünü temel alır. Başarısız HTTP yanıtları sonuç olarak gösterilmez.
- Yükleme ucu POST kabul eder, dosyanın varlığını denetler ve alınan bayt sayısını doğrular. Multipart ek yükü dahil toplam istek 32 MiB ile sınırlıdır. Uygulama dosyası kaydedilmez.
- İndirme ve ping yanıtlarında önbellekleme kapatılır. İstek zaman aşımları ve tarayıcı hata mesajları kodda yer alır, ancak çalıştırılarak doğrulanmadı.
- Ölçümler tarayıcı ile Flask arasındaki yolu tanımlar. Localhost kullanıldığında internet sağlayıcısının hızını değil, yerel aktarımı inceler.
- Tarayıcı süresi HTTP ve uygulama ek yükünü de içerir. Doğruluk ve tekrarlanabilirlik kontrollü ölçümler gerektirir.

Tarihsel genel IP adresleri ve eski dosya boyutu verimliliği iddiaları güncel dağıtım veya ölçüm güvencesi değildir.

## Proje yapısı

```text
app.py                 Flask sayfası, indirme, yükleme ve ping rotaları
views.py               Alternatif sayfa rotası
templates/index.html   Tarayıcı zamanlaması ve boyut biçimlendirici
static/                Mevcut aktarım örnekleri
image/                 Ek görsel ve HTML deneyi
requirements.txt       Geçmiş bağımlılık kaydı
```

## Geliştirme ve katkı

Değişiklikleri tek bir ölçüm yoluna odakla. Hata bildirimine istenen URL'yi, HTTP durumunu, dosya boyutunu ve beklenen hesabı ekle. Arayüz kontrolleriyle gerçek ağ ölçümlerini ayır. Yükleme desteğini geliştirirken hassas olmayan dosyalar kullan.

## Lisans ve kaynaklar

[MIT lisansı](LICENSE) ile dağıtılır. Python, Flask ve tanımlanan bağımlılıklar kendi lisanslarına tabidir.
