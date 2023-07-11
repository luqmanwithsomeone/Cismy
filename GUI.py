import tkinter as tk
import json
from tkinter import messagebox
from tkinter import ttk

def place_center():
    start_button.place(relx=0.35555, rely=0.5, anchor=tk.CENTER)
    about_button.place(relx=0.6555, rely=0.5, anchor=tk.CENTER)

def start_action():
    def back_action():
        action_window.destroy()  
        window.deiconify()  


    def settings_action():
        def back_action():
            mantap2.destroy() 
            action_window.deiconify()
        def read_json_data():
            with open('data.json') as file:
                data = json.load(file)
            return data

        def save_json_data(data):
            with open('data.json', 'w') as file:
                json.dump(data, file)

        def update_quantity():
            selected_merk = merk_dropdown.get()
            input_value = input_entry.get()

            if input_value.isdigit():
                input_value = int(input_value)


                data = read_json_data()

                for obj in data:
                    if obj['merk'] == selected_merk:
                        obj['jumlah'] = input_value
                        break
                else:
                    data.append({'merk': selected_merk, 'jumlah': input_value})

    
                save_json_data(data)

        
                refresh_quantity()
            else:

                tk.messagebox.showerror("Error", "Input harus berupa angka!")

    
        def refresh_quantity():
            selected_merk = merk_dropdown.get()

        
            data = read_json_data()

    
            for obj in data:
                if obj['merk'] == selected_merk:
                
                    quantity_label.config(text="Jumlah: {}".format(obj['jumlah']))
                    break
            else:
                 quantity_label.config(text="Merk tidak ditemukan")

       
        data = read_json_data()
        action_window.withdraw()

       
        mantap2 = tk.Tk()
        mantap2.title("GUI dengan Dropdown dan Label")

    
        merk_dropdown = tk.StringVar(mantap2)
        merk_dropdown.set("")
        merk_menu = tk.OptionMenu(mantap2, merk_dropdown, *[obj['merk'] for obj in data])
        merk_menu.pack()

       
        quantity_label = tk.Label(mantap2, text="Jumlah: ")
        quantity_label.pack()

     
        data_label = tk.Label(mantap2, text="Data Jumlah: ")
        data_label.pack()

       
        input_entry = tk.Entry(mantap2)
        input_entry.pack()
        mantap2.geometry("300x300") 
      
        update_button = tk.Button(mantap2, text="Update", command=update_quantity)
        update_button.pack()


        refresh_button = tk.Button(mantap2, text="Refresh", command=refresh_quantity)
        refresh_button.pack()

        back_button = tk.Button(mantap2, text="Back", command=back_action)
        back_button.pack()
 
        mantap2.mainloop()


    def barang_masuk_action():
        def back_action():
            mantap_window.destroy()  
            action_window.deiconify() 

        def submit_action():
            merk = merk_entry.get()
            jumlah = jumlah_entry.get()
            
     
            if not merk.replace(" ", "").isalpha():
                messagebox.showerror("Error", "Input Merk Rokok hanya boleh berisi huruf.")
                return
            
         
            if not jumlah.isdigit():
                messagebox.showerror("Error", "Input Jumlah Rokok hanya boleh berisi angka.")
                return
            
           
            existing_data = [rokok for rokok in data if rokok["merk"] == merk ]
            if existing_data:
                messagebox.showerror("Error", "Data sudah ada.")
            else:
                rokok = {"merk": merk, "jumlah": jumlah}
                data.append(rokok)
                save_to_json()
                messagebox.showinfo("Success", "Data berhasil ditambahkan.")

        def save_to_json():
            with open("data.json", "w") as file:
                json.dump(data, file, sort_keys=True, indent=4)

        
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        
        action_window.withdraw()
        

       
        mantap_window = tk.Toplevel()
        mantap_window.title("mantap")
        mantap_window.geometry("300x300") 
       
        merk_label = tk.Label(mantap_window, text="Nama Rokok:")
        merk_label.pack()
        merk_entry = tk.Entry(mantap_window)
        merk_entry.pack()

        
        jumlah_label = tk.Label(mantap_window, text="Jumlah Rokok:")
        jumlah_label.pack()
        jumlah_entry = tk.Entry(mantap_window)
        jumlah_entry.pack()

      
        submit_button = tk.Button(mantap_window, text="Submit", command=submit_action)
        submit_button.pack()

       
        back_button = tk.Button(mantap_window, text="Back", command=back_action)
        back_button.pack()
        mantap_window.mainloop()







        
        
           
    def barang_keluar_action():
        def back_action():
            mantap1_window.destroy() 
            action_window.deiconify() 
            
        def load_data():
            with open('data.json') as file:
                data = json.load(file)
            return data

        def save_data(data):
            with open('data.json', 'w') as file:
                json.dump(data, file)

        
        def extract_data():
            data = load_data()
            brand_list = []
            count_dict = {}
            for item in data:
                brand_list.append(item['merk'])
                count_dict[item['merk']] = int(item['jumlah'])
            return brand_list, count_dict

        def update_data(brand, value):
            data = load_data()
            for item in data:
                if item['merk'] == brand:
                    item['jumlah'] = str(value)
                    break
            save_data(data)
        
        action_window.withdraw()
       
        mantap1_window = tk.Tk()
        mantap1_window.title("Aplikasi Rokok")
        mantap1_window.geometry("300x300") 
      
        brand_label = tk.Label(mantap1_window, text="Merk Rokok")
        brand_label.pack()
        
        
        selected_brand = tk.StringVar()
        selected_brand.set("Pilih Merk Rokok")

        brand_list, count_dict = extract_data()
        dropdown = tk.OptionMenu(mantap1_window, selected_brand, *brand_list)
        dropdown.pack()
        
        
        def update_count():
            brand = selected_brand.get()
            count = count_dict.get(brand, 0)
            cigarette_count.config(text="Jumlah Rokok: " + str(count))
            selected_brand_label.config(text="Merk Rokok Terpilih: " + brand)       
            selected_brand.set(brand)
    
        selected_brand_label = tk.Label(mantap1_window, text="Merk Rokok Terpilih: ")
        selected_brand_label.pack()

       
        cigarette_count = tk.Label(mantap1_window, text="Jumlah Rokok: ")
        cigarette_count.pack()

        
        def update_data_count():
            brand = selected_brand.get()
            try:
                value = int(entry.get())
                current_count = count_dict.get(brand, 0)
                new_count = current_count - value
                if new_count < 0:
                    raise ValueError("Jumlah rokok tidak bisa menjadi negatif.")
                update_data(brand, new_count)
                count_dict[brand] = new_count
                update_count()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        
        entry = tk.Entry(mantap1_window)
        entry.pack()
        back_button = tk.Button(mantap1_window, text="Back", command=back_action)
        back_button.pack()
        
        update_button = tk.Button(mantap1_window, text="Update", command=update_data_count)
        update_button.pack()

      
        refresh_button = tk.Button(mantap1_window, text="Refresh", command=update_count)
        refresh_button.pack()

        
        update_count()


















    def cek_stok_action():
        def back_action():
            root.destroy()  
            action_window.deiconify() 

        def load_data():
            try:
                with open('data.json') as file:
                    data = json.load(file)
                    return data
            except FileNotFoundError:
                print("File not found!")
                return []

        def display_table():
            data = load_data()
            table.delete(*table.get_children()) 

            for item in data:
                merk = item.get('merk', '')
                jumlah = item.get('jumlah', '')

                table.insert('', 'end', values=(merk, jumlah))

        
        root = tk.Tk()
        root.title("Tabel JSON")
        action_window.withdraw()

        root.geometry("300x300") 

        
        table = ttk.Treeview(root, columns=('merk', 'jumlah'), show='headings')
        table.heading('merk', text='Merk')
        table.heading('jumlah', text='Jumlah')
        table.pack(padx=10, pady=10)

       
        load_button = tk.Button(root, text="Muat Data", command=display_table)
        load_button.pack(pady=10)
          
        back_button = tk.Button(root, text="Back", command=back_action)
        back_button.pack()



  

 
    window.withdraw()
 

    
    action_window = tk.Toplevel()
    action_window.title("Aksi")
    action_window.geometry("300x300") 
    
    back_button = tk.Button(action_window, text="Back", command=back_action)
     
    settings_button = tk.Button(action_window, text="Tambah stok", command=settings_action)
    settings_button.pack()

    
    barang_masuk_button = tk.Button(action_window, text="Barang Masuk", command=barang_masuk_action)
    barang_masuk_button.pack()

  
    barang_keluar_button = tk.Button(action_window, text="Barang Keluar", command=barang_keluar_action)
    barang_keluar_button.pack()

   
    cek_stok_button = tk.Button(action_window, text="Cek Stok", command=cek_stok_action)
    cek_stok_button.pack()
    back_button.pack()

   

    

def about_action():
    messagebox.showinfo("About", "Tombol About ditekan!")



window = tk.Tk()
window.title("Cismy")

window.geometry("300x300")




start_button = tk.Button(window, text="Start", command=start_action, padx=10, pady=5)
start_button.pack()




about_button = tk.Button(window, text="About", command=about_action, padx=10, pady=5)
about_button.pack()

window.resizable(False, False)

place_center()


window.mainloop()
