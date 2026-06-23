import csv
import os

FILE_NAME = "buku.csv"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def to_list(self):
        data_list = []
        current = self.head

        while current:
            data_list.append(current.data)
            current = current.next

        return data_list

def load_data():
    linked_list = LinkedList()
    data_map = {}

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                linked_list.append(row)
                data_map[row["ID"]] = row

    return linked_list, data_map

def save_data(data_map):
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["ID", "Judul", "Penulis", "Tahun"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for data in data_map.values():
            writer.writerow(data)

def tambah_buku(data_map):
    id_buku = input("ID Buku: ")

    if id_buku in data_map:
        print("ID sudah ada!")
        return

    judul = input("Judul Buku: ")
    penulis = input("Penulis: ")
    tahun = input("Tahun: ")

    data_map[id_buku] = {
        "ID": id_buku,
        "Judul": judul,
        "Penulis": penulis,
        "Tahun": tahun
    }

    save_data(data_map)
    print("Data berhasil ditambahkan!")

def tampilkan_buku(data_map):
    if not data_map:
        print("Data kosong.")
        return

    print("\\n=== DAFTAR BUKU ===")
    for buku in data_map.values():
        print(f"ID: {buku['ID']} | Judul: {buku['Judul']} | Penulis: {buku['Penulis']} | Tahun: {buku['Tahun']}")

def update_buku(data_map):
    id_buku = input("Masukkan ID Buku: ")

    if id_buku not in data_map:
        print("Data tidak ditemukan!")
        return

    data_map[id_buku]["Judul"] = input("Judul Baru: ")
    data_map[id_buku]["Penulis"] = input("Penulis Baru: ")
    data_map[id_buku]["Tahun"] = input("Tahun Baru: ")

    save_data(data_map)
    print("Data berhasil diperbarui!")

def hapus_buku(data_map):
    id_buku = input("Masukkan ID Buku: ")

    if id_buku not in data_map:
        print("Data tidak ditemukan!")
        return

    del data_map[id_buku]
    save_data(data_map)
    print("Data berhasil dihapus!")

def cari_buku(data_map):
    keyword = input("Masukkan judul buku: ").lower()

    ditemukan = False

    for buku in data_map.values():
        if keyword in buku["Judul"].lower():
            print(f"ID: {buku['ID']} | Judul: {buku['Judul']} | Penulis: {buku['Penulis']} | Tahun: {buku['Tahun']}")
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan.")

def sorting_buku(data_map):
    data = list(data_map.values())
    data.sort(key=lambda x: x["Judul"])

    print("\\n=== DATA TERURUT BERDASARKAN JUDUL ===")

    for buku in data:
        print(f"ID: {buku['ID']} | Judul: {buku['Judul']} | Penulis: {buku['Penulis']} | Tahun: {buku['Tahun']}")

def menu():
    while True:
        linked_list, data_map = load_data()

        print("\\n===== SISTEM MANAJEMEN PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Cari Buku")
        print("4. Urutkan Buku")
        print("5. Update Buku")
        print("6. Hapus Buku")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_buku(data_map)
        elif pilihan == "2":
            tampilkan_buku(data_map)
        elif pilihan == "3":
            cari_buku(data_map)
        elif pilihan == "4":
            sorting_buku(data_map)
        elif pilihan == "5":
            update_buku(data_map)
        elif pilihan == "6":
            hapus_buku(data_map)
        elif pilihan == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

menu()
