# --- Program Utama ---

def main_menu():
    """Fungsi untuk menampilkan menu utama dan mengatur alur program."""
    
    # Kita butuh variabel untuk menyimpan target, karena fungsi scan belum jadi
    target_ip = None
    gateway_ip = "192.168.1.1" # Ganti ini jika gateway Anda berbeda

    while True:
        print("\n" + "="*20)
        print("   WiFi Rakus v0.1")
        print("="*20)
        print("1. Pindai Jaringan (Scan Network)")
        print("2. Mulai Batasi Kecepatan (Start Throttling)")
        print("3. Hentikan Pembatasan (Stop)")
        print("4. Keluar (Exit)")
        print(f"[*] Target saat ini: {target_ip or 'Belum ada'}")
        
        choice = input(">> Pilih opsi (1-4): ")

        if choice == '1':
            print("\n[!] Maaf, fungsi scan belum diimplementasikan.")
            # Di masa depan, di sini kita akan memanggil fungsi scan_network()
            # dan hasilnya akan disimpan ke variabel target_ip
            scan_network() 

        elif choice == '2':
            if target_ip is None:
                # Minta IP target secara manual karena scan belum bisa
                target_ip = input("[?] Masukkan IP target yang akan dilambatkan: ")
            
            down_limit = input("[?] Masukkan batas kecepatan download (kbps, cth: 256): ")
            up_limit = input("[?] Masukkan batas kecepatan upload (kbps, cth: 128): ")

            try:
                # Panggil fungsi untuk mulai serangan
                start_throttling(target_ip, gateway_ip, down_limit, up_limit)
                print("\n[+] Pembatasan kecepatan sedang berjalan di background.")
                print("[!] Pilih opsi '3' untuk menghentikannya.")
            except Exception as e:
                print(f"[!] Gagal memulai serangan: {e}")

        elif choice == '3':
            # Panggil fungsi untuk menghentikan serangan
            stop_throttling()

        elif choice == '4':
            print("[+] Terima kasih telah menggunakan tools ini. Memastikan jaringan kembali normal...")
            stop_throttling() # Pastikan semua serangan berhenti sebelum keluar
            break

        else:
            print("[!] Pilihan tidak valid, silakan coba lagi.")
            time.sleep(1)

# Pastikan program utama hanya berjalan saat script dieksekusi langsung
if __name__ == "__main__":
    # Peringatan penting sebelum menjalankan
    print("="*50)
    print("PERINGATAN: Tools ini memerlukan hak akses ROOT dan")
    print("paket 'nmap', 'dsniff', dan 'wondershaper'.")
    print("Gunakan hanya untuk tujuan edukasi pada jaringan Anda sendiri.")
    print("="*50)
    
    # Cek hak akses root (sederhana)
    if os.geteuid() != 0:
        print("[!] FATAL: Script ini harus dijalankan sebagai root!")
        exit()

    main_menu()