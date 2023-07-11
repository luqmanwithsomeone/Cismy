import tkinter as tk
import json

# Fungsi untuk membaca data dari file JSON
def read_json_data():
    with open('data.json') as file:
        data = json.load(file)
        return data

# Fungsi untuk menyimpan data ke file JSON
def save_json_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

# Fungsi untuk mengupdate jumlah berdasarkan input
def update_quantity():
    selected_merk = merk_dropdown.get()
    input_value = input_entry.get()

    # Periksa apakah input merupakan angka
    if input_value.isdigit():
        input_value = int(input_value)

        # Baca data JSON
        data = read_json_data()

        # Perbarui jumlah
        for obj in data:
            if obj['merk'] == selected_merk:
                obj['jumlah'] = input_value
                break
        else:
            data.append({'merk': selected_merk, 'jumlah': input_value})

        # Simpan data ke file JSON
        save_json_data(data)

        # Refresh label jumlah
        refresh_quantity()
    else:
        # Tampilkan pesan kesalahan jika input bukan angka
        tk.messagebox.showerror("Error", "Input harus berupa angka!")

# Fungsi untuk merefresh label jumlah
def refresh_quantity():
    selected_merk = merk_dropdown.get()

    # Baca data JSON
    data = read_json_data()

    # Cari objek dengan merk yang sesuai
    for obj in data:
        if obj['merk'] == selected_merk:
            # Update label jumlah
            quantity_label.config(text="Jumlah: {}".format(obj['jumlah']))
            break
    else:
        # Tampilkan pesan jika merk tidak ditemukan dalam data
        quantity_label.config(text="Merk tidak ditemukan")

# Membaca data awal dari file JSON
data = read_json_data()

# Membuat instance Tkinter
root = tk.Tk()
root.title("GUI dengan Dropdown dan Label")

# Membuat dropdown menu
merk_dropdown = tk.StringVar(root)
merk_dropdown.set("")  # Merk awal kosong
merk_menu = tk.OptionMenu(root, merk_dropdown, *[obj['merk'] for obj in data])
merk_menu.pack()

# Membuat label jumlah
quantity_label = tk.Label(root, text="Jumlah: ")
quantity_label.pack()

# Membuat label data jumlah
data_label = tk.Label(root, text="Data Jumlah: ")
data_label.pack()

# Membuat entry untuk input
input_entry = tk.Entry(root)
input_entry.pack()

# Membuat tombol Update
update_button = tk.Button(root, text="Update", command=update_quantity)
update_button.pack()

# Membuat tombol Refresh
refresh_button = tk.Button(root, text="Refresh", command=refresh_quantity)
refresh_button.pack()

# Menjalankan main loop Tkinter
root.mainloop()
