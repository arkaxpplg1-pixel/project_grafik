
# main.py
import customtkinter as ctk
from tkinter import ttk, messagebox
import database
import grafik
from datetime import datetime


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class AplikasiPenjualan:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Penjualan")
        # Ukuran awal mengikuti layar pengguna, bukan ukuran tetap.
        # Tetap mempertahankan batas minimum agar komponen tidak bertabrakan.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = min(1400, max(900, int(screen_width * 0.90)))
        window_height = min(900, max(650, int(screen_height * 0.88)))

        pos_x = max(0, (screen_width - window_width) // 2)
        pos_y = max(0, (screen_height - window_height) // 2)

        self.root.geometry(
            f"{window_width}x{window_height}+{pos_x}+{pos_y}"
        )
        self.root.minsize(720, 520)

        # Saat ukuran window berubah, komponen ikut menyesuaikan.
        self.root.bind("<Configure>", self.responsive_layout)

        self.mode_tampilan = "light"

        # Menyimpan grafik yang sedang aktif
        self.grafik_terakhir = "bar"

        # =========================
        # JUDUL
        # =========================
        self.frame_header = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )
        self.frame_header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        self.label_judul = ctk.CTkLabel(
            self.frame_header,
            text="DASHBOARD PENJUALAN",
            font=("Arial", 26, "bold")
        )
        self.label_judul.pack(anchor="w")

        self.label_subjudul = ctk.CTkLabel(
            self.frame_header,
            text="Kelola data penjualan dan lihat grafik secara langsung",
            font=("Arial", 13)
        )
        self.label_subjudul.pack(
            anchor="w",
            pady=(2, 0)
        )

        # =========================
        # SCROLLABLE FRAME
        # =========================
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color="transparent"
        )
        self.scroll_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        # =========================
        # FORM DATA
        # =========================
        self.frame_form = ctk.CTkFrame(
            self.scroll_frame,
            corner_radius=8
        )
        self.frame_form.pack(
            fill="x",
            padx=5,
            pady=5
        )

        self.label_form = ctk.CTkLabel(
            self.frame_form,
            text="FORM DATA PENJUALAN",
            font=("Arial", 16, "bold")
        )
        self.label_form.grid(
            row=0,
            column=0,
            columnspan=5,
            sticky="w",
            padx=20,
            pady=(15, 10)
        )

        # =========================
        # NAMA PRODUK
        # =========================
        ctk.CTkLabel(
            self.frame_form,
            text="Nama Produk",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(20, 10),
            pady=5
        )

        self.entry_nama = ctk.CTkEntry(
            self.frame_form,
            width=210,
            height=32
        )
        self.entry_nama.grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=(0, 15)
        )

        # =========================
        # KATEGORI
        # =========================
        ctk.CTkLabel(
            self.frame_form,
            text="Kategori",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=1,
            sticky="w",
            padx=10,
            pady=5
        )

        self.combo_kategori = ctk.CTkOptionMenu(
            self.frame_form,
            width=210,
            height=32,
            values=[
                "Elektronik",
                "Makanan",
                "Minuman",
                "Pakaian",
                "Kebutuhan Rumah",
                "Lainnya"
            ]
        )
        self.combo_kategori.grid(
            row=2,
            column=1,
            padx=10,
            pady=(0, 15)
        )

        # =========================
        # JUMLAH TERJUAL
        # =========================
        ctk.CTkLabel(
            self.frame_form,
            text="Jumlah Terjual",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=10,
            pady=5
        )

        self.entry_jumlah = ctk.CTkEntry(
            self.frame_form,
            width=190,
            height=32
        )
        self.entry_jumlah.grid(
            row=2,
            column=2,
            padx=10,
            pady=(0, 15)
        )

        # =========================
        # HARGA SATUAN
        # =========================
        ctk.CTkLabel(
            self.frame_form,
            text="Harga Satuan",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=3,
            sticky="w",
            padx=10,
            pady=5
        )

        self.entry_harga = ctk.CTkEntry(
            self.frame_form,
            width=190,
            height=32
        )
        self.entry_harga.grid(
            row=2,
            column=3,
            padx=10,
            pady=(0, 15)
        )

        # =========================
        # TANGGAL
        # =========================
        ctk.CTkLabel(
            self.frame_form,
            text="Tanggal",
            font=("Arial", 12)
        ).grid(
            row=1,
            column=4,
            sticky="w",
            padx=(10, 20),
            pady=5
        )

        self.entry_tanggal = ctk.CTkEntry(
            self.frame_form,
            width=150,
            height=32
        )
        self.entry_tanggal.grid(
            row=2,
            column=4,
            padx=(10, 20),
            pady=(0, 15)
        )

        self.entry_tanggal.insert(
            0,
            datetime.now().strftime("%Y-%m-%d")
        )

        # =========================
        # TOMBOL CRUD
        # =========================
        self.frame_tombol = ctk.CTkFrame(
            self.frame_form,
            fg_color="transparent"
        )
        self.frame_tombol.grid(
            row=3,
            column=0,
            columnspan=5,
            pady=(0, 15)
        )

        ctk.CTkButton(
            self.frame_tombol,
            text="TAMBAH DATA",
            width=140,
            height=35,
            command=self.tambah
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_tombol,
            text="UPDATE DATA",
            width=140,
            height=35,
            command=self.update
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_tombol,
            text="HAPUS DATA",
            width=140,
            height=35,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.hapus
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_tombol,
            text="BERSIHKAN",
            width=140,
            height=35,
            fg_color="#6B7280",
            hover_color="#4B5563",
            command=self.bersihkan_form
        ).pack(side="left", padx=5)

        # =========================
        # DARK MODE
        # =========================
        self.switch_mode = ctk.CTkSwitch(
            self.frame_form,
            text="Dark Mode",
            command=self.ganti_mode
        )
        self.switch_mode.grid(
            row=4,
            column=4,
            sticky="e",
            padx=20,
            pady=(0, 15)
        )

        # =========================
        # TABEL
        # =========================
        self.frame_tabel = ctk.CTkFrame(
            self.scroll_frame,
            corner_radius=8
        )
        self.frame_tabel.pack(
            fill="x",
            padx=5,
            pady=10
        )

        self.label_tabel = ctk.CTkLabel(
            self.frame_tabel,
            text="DATA PENJUALAN",
            font=("Arial", 16, "bold")
        )
        self.label_tabel.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        self.style = ttk.Style()

        self.style.configure(
            "Treeview",
            rowheight=28,
            font=("Arial", 10)
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        self.tree = ttk.Treeview(
            self.frame_tabel,
            columns=(
                "id",
                "tanggal",
                "nama_produk",
                "kategori",
                "jumlah_terjual",
                "harga_satuan"
            ),
            show="headings",
            height=7
        )

        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "tanggal",
            text="Tanggal"
        )

        self.tree.heading(
            "nama_produk",
            text="Nama Produk"
        )

        self.tree.heading(
            "kategori",
            text="Kategori"
        )

        self.tree.heading(
            "jumlah_terjual",
            text="Jumlah Terjual"
        )

        self.tree.heading(
            "harga_satuan",
            text="Harga Satuan"
        )

        self.tree.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tree.column(
            "tanggal",
            width=120,
            anchor="center"
        )

        self.tree.column(
            "nama_produk",
            width=230
        )

        self.tree.column(
            "kategori",
            width=160
        )

        self.tree.column(
            "jumlah_terjual",
            width=160,
            anchor="center"
        )

        self.tree.column(
            "harga_satuan",
            width=160,
            anchor="center"
        )

        self.tree.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.tree.bind(
            "<ButtonRelease-1>",
            self.pilih_baris
        )

        # =========================
        # TOMBOL GRAFIK
        # =========================
        self.frame_grafik_tombol = ctk.CTkFrame(
            self.scroll_frame,
            fg_color="transparent"
        )
        self.frame_grafik_tombol.pack(
            fill="x",
            padx=5,
            pady=5
        )

        ctk.CTkButton(
            self.frame_grafik_tombol,
            text="BAR CHART JUMLAH",
            width=170,
            height=35,
            command=self.tampilkan_bar
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_grafik_tombol,
            text="PIE CHART KATEGORI",
            width=180,
            height=35,
            command=self.tampilkan_pie
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_grafik_tombol,
            text="BAR CHART OMZET",
            width=170,
            height=35,
            command=self.tampilkan_omzet
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            self.frame_grafik_tombol,
            text="LINE CHART TREN",
            width=170,
            height=35,
            command=self.tampilkan_line
        ).pack(side="left", padx=5)

        # =========================
        # FILTER
        # =========================
        self.frame_filter = ctk.CTkFrame(
            self.scroll_frame,
            corner_radius=8
        )
        self.frame_filter.pack(
            fill="x",
            padx=5,
            pady=10
        )

        ctk.CTkLabel(
            self.frame_filter,
            text="Filter Kategori",
            font=("Arial", 12)
        ).pack(
            side="left",
            padx=(20, 10),
            pady=15
        )

        self.combo_filter = ctk.CTkOptionMenu(
            self.frame_filter,
            width=220,
            height=32,
            values=[
                "Semua Kategori",
                "Elektronik",
                "Makanan",
                "Minuman",
                "Pakaian",
                "Kebutuhan Rumah",
                "Lainnya"
            ],
            command=self.filter_grafik
        )

        self.combo_filter.pack(
            side="left",
            padx=10,
            pady=15
        )

        # =========================
        # AREA GRAFIK
        # =========================
        self.frame_grafik = ctk.CTkFrame(
            self.scroll_frame,
            height=520,
            corner_radius=8
        )

        self.frame_grafik.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=10
        )

        self.frame_grafik.pack_propagate(False)

        self.tampilkan_data()

        # Terapkan ukuran responsif setelah seluruh widget selesai dibuat.
        self.root.after(100, self.responsive_layout)

    # =========================
    # RESPONSIVE LAYOUT
    # =========================
    def responsive_layout(self, event=None):
        """Menyesuaikan ukuran widget berdasarkan ukuran window."""
        if not hasattr(self, "entry_nama"):
            return

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Lebar field mengikuti lebar window.
        if width >= 1200:
            field_width = 210
            jumlah_width = 190
            tanggal_width = 150
            button_width = 140
            chart_button_width = 170
        elif width >= 950:
            field_width = 175
            jumlah_width = 160
            tanggal_width = 140
            button_width = 125
            chart_button_width = 145
        else:
            field_width = 125
            jumlah_width = 120
            tanggal_width = 120
            button_width = 110
            chart_button_width = 125

        self.entry_nama.configure(width=field_width)
        self.combo_kategori.configure(width=field_width)
        self.entry_jumlah.configure(width=jumlah_width)
        self.entry_harga.configure(width=jumlah_width)
        self.entry_tanggal.configure(width=tanggal_width)

        # Tombol CRUD ikut mengecil pada window yang lebih sempit.
        for widget in self.frame_tombol.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(width=button_width)

        # Tombol grafik ikut menyesuaikan.
        for widget in self.frame_grafik_tombol.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(width=chart_button_width)

        # Treeview menggunakan lebar window agar tidak terlalu melebar.
        table_width = max(500, width - 90)
        proportions = {
            "id": 0.07,
            "tanggal": 0.13,
            "nama_produk": 0.27,
            "kategori": 0.20,
            "jumlah_terjual": 0.17,
            "harga_satuan": 0.16
        }

        for column, proportion in proportions.items():
            self.tree.column(
                column,
                width=max(55, int(table_width * proportion))
            )

        # Tinggi area grafik mengikuti tinggi window.
        graph_height = max(420, int(height * 0.55))
        self.frame_grafik.configure(height=graph_height)

        # Judul mengecil pada layar yang lebih sempit.
        if width < 850:
            self.label_judul.configure(font=("Arial", 20, "bold"))
            self.label_subjudul.configure(font=("Arial", 11))
        elif width < 1100:
            self.label_judul.configure(font=("Arial", 23, "bold"))
            self.label_subjudul.configure(font=("Arial", 12))
        else:
            self.label_judul.configure(font=("Arial", 26, "bold"))
            self.label_subjudul.configure(font=("Arial", 13))

    # =========================
    # REFRESH GRAFIK AKTIF
    # =========================
    def refresh_grafik_aktif(self):
        if self.grafik_terakhir == "bar":
            self.tampilkan_bar()

        elif self.grafik_terakhir == "pie":
            self.tampilkan_pie()

        elif self.grafik_terakhir == "omzet":
            self.tampilkan_omzet()

        elif self.grafik_terakhir == "line":
            self.tampilkan_line()

    # =========================
    # TAMPILKAN DATA
    # =========================
    def tampilkan_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = database.get_all_data()

        for row in data:
            self.tree.insert(
                "",
                "end",
                values=row
            )

        self.update_filter_kategori()

    # =========================
    # UPDATE FILTER KATEGORI
    # =========================
    def update_filter_kategori(self):
        kategori = database.get_rekap_kategori()

        values = ["Semua Kategori"]

        for row in kategori:
            if row[0] not in values:
                values.append(row[0])

        self.combo_filter.configure(
            values=values
        )

    # =========================
    # TAMBAH DATA
    # =========================
    def tambah(self):
        nama = self.entry_nama.get().strip()
        kategori = self.combo_kategori.get()
        jumlah = self.entry_jumlah.get().strip()
        harga = self.entry_harga.get().strip()
        tanggal = self.entry_tanggal.get().strip()

        if not nama or not jumlah or not harga or not tanggal:
            messagebox.showwarning(
                "Peringatan",
                "Semua data harus diisi!"
            )
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Jumlah terjual harus berupa angka!"
            )
            return

        try:
            harga = int(harga)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Harga satuan harus berupa angka!"
            )
            return

        try:
            datetime.strptime(
                tanggal,
                "%Y-%m-%d"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Tanggal harus menggunakan format YYYY-MM-DD!"
            )
            return

        if jumlah < 0 or harga < 0:
            messagebox.showerror(
                "Error",
                "Jumlah dan harga tidak boleh negatif!"
            )
            return

        database.tambah_data(
            nama,
            kategori,
            jumlah,
            harga,
            tanggal
        )

        messagebox.showinfo(
            "Berhasil",
            "Data berhasil ditambahkan!"
        )

        self.bersihkan_form()
        self.tampilkan_data()
        self.refresh_grafik_aktif()

    # =========================
    # UPDATE DATA
    # =========================
    def update(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin diupdate!"
            )
            return

        item = self.tree.item(selected[0])
        id_produk = item["values"][0]

        nama = self.entry_nama.get().strip()
        kategori = self.combo_kategori.get()
        jumlah = self.entry_jumlah.get().strip()
        harga = self.entry_harga.get().strip()
        tanggal = self.entry_tanggal.get().strip()

        if not nama or not jumlah or not harga or not tanggal:
            messagebox.showwarning(
                "Peringatan",
                "Semua data harus diisi!"
            )
            return

        try:
            jumlah = int(jumlah)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Jumlah terjual harus berupa angka!"
            )
            return

        try:
            harga = int(harga)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Harga satuan harus berupa angka!"
            )
            return

        try:
            datetime.strptime(
                tanggal,
                "%Y-%m-%d"
            )
        except ValueError:
            messagebox.showerror(
                "Error",
                "Tanggal harus menggunakan format YYYY-MM-DD!"
            )
            return

        if jumlah < 0 or harga < 0:
            messagebox.showerror(
                "Error",
                "Jumlah dan harga tidak boleh negatif!"
            )
            return

        database.update_data(
            id_produk,
            nama,
            kategori,
            jumlah,
            harga,
            tanggal
        )

        messagebox.showinfo(
            "Berhasil",
            "Data berhasil diupdate!"
        )

        self.bersihkan_form()
        self.tampilkan_data()
        self.refresh_grafik_aktif()

    # =========================
    # HAPUS DATA
    # =========================
    def hapus(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin dihapus!"
            )
            return

        item = self.tree.item(selected[0])
        id_produk = item["values"][0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data ini?"
        )

        if konfirmasi:
            database.hapus_data(id_produk)

            messagebox.showinfo(
                "Berhasil",
                "Data berhasil dihapus!"
            )

            self.bersihkan_form()
            self.tampilkan_data()
            self.refresh_grafik_aktif()

    # =========================
    # PILIH BARIS
    # =========================
    def pilih_baris(self, event):
        selected = self.tree.selection()

        if not selected:
            return

        item = self.tree.item(selected[0])
        values = item["values"]

        self.entry_tanggal.delete(0, "end")
        self.entry_tanggal.insert(
            0,
            values[1]
        )

        self.entry_nama.delete(0, "end")
        self.entry_nama.insert(
            0,
            values[2]
        )

        self.combo_kategori.set(
            values[3]
        )

        self.entry_jumlah.delete(0, "end")
        self.entry_jumlah.insert(
            0,
            values[4]
        )

        self.entry_harga.delete(0, "end")
        self.entry_harga.insert(
            0,
            values[5]
        )

    # =========================
    # BERSIHKAN FORM
    # =========================
    def bersihkan_form(self):
        self.entry_nama.delete(0, "end")
        self.entry_jumlah.delete(0, "end")
        self.entry_harga.delete(0, "end")

        self.entry_tanggal.delete(0, "end")
        self.entry_tanggal.insert(
            0,
            datetime.now().strftime("%Y-%m-%d")
        )

        self.combo_kategori.set(
            "Elektronik"
        )

        for item in self.tree.selection():
            self.tree.selection_remove(item)

    # =========================
    # BAR CHART
    # =========================
    def tampilkan_bar(self):
        self.grafik_terakhir = "bar"

        data = database.get_all_data()

        grafik_data = []

        for row in data:
            grafik_data.append(
                (row[2], row[4])
            )

        grafik.buat_bar_chart(
            self.frame_grafik,
            grafik_data,
            self.mode_tampilan
        )

    # =========================
    # PIE CHART
    # =========================
    def tampilkan_pie(self):
        self.grafik_terakhir = "pie"

        data = database.get_all_data()

        pilihan = self.combo_filter.get()

        grafik_data = []

        # =========================
        # SEMUA KATEGORI
        # Pie berdasarkan kategori
        # =========================
        if pilihan == "Semua Kategori":

            kategori_data = {}

            for row in data:
                kategori = row[3]
                jumlah = row[4]

                if kategori not in kategori_data:
                    kategori_data[kategori] = 0

                kategori_data[kategori] += jumlah

            for kategori, jumlah in kategori_data.items():
                if jumlah > 0:
                    grafik_data.append(
                        (kategori, jumlah)
                    )

        # =========================
        # KATEGORI TERTENTU
        # Pie berdasarkan produk
        # =========================
        else:

            produk_data = {}

            for row in data:
                kategori = row[3]
                nama_produk = row[2]
                jumlah = row[4]

                if kategori == pilihan:

                    if nama_produk not in produk_data:
                        produk_data[nama_produk] = 0

                    produk_data[nama_produk] += jumlah

            for nama_produk, jumlah in produk_data.items():
                if jumlah > 0:
                    grafik_data.append(
                        (nama_produk, jumlah)
                    )

        # =========================
        # CEK DATA
        # =========================
        if not grafik_data:
            messagebox.showwarning(
                "Peringatan",
                "Tidak ada data untuk ditampilkan!"
            )
            return

        grafik.buat_pie_chart(
            self.frame_grafik,
            grafik_data,
            self.mode_tampilan
        )

    # =========================
    # BAR CHART OMZET
    # =========================
    def tampilkan_omzet(self):
        self.grafik_terakhir = "omzet"

        data = database.get_rekap_omzet()

        grafik.buat_omzet_chart(
            self.frame_grafik,
            data,
            self.mode_tampilan
        )

    # =========================
    # LINE CHART TREN
    # =========================
    def tampilkan_line(self):
        self.grafik_terakhir = "line"

        data = database.get_rekap_tanggal()

        grafik.buat_line_chart(
            self.frame_grafik,
            data,
            self.mode_tampilan
        )

    # =========================
    # FILTER GRAFIK
    # =========================
    def filter_grafik(self, pilihan):
        data = database.get_all_data()

        if pilihan != "Semua Kategori":
            data = [
                row for row in data
                if row[3] == pilihan
            ]

        # =========================
        # FILTER BAR CHART
        # =========================
        if self.grafik_terakhir == "bar":

            grafik_data = []

            for row in data:
                grafik_data.append(
                    (row[2], row[4])
                )

            if not grafik_data:
                messagebox.showwarning(
                    "Peringatan",
                    "Tidak ada data untuk kategori yang dipilih!"
                )
                return

            grafik.buat_bar_chart(
                self.frame_grafik,
                grafik_data,
                self.mode_tampilan
            )

        # =========================
        # FILTER PIE CHART
        # =========================
        elif self.grafik_terakhir == "pie":

            grafik_data = []

            # =========================
            # SEMUA KATEGORI
            # Pie berdasarkan kategori
            # =========================
            if pilihan == "Semua Kategori":

                kategori_data = {}

                for row in data:
                    kategori = row[3]
                    jumlah = row[4]

                    if kategori not in kategori_data:
                        kategori_data[kategori] = 0

                    kategori_data[kategori] += jumlah

                for kategori, jumlah in kategori_data.items():
                    if jumlah > 0:
                        grafik_data.append(
                            (kategori, jumlah)
                        )

            # =========================
            # KATEGORI TERTENTU
            # Pie berdasarkan produk
            # =========================
            else:

                produk_data = {}

                for row in data:
                    nama_produk = row[2]
                    jumlah = row[4]

                    if nama_produk not in produk_data:
                        produk_data[nama_produk] = 0

                    produk_data[nama_produk] += jumlah

                for nama_produk, jumlah in produk_data.items():
                    if jumlah > 0:
                        grafik_data.append(
                            (nama_produk, jumlah)
                        )

            # =========================
            # CEK DATA
            # =========================
            if not grafik_data:
                messagebox.showwarning(
                    "Peringatan",
                    "Tidak ada data untuk kategori yang dipilih!"
                )
                return

            grafik.buat_pie_chart(
                self.frame_grafik,
                grafik_data,
                self.mode_tampilan
            )

        # =========================
        # FILTER OMZET
        # =========================
        elif self.grafik_terakhir == "omzet":

            omzet_data = {}

            for row in data:
                nama_produk = row[2]
                jumlah = row[4]
                harga = row[5]

                omzet = jumlah * harga

                if nama_produk not in omzet_data:
                    omzet_data[nama_produk] = 0

                omzet_data[nama_produk] += omzet

            if not omzet_data:
                messagebox.showwarning(
                    "Peringatan",
                    "Tidak ada data untuk kategori yang dipilih!"
                )
                return

            grafik.buat_omzet_chart(
                self.frame_grafik,
                list(omzet_data.items()),
                self.mode_tampilan
            )

        # =========================
        # FILTER LINE CHART
        # =========================
        elif self.grafik_terakhir == "line":

            tanggal_data = {}

            for row in data:
                tanggal = row[1]
                jumlah = row[4]

                if tanggal not in tanggal_data:
                    tanggal_data[tanggal] = 0

                tanggal_data[tanggal] += jumlah

            data_line = sorted(
                tanggal_data.items()
            )

            if not data_line:
                messagebox.showwarning(
                    "Peringatan",
                    "Tidak ada data untuk kategori yang dipilih!"
                )
                return

            grafik.buat_line_chart(
                self.frame_grafik,
                data_line,
                self.mode_tampilan
            )

    # =========================
    # GANTI MODE
    # =========================
    def ganti_mode(self):
        if self.switch_mode.get() == 1:
            self.mode_tampilan = "dark"
            ctk.set_appearance_mode("dark")
        else:
            self.mode_tampilan = "light"
            ctk.set_appearance_mode("light")

        self.refresh_grafik_aktif()


if __name__ == "__main__":
    root = ctk.CTk()
    app = AplikasiPenjualan(root)
    root.mainloop()