# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input
- Nama: Tantri Widya Solehati
- NIM: 2225250114
- Kelas: 3F
## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.
## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py
## Tabel Keputusan
| Kategori                  | Syarat                                                                 | Contoh Masukan (Ujian, Tugas, Kehadiran) |
|---------------------------|------------------------------------------------------------------------|------------------------------------------|
| Penolakan tipe data       | Salah satu input bukan angka                                           | 80, 80, abc                              |
| Penolakan rentang ujian   | Nilai ujian < 0 atau > 100                                             | 105, 80, 90                              |
| Penolakan rentang tugas   | Nilai tugas < 0 atau > 100                                             | 80, -5, 90                               |
| Penolakan rentang hadir   | Nilai kehadiran < 0 atau > 100                                         | 80, 80, 120                              |
|Tidak memenuhi syarat hadir| Kehadiran < 80%                                                        | 90, 90, 75                               |
| Predikat A, Lulus         | Kehadiran ≥ 80 dan Nilai akhir ≥ 85                                    | 90, 80, 95                               |
| Predikat B, Lulus         | Kehadiran ≥ 80 dan 70 ≤ Nilai akhir < 85                               | 75, 70, 85                               |
| Predikat C, Lulus         | Kehadiran ≥ 80 dan 60 ≤ Nilai akhir < 70                               | 60, 60, 80                               |
| Predikat D, Belum Lulus   | Kehadiran ≥ 80 dan 50 ≤ Nilai akhir < 60                               | 55, 50, 90                               |
| Predikat E, Belum Lulus   | Kehadiran ≥ 80 dan Nilai akhir < 50                                    | 40, 30, 100                              |
## Hasil Pengujian
| Ujian | Tugas | Kehadiran | nilai akhir | Keluaran yang Diharapkan                                         | Keluaran Aktual                                 | Status  |
|-------|-------|-----------|-------------|------------------------------------------------------------------|---------------------------------------|---------|
| 90    | 80    | 95        | 86.00       | Predikat A, Lulus                                                | Predikat A, Lulus                                  | Sesuai  |
| 75    | 70    | 85        | 73.00       | Predikat B, Lulus                                                | Predikat B, Lulus                                  | Sesuai  |
| 60    | 60    | 80        | 60.00       | Predikat C, Lulus                                                | Predikat C, Lulus                                  | Sesuai  |
| 55    | 50    | 90        | 53.00       | Predikat D, Belum Lulus                                          | Predikat D, Belum Lulus                                  | Sesuai    |
| 40    | 30    | 100       | 36.00       | Predikat E, Belum Lulus                                          | Predikat E, Belum Lulus                                  | Sesuai  |
| 90    | 90    | 75        | 90.00       | Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran | Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran | Sesuai  |
| 105   | 80    | 90        | -           | Pesan penolakan rentang nilai ujian                              | Pesan penolakan rentang nilai ujian                            | Sesuai  |
| 80    | -5    | 90        | -           | Pesan penolakan rentang nilai tugas                              | Pesan penolakan rentang nilai tugas                            | Sesuai  |
| 80    | 80    | abc       | -           | Pesan penolakan tipe                                             | Pesan penolakan tipe                                   | Sesuai  |
## Refleksi
1. Masalah
Program awal hanya memeriksa apakah input bisa dikonversi ke angka (float). Akibatnya, masukan dengan simbol tambahan seperti "80%" langsung ditolak dengan pesan umum "seluruh data harus berupa angka", tanpa menjelaskan kesalahan format.
2. Perbaikan
```bash
if not teks_hadir.replace(".", "").isdigit():
    print("Masukan ditolak: kehadiran harus berupa angka tanpa simbol.")
else:
    hadir = float(teks_hadir)

3. Dengan begitu, input "80%" ditolak dengan pesan khusus, sedangkan "80" atau "80.5" tetap diterima.