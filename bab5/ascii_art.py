from PIL import Image

# 1. Daftar karakter ASCII dari yang paling padat (gelap) ke paling renggang (terang)
# Anda bisa memodifikasi string ini untuk hasil yang berbeda
CHAR_ASCII = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def konversi_ke_ascii(jalur_gambar, lebar_baru=100):
    try:
        # Buka gambar
        img = Image.open(jalur_gambar)
    except Exception as e:
        print(f"Gagal membuka gambar. Error: {e}")
        return

    # 2. Hitung tinggi baru agar proporsi gambar tetap terjaga
    # Karakter teks biasanya lebih tinggi daripada lebarnya, jadi kita kalikan 0.55
    lebar_asli, tinggi_asli = img.size
    rasio = tinggi_asli / lebar_asli
    tinggi_baru = int(lebar_baru * rasio * 0.55)
    
    # Ubah ukuran dan ubah mode gambar menjadi Grayscale ('L')
    img = img.resize((lebar_baru, tinggi_baru))
    img = img.convert('L')
    
    # Ambil data piksel gambar (berupa angka 0 - 255)
    data_piksel = img.getdata()
    
    # 3. PERULANGAN UTAMA: Mengubah setiap piksel menjadi karakter ASCII
    karakter_hasil = []
    for piksel in data_piksel:
        # Memetakan nilai 0-255 ke dalam 11 pilihan karakter di list CHAR_ASCII
        indeks_karakter = piksel // 25
        # Antisipasi agar indeks tidak melebihi panjang list
        if indeks_karakter >= len(CHAR_ASCII):
            indeks_karakter = len(CHAR_ASCII) - 1
        karakter_hasil.append(CHAR_ASCII[indeks_karakter])
        
    # Gabungkan semua karakter menjadi string utuh
    string_ascii = "".join(karakter_hasil)
    
    # 4. Memotong string menjadi baris-baris sesuai dengan lebar gambar
    jumlah_karakter = len(string_ascii)
    gambar_ascii = "\n".join([string_ascii[i:(i + lebar_baru)] for i in range(0, jumlah_karakter, lebar_baru)])
    
    return gambar_ascii

# --- CARA MENGGUNAKAN ---
# Ganti "foto_anda.jpg" dengan nama file gambar yang ada di folder yang sama
nama_file = "foto_anda.jpg" 
hasil_ascii = konversi_ke_ascii(nama_file, lebar_baru=80)

if hasil_ascii:
    print(hasil_ascii)
    
    # Opsional: Simpan hasilnya ke dalam file teks (.txt)
    with open("hasil_art.txt", "w") as f:
        f.write(hasil_ascii)
    print("\nHasil telah disimpan ke 'hasil_art.txt'")
