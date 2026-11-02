<h1 align="center">Speedtest-1</h1>

<p align="center"><strong>Aktarımı izle. Zamanlamayı anla.</strong></p>
<p align="center">Tarayıcı tarafında indirme, yükleme ve HTTP gidiş-dönüş sürelerini inceleyen eğitsel Flask ve JavaScript prototipi.</p>

<p align="center">
  <a href="README.md">English</a> · <strong>Türkçe</strong><br />
  <a href="#yerel-arayüzü-çalıştır"><strong>Yerel arayüzü çalıştır</strong></a> ·
  <a href="#projede-neler-var">Özellikler</a> ·
  <a href="#doğrulama-ve-mevcut-sınırlar">Mevcut sınırlar</a>
</p>

---

Speedtest-1, zamanlama mantığını tarayıcıda çalıştırır. JavaScript istekleri başlatır, geçen süreyi kaydeder ve aktarım boyutu ile süre alanlarını gösterir. Flask ise sayfayı ve küçük bir uç nokta grubunu sunar.

**Bu, tamamlanmamış bir ders prototipidir ve doğrulanmış bant genişliği ölçüm aracı değildir.** İlk proje belgesi Kasım 2023 tarihli teslim süresini kaydeder. Önceki README aynı adı kullansa da bu repo, [speedtestFinal](https://github.com/ArdaHFO/speedtestFinal) projesinden ayrı bir uygulamadır.

## Yerel arayüzü çalıştır

| Gereksinim | Amaç |
| --- | --- |
| pip ve venv içeren Python 3 | Geliştirme ortamı |
| Flask 3.0.0 | Sunucu ve Jinja şablonları |
| JavaScript destekli tarayıcı | İstek zamanlaması ve sonuç gösterimi |

```text
git clone https://github.com/ArdaHFO/speedtest-1.git
cd speedtest-1
python -m venv .venv
```

Windows Komut İstemi'nde `.venv\Scripts\activate`, macOS/Linux'ta `source .venv/bin/activate` ile ortamı etkinleştir ve çalıştır.

```text
python -m pip install Flask==3.0.0
python -m flask --app app run --host 127.0.0.1 --port 8000
```

[localhost:8000](http://127.0.0.1:8000) adresini aç. CLI, betikteki tüm ağ arayüzlerini dinleyen 80 numaralı port ve debug ayarlarını kullanmadan yerel önizleme başlatır. Sayfa incelenebilir, ancak aktarım kontrollerinde aşağıdaki sınırlamalar vardır.

Bu sürümün uygulama kodu yalnızca Flask'ı içe aktarır. [requirements.txt](requirements.txt), uygulama dosyalarının çağırmadığı speedtest-cli dahil daha geniş bir geçmiş ortam kaydını korur.

## Projede neler var?

- **Tarayıcıda zamanlama.** İndirme ve yükleme kontrolleri XMLHttpRequest ile tarayıcıda geçen süreyi kullanır.
- **Aktarım boyutu gösterimi.** Biçimlendirme işlevi, boyutları sonuçların yanında okunabilir birimlere dönüştürür.
- **HTTP gidiş-dönüş süresi.** `GET /ping`, istek süresi deneyi için `Pong` yanıtını verir.
- **Küçük Flask yapısı.** Ana sayfa, alternatif `/views/` sayfası ve tamamlanmamış yükleme işleyicisi bulunur.
- **Yerel örnek dosyalar.** Geliştirme için görseller ve statik aktarım dosyaları yer alır.

## Deneyin işleyişi

| Arayüz eylemi | İstek | Mevcut kaynak davranışı |
| --- | --- | --- |
| İndir | `GET static/100MB.png` | İstenen dosya yok |
| Yükle | `POST /upload` | Sunucu rotası yalnızca GET kabul eder |
| Ping | `GET /ping` | Kısa HTTP yanıtı döndürür |
| Yenile | Sayfa yenileme | Sayfayı sıfırlar |

HTTP gidiş-dönüş süresi, tarayıcıdan uygulamaya gecikmeyi ölçer. Ağ aktarımı dışındaki süreleri de içerir ve ICMP ping değildir. Yerel sunucu ağırlıklı olarak yerel bağlantıyı sınar.

## Doğrulama ve mevcut sınırlar

Kaynak dosyaları, rota tanımları, şablon istekleri ve repodaki örnek dosyalar incelendi. Aktarım ölçümü veya çalışma zamanı entegrasyon testi yapılmadı.

- Şablon `static/100MB.png` dosyasını ister. Repodaki statik dosyalar ise `static/20MB.png` ve `static/100MB.zip` şeklindedir. Dosya adı, gerçek aktarım boyutunu kanıtlamaz.
- Yükleme işleyicisinde `request` içe aktarılmaz, tarayıcının gönderdiği POST yöntemi kabul edilmez ve repoda bulunmayan `uploads/` klasörü beklenir.
- Süre dönüşüm sabitleri ve bayttan bite dönüşüm, gösterilen Mbps birimleriyle tutarlı değildir. İndirme hesabı varsayılan boyut ve yanıt metninin uzunluğunu da kullanır.
- Tarayıcı, hesaplamadan önce HTTP durumunu denetlemediğinden hata yanıtından sonra da sonuç gösterebilir.
- Önceki belgelerdeki genel IP adresi, Python beta sürümü ve 20 MB verimlilik iddiası tarihsel notlardır. Güncel dağıtım veya ölçüm güvencesi değildir.

Anlamlı ölçümler için önce bu yolların düzeltilmesi ve aritmetiğin doğrulanması gerekir. Gelecekteki ölçümler gerçek bayt sayısını, geçen saniyeyi, önbellek koşullarını ve tekrarları belirtmelidir.

## Proje yapısı

```text
app.py                 Flask sayfası, ping ve eksik yükleme rotası
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

