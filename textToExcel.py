import openpyxl

txt_dosya_yolu = "C:/Users/Cengiz/Desktop/ResearchGate/ResearchGatePullData/veriler.txt"
excel_dosya_yolu = "C:/Users/Cengiz/Desktop/ResearchGate/ResearchGatePullData/veri.xlsx"

# Txt dosyasını oku
with open(txt_dosya_yolu, "r", encoding="utf-8") as file:
    satirlar = file.readlines()

# Veri setlerini birleştirmek
veri_setleri = []
aktif_veri = []

for satir in satirlar:
    satir = satir.strip()
    if satir:  # Boş olmayan satırları al
        aktif_veri.append(satir)
    else:  # Boş satırlar veri setlerini ayırır
        if aktif_veri:
            veri_setleri.append(aktif_veri)
            aktif_veri = []

if aktif_veri:  # Dosyanın sonundaki veriyi ekler
    veri_setleri.append(aktif_veri)

# Excel dosyasını oluştur
workbook = openpyxl.Workbook()
worksheet = workbook.active

basliklar_eklendi = False  # Başlıklar henüz eklenmedi

# Veriyi uygun formatta düzenleme
for veri_seti in veri_setleri:
    isim = veri_seti[0]
    publications = veri_seti[1]
    reads = veri_seti[3]
    citations = veri_seti[5]

    if not basliklar_eklendi:  # Başlıklar henüz eklenmediyse ekle
        basliklar = ["Name", "Publications", "Reads", "Citations"]
        worksheet.append(basliklar)
        basliklar_eklendi = True

    veri = {
        'Name': isim,
        'Publications': publications,
        'Reads': reads,
        'Citations': citations
    }

    row = [veri['Name'], veri['Publications'], veri['Reads'], veri['Citations']]
    worksheet.append(row)

# Excel dosyasını kaydet
workbook.save(excel_dosya_yolu)

print("Excel dosyası oluşturuldu:", excel_dosya_yolu)
