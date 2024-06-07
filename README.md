Duygu Analizi Projesi - Dağıtım Kılavuzu
Bu kılavuzda, duygu analizi projesini başka bir bilgisayara dağıtma adımlarını bulacaksınız. Proje, duygu analizi modelini eğitmek, bir FastAPI servisi oluşturmak ve bir kullanıcı arayüzü sağlamak için Python kullanılarak geliştirilmiştir.

İçindekiler
Literatür ve Makale Araştırmaları
DataSet, Veri Özellikleri ve Ön İşleme
Modelleme, Test ve Doğrulama
Dağıtım Adımları
Literatür ve Makale Araştırmaları
Duygu analizi, metin tabanlı duygusal içeriğin otomatik olarak tanınması ve sınıflandırılması için kullanılan bir makine öğrenimi alt dalıdır. Projenin temelinde, bu alanda yayınlanan makalelerden ve literatürden elde edilen bilgiler kullanılmıştır.

DataSet, Veri Özellikleri ve Ön İşleme
Projede kullanılan veri kümesi, Türkçe duygu analizi için çeşitli duygusal etiketlere sahip metin örneklerinden oluşur. Veri kümesi, temizlenme ve özellik mühendisliği adımlarından geçirilmiştir. Metinlerdeki gereksiz öğeler (örneğin, URL'ler, kullanıcı adları) kaldırılmış ve metinler BERT modeli tarafından işlenebilmesi için önceden işlenmiştir.

Modelleme, Test ve Doğrulama
Model, Türkçe duygu analizi için BERT tabanlı bir modeldir. Model eğitimi, doğrulama ve test işlemleri Python kullanılarak gerçekleştirilmiştir. Eğitim ve test süreçleri boyunca, modelin performansını değerlendirmek için çeşitli metrikler kullanılmıştır.

Dağıtım Adımları
Gerekli Kütüphanelerin Yüklenmesi: Projeyi çalıştırmak için gerekli olan Python kütüphanelerini yükleyin. Bunlar arasında FastAPI, Transformers, ve diğer bağımlılıklar bulunabilir.

Modelin ve Servis Kodunun Kopyalanması: Modelinizi ve servis kodunu hedef bilgisayara kopyalayın. Model dosyasını ve main.py gibi servis dosyalarını doğru dizinlere yerleştirin.

Gerekli Kütüphanelerin Kurulumu: Hedef bilgisayarda Python ortamını kurun ve gerekli kütüphaneleri yükleyin. Bunlar arasında FastAPI, Transformers ve diğer bağımlılıklar bulunabilir.

Servisin Başlatılması: Python terminalinde veya komut istemcisinde servisi başlatmak için uygun komutları çalıştırın. Örneğin, uvicorn main:app --host=127.0.0.1 --port=8000 komutunu kullanarak FastAPI servisini başlatabilirsiniz.

Kullanıcı Arayüzünün Erişimi: Tarayıcınızda veya uygun bir HTTP istemcisi kullanarak servise erişin. Servisin URL'sini ve kullanım talimatlarını belirtin.
