print("=" * 75)
print("       TRAFİK KONİSİ TESPİTİ - MODEL KARŞILAŞTIRMASI")
print("=" * 75)

print(f"{'METRİK':<18}{'İLK MODEL':<18}{'GELİŞTİRİLMİŞ MODEL':<22}")
print("-" * 75)

sonuclar = [
    ("Precision", "%93.8", "%94.9"),
    ("Recall", "%87.5", "%93.4"),
    ("mAP50", "%92.6", "%96.3"),
    ("mAP50-95", "%71.7", "%75.7")
]

for metrik, ilk, yeni in sonuclar:
    print(f"{metrik:<18}{ilk:<18}{yeni:<22}")

print("-" * 75)
print("Test verisi: 224 görüntü / 378 nesne")
print("=" * 75)