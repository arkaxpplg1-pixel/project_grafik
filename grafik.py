from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


WARNA_LATAR = '#F2F2F2'


def _bersihkan_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def buat_bar_chart(frame, data, mode="light"):
    _bersihkan_frame(frame)

    if mode == "dark":
        bg = "#1E1E1E"
        fg = "white"
    else:
        bg = WARNA_LATAR
        fg = "black"

    fig = Figure(
        figsize=(10, 5.5),
        dpi=100,
        facecolor=bg
    )

    ax = fig.add_subplot(111)
    ax.set_facecolor(bg)

    label = [row[0] for row in data]
    nilai = [row[1] for row in data]

    ax.bar(label, nilai)

    ax.set_title(
        "Jumlah Penjualan per Produk",
        color=fg,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Nama Produk",
        color=fg
    )

    ax.set_ylabel(
        "Jumlah Terjual",
        color=fg
    )

    ax.tick_params(
        axis="x",
        labelrotation=20,
        colors=fg
    )

    ax.tick_params(
        axis="y",
        colors=fg
    )

    for spine in ax.spines.values():
        spine.set_color(fg)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


def buat_pie_chart(frame, data, mode="light"):
    _bersihkan_frame(frame)

    if mode == "dark":
        bg = "#1E1E1E"
        fg = "white"
    else:
        bg = WARNA_LATAR
        fg = "black"

    fig = Figure(
        figsize=(10, 5.5),
        dpi=100,
        facecolor=bg
    )

    ax = fig.add_subplot(111)
    ax.set_facecolor(bg)

    label = [row[0] for row in data]
    nilai = [row[1] for row in data]

    ax.pie(
        nilai,
        labels=label,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Persentase Penjualan Berdasarkan Kategori",
        color=fg,
        fontsize=14,
        fontweight="bold"
    )

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


def buat_omzet_chart(frame, data, mode="light"):
    _bersihkan_frame(frame)

    if mode == "dark":
        bg = "#1E1E1E"
        fg = "white"
    else:
        bg = WARNA_LATAR
        fg = "black"

    fig = Figure(
        figsize=(10, 5.5),
        dpi=100,
        facecolor=bg
    )

    ax = fig.add_subplot(111)
    ax.set_facecolor(bg)

    label = [row[0] for row in data]
    nilai = [row[1] for row in data]

    ax.bar(label, nilai)

    ax.set_title(
        "Total Omzet per Produk",
        color=fg,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Nama Produk",
        color=fg
    )

    ax.set_ylabel(
        "Total Omzet",
        color=fg
    )

    ax.tick_params(
        axis="x",
        labelrotation=20,
        colors=fg
    )

    ax.tick_params(
        axis="y",
        colors=fg
    )

    for spine in ax.spines.values():
        spine.set_color(fg)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


def buat_line_chart(frame, data, mode="light"):
    _bersihkan_frame(frame)

    if mode == "dark":
        bg = "#1E1E1E"
        fg = "white"
    else:
        bg = WARNA_LATAR
        fg = "black"

    fig = Figure(
        figsize=(10, 5.5),
        dpi=100,
        facecolor=bg
    )

    ax = fig.add_subplot(111)
    ax.set_facecolor(bg)

    tanggal = [row[0] for row in data]
    nilai = [row[1] for row in data]

    ax.plot(
        tanggal,
        nilai,
        marker="o",
        linewidth=2
    )

    ax.set_title(
        "Tren Penjualan Berdasarkan Tanggal",
        color=fg,
        fontsize=14,
        fontweight="bold"
    )

    ax.set_xlabel(
        "Tanggal",
        color=fg
    )

    ax.set_ylabel(
        "Jumlah Terjual",
        color=fg
    )

    ax.tick_params(
        axis="x",
        labelrotation=20,
        colors=fg
    )

    ax.tick_params(
        axis="y",
        colors=fg
    )

    for spine in ax.spines.values():
        spine.set_color(fg)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )