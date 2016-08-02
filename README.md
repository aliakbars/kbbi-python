# KBBI IV Daring

Pustaka ini dibuat untuk mendapatkan keluaran seperti JSON (Anda dapat menggunakan `json.dumps()` pada hasil keluarannya) untuk pencarian arti kata berdasarkan situs http://kbbi4.portalbahasa.com/

## Instalasi

Salin _repository_ ini dengan perintah

    git clone https://github.com/aliakbars/kbbi-python.git

Masuk ke dalam folder yang telah disalin dan lakukan instalasi untuk kebutuhan pustaka lainnya dengan perintah

    pip install -r requirements.txt

Anda dapat menggunakan [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) jika perlu.

## Penggunaan

Untuk pencarian melalui _shell_, Anda dapat menggunakan perintah

    python kbbi.py <kata_yang_ingin_dicari>

Sedangkan penggunaan sebagai pustaka dapat dilakukan seperti berikut

```
>>> import kbbi
>>>
>>> kbbi.cari('contoh')
```
