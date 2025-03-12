# Ethereum Wallet Generator

Sebuah **Python CLI Tool** untuk **membuat Ethereum wallet** menggunakan **mnemonic** dengan opsi 12 atau 24 kata, serta menyimpannya ke dalam file JSON.

## Fitur
- **Generate Ethereum wallet** dengan **12 atau 24 kata mnemonic**  
- **Menyimpan hasil ke file JSON**  
- **Mendukung CLI untuk mengatur jumlah wallet, jumlah kata mnemonic, dan nama file JSON**  
- **File JSON dibuat otomatis jika belum ada**  

---

## Instalasi
```sh
pip install mnemonic ecdsa
```

## Penggunaan
```sh
python3 main.py --create <jumlah_wallet> --words <12|24> --file <nama_file.json>
```

Argument | Deskripsi
--------- | --------
--create 3 | membuat 3 wallet
--words 12 | menggunakan mnemonic 12/24
--file wallets.json | menyimpan ke file json

## File json
contoh format json
```json
[
    {
        "mnemonic": "oil slight tattoo smile alarm search worry sphere joy side royal fiber ...",
        "private_key": "7a8c1d9f7...",
        "address": "0xA123B456C789..."
    },
    {
        "mnemonic": "wisdom fame luggage recall garden chimney vast mask machine comfort tiger...",
        "private_key": "5e9b0c3a4...",
        "address": "0xB234C567D890..."
    }
]
```

