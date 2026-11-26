
import shutil
from pathlib import Path

# Kaynak klasörler
eski = Path("../traffic_cone_dataset")
yeni = Path("../uzak_koni_veriseti")
hedef = Path(".")

kaynaklar = [
    ("eski", eski),
    ("yeni", yeni)
]

uzantilar = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

for bolum in ["train", "valid", "test"]:
    for tur in ["images", "labels"]:
        (hedef / bolum / tur).mkdir(parents=True, exist_ok=True)

for ad, kaynak in kaynaklar:
    for bolum in ["train", "valid", "test"]:

        image_dir = kaynak / bolum / "images"
        label_dir = kaynak / bolum / "labels"

        if not image_dir.exists() or not label_dir.exists():
            raise FileNotFoundError(f"Klasor eksik: {kaynak / bolum}")

        for resim in image_dir.iterdir():

            if resim.suffix.lower() not in uzantilar:
                continue

            etiket = label_dir / (resim.stem + ".txt")

            if not etiket.exists():
                raise FileNotFoundError(f"Etiket bulunamadi: {etiket}")

            yeni_resim_adi = ad + "_" + resim.name
            yeni_etiket_adi = ad + "_" + etiket.name

            shutil.copy2(
                resim,
                hedef / bolum / "images" / yeni_resim_adi
            )

            shutil.copy2(
                etiket,
                hedef / bolum / "labels" / yeni_etiket_adi
            )

# Yeni data.yaml
(hedef / "data.yaml").write_text(
    "train: train/images\n"
    "val: valid/images\n"
    "test: test/images\n\n"
    "nc: 1\n"
    "names: ['cone']\n",
    encoding="utf-8"
)

print("\nBIRLESTIRME TAMAMLANDI!")

for bolum in ["train", "valid", "test"]:
    sayi = len(list((hedef / bolum / "images").iterdir()))
    print(bolum, ":", sayi, "görüntü")
