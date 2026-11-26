# TEKNOFEST İKA – Bilgisayarlı Görü

İnsansız Kara Aracı (İKA) projesi kapsamında YOLO tabanlı nesne tespiti çalışmaları.

## Proje Hakkında

Bu projede İKA'nın parkur üzerindeki trafik konilerini algılayabilmesi amacıyla YOLO kullanılarak nesne tespit modeli geliştirilmiştir.

Uzak mesafedeki konilerin algılanmasını iyileştirmek amacıyla iki farklı veri seti birleştirilmiş ve model yeniden eğitilmiştir.

## Yapılan Çalışmalar

- Trafik konisi veri setinin hazırlanması.
- İlk YOLO modelinin eğitilmesi.
- Uzak mesafe koni veri setinin hazırlanması.
- İki veri setinin birleştirilmesi.
- Geliştirilmiş modelin eğitilmesi.
- Modellerin aynı test veri seti üzerinde karşılaştırılması.
- Video üzerinden tespit testi yapılması.

## Model Karşılaştırması

| Metrik | İlk Model | Geliştirilmiş Model |
|---|---:|---:|
| Precision | %93.8 | %94.9 |
| Recall | %87.5 | %93.4 |
| mAP50 | %92.6 | %96.3 |
| mAP50-95 | %71.7 | %75.7 |

**Test verisi:** 224 görüntü / 378 nesne.

## Kullanılan Teknolojiler

- Python
- YOLOv8
- Ultralytics
- PyTorch
- OpenCV
- Roboflow

## Veri Setleri ve Lisanslar

**1. Persedatasetrealcones – Sürüm 1**

Kaynak: https://universe.roboflow.com/rique01101999-gmail-com/persedatasetrealcones/dataset/1

Lisans: CC BY 4.0

**2. Traffic Cones – Sürüm 2**

Kaynak: https://universe.roboflow.com/robotica-xftin/traffic-cones-4laxg/dataset/2

Lisans: Public Domain (Roboflow proje sayfasında belirtilen lisans).

Veri setleri birleştirilerek geliştirilmiş eğitim verisi oluşturulmuştur.

## Proje Durumu

Trafik konisi tespiti için model eğitimi ve video testleri tamamlanmıştır. Gerçek İKA kamerası ile testler ilerleyen aşamada yapılacaktır.

## Geliştirici Ortamı

- NVIDIA RTX 5070 Laptop GPU
- Python 3.12
- Ultralytics YOLO 8.4

## Results

### Cone Detection Test
![Cone Detection](results/cone_detection_video_test.png)

### Model Performance Comparison
![Model Comparison](results/model_performance_comparison.png)
