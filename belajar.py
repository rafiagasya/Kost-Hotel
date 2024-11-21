def hitung_harga():
    print("Selamat datang di Kalkulator Harga Kost/Hotel!")
    print("Pilih tipe kamar:")
    print("1. Kost Standar (Rp100.000/hari)")
    print("2. Kost Premium (Rp150.000/hari)")
    print("3. Hotel Ekonomi (Rp250.000/hari)")
    print("4. Hotel Mewah (Rp500.000/hari)")

    # Input pilihan kamar
    pilihan = int(input("Masukkan nomor tipe kamar (1-4): "))

    # Harga per hari berdasarkan tipe kamar
    harga_per_hari = {
        1: 100_000,  # Kost Standar
        2: 150_000,  # Kost Premium
        3: 250_000,  # Hotel Ekonomi
        4: 500_000   # Hotel Mewah
    }

    if pilihan not in harga_per_hari:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return

    # Input jumlah hari
    try:
        jumlah_hari = int(input("Masukkan jumlah hari menginap: "))
        if jumlah_hari <= 0:
            print("Jumlah hari harus lebih dari 0.")
            return
    except ValueError:
        print("Input jumlah hari harus berupa angka.")
        return

    # Tambahkan fasilitas tambahan
    print("\nPilih fasilitas tambahan:")
    print("1. Sarapan pagi (Rp50.000/hari)")
    print("2. Laundry (Rp20.000/hari)")
    print("3. Tidak ada tambahan")

    fasilitas = int(input("Masukkan nomor fasilitas tambahan (1-3): "))
    biaya_tambahan = 0

    if fasilitas == 1:
        biaya_tambahan = 50_000
    elif fasilitas == 2:
        biaya_tambahan = 20_000
    elif fasilitas != 3:
        print("Pilihan fasilitas tidak valid.")
        return

    # Hitung total harga
    total_harga = (harga_per_hari[pilihan] + biaya_tambahan) * jumlah_hari

    # Tambahkan diskon
    if jumlah_hari > 30:
        total_harga *= 0.8  # Diskon 20%
    elif jumlah_hari > 7:
        total_harga *= 0.9  # Diskon 10%

    print(f"\nDetail Pembayaran:")
    print(f"Tipe kamar: {pilihan} ({harga_per_hari[pilihan]:,}/hari)")
    print(f"Jumlah hari: {jumlah_hari}")
    if biaya_tambahan > 0:
        print(f"Biaya tambahan fasilitas: Rp{biaya_tambahan:,}/hari")
    print(f"Total harga (setelah diskon jika ada): Rp{total_harga:,.0f}")
    print("\nTerima kasih telah menggunakan Kalkulator Harga Kost/Hotel!")

# Jalankan program
hitung_harga()
