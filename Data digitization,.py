import pandas as pd

# Excel dosyasının yolunu ve adını belirtin
excel_path = r"C:\Users\akgul\OneDrive\Masaüstü\veri yeni.xlsx"

# Excel dosyasını oku
df = pd.read_excel(excel_path)

# Her bir hücre tipi için numaralandırma işlemini yap
numaralar = {}
numara = 1
for indeks, satır in df.iterrows():
    for sütun, değer in satır.items():
        if pd.notna(değer):  # Boş hücreleri atla
            tip = type(değer)
            if tip not in numaralar:
                numaralar[tip] = {}
            if değer not in numaralar[tip]:
                numaralar[tip][değer] = numara
                numara += 1
            df.at[indeks, sütun] = numaralar[tip][değer]

# Numaralandırılmış veriyi yeni bir Excel dosyasına yaz
df.to_excel(r"C:\Users\akgul\OneDrive\Masaüstü\output veri.xlsx", index=False)
