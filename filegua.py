import os

def load_books(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_books(filename, books):
    with open(filename, 'w') as file:
        for book in books:
            file.write(book + '\n')

def display_books(books, index=0):
    if index < len(books):
        print(f"{index + 1}. {books[index]}")
        display_books(books, index + 1)

def add_book(books, book):
    books.append(book)

def remove_book(books, index):
    if 0 <= index < len(books):
        books.pop(index)

def main():
    filename = 'books.txt'
    books = load_books(filename)

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Buku")
        print("4. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            book = input("Masukkan nama buku: ")
            add_book(books, book)
            save_books(filename, books)
        elif choice == '2':
            display_books(books)
            index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
            remove_book(books, index)
            save_books(filename, books)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if _name_ == "_main_":
    main()


    # Aplikasi Pengelolaan Buku (Book Management System)

## Deskripsi
Aplikasi ini adalah sistem pengelolaan buku sederhana yang memungkinkan pengguna untuk menambahkan, menghapus, dan menampilkan daftar buku. Buku disimpan dalam file teks sehingga pengguna dapat melanjutkan pekerjaan mereka di lain waktu.

## Fitur
- Menambahkan buku baru
- Menghapus buku berdasarkan nomor urut
- Menampilkan semua buku
- Menyimpan dan membaca dari file
- Menggunakan rekursi untuk menampilkan daftar buku

## Cara Menggunakan
1. Clone repositori ini atau unduh file book_management.py dan books.txt.
2. Jalankan aplikasi dengan perintah:

Ikuti instruksi di menu untuk menambahkan, menghapus, atau menampilkan buku.

## Struktur File
- book_management.py: File utama yang berisi logika aplikasi.
- books.txt: File untuk menyimpan daftar buku.

## Teknologi yang Digunakan
- Python
- File Handling
- Rekursi
- Manipulasi String

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat pull request atau buka isu jika Anda menemukan bug.

## Lisensi
Proyek ini dilisensikan di bawah MIT License.