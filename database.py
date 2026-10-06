import mysql.connector


def koneksi_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password="",
        database='db_penjualan'
    )


def get_all_data():
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            id,
            tanggal,
            nama_produk,
            kategori,
            jumlah_terjual,
            harga_satuan
        FROM penjualan
        '''
    )

    hasil = cursor.fetchall()

    cursor.close()
    conn.close()

    return hasil


def tambah_data(nama_produk, kategori, jumlah_terjual, harga_satuan, tanggal):
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO penjualan
        (nama_produk, kategori, jumlah_terjual, harga_satuan, tanggal)
        VALUES (%s, %s, %s, %s, %s)
        ''',
        (
            nama_produk,
            kategori,
            jumlah_terjual,
            harga_satuan,
            tanggal
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def update_data(
    id_produk,
    nama_produk,
    kategori,
    jumlah_terjual,
    harga_satuan,
    tanggal
):
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE penjualan
        SET nama_produk=%s,
            kategori=%s,
            jumlah_terjual=%s,
            harga_satuan=%s,
            tanggal=%s
        WHERE id=%s
        ''',
        (
            nama_produk,
            kategori,
            jumlah_terjual,
            harga_satuan,
            tanggal,
            id_produk
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def hapus_data(id_produk):
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM penjualan WHERE id=%s',
        (id_produk,)
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_rekap_kategori():
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            kategori,
            SUM(jumlah_terjual) AS total
        FROM penjualan
        GROUP BY kategori
        '''
    )

    hasil = cursor.fetchall()

    cursor.close()
    conn.close()

    return hasil


def get_rekap_omzet():
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            nama_produk,
            SUM(jumlah_terjual * harga_satuan) AS omzet
        FROM penjualan
        GROUP BY nama_produk
        ORDER BY omzet DESC
        '''
    )

    hasil = cursor.fetchall()
    cursor.close()
    conn.close()

    return hasil


def get_rekap_tanggal():
    conn = koneksi_db()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            tanggal,
            SUM(jumlah_terjual) AS total
        FROM penjualan
        GROUP BY tanggal
        ORDER BY tanggal
        '''
    )

    hasil = cursor.fetchall()

    cursor.close()
    conn.close()

    return hasil