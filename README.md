# Latihan CI/CD — Quality Gate Coverage ≥ 80%

Repository latihan Tugas Akhir: pipeline CI yang menjalankan lint, format check,
test, dan coverage gate minimal 80%, dengan pre-commit hook dan branch protection.

## Ringkasan Pipeline CI

Workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml) (`CI Code Quality`)

Berjalan pada `push` ke `main`/`fitur-coverage` dan pada setiap `pull_request` ke `main`.

| Langkah | Perintah | Tujuan |
| --- | --- | --- |
| Lint | `ruff check .` | Menolak error gaya penulisan dan import bermasalah |
| Format Check | `black --check .` | Memastikan format konsisten (tanpa mengubah file) |
| Test + Coverage | `pytest --cov=. --cov-report=xml --cov-fail-under=80` | Menjalankan test dan menolak hasil jika coverage < 80% |
| Upload Codecov | `codecov/codecov-action@v4` | Publikasi laporan coverage ke Codecov (opsional) |

## Threshold Coverage

- Minimal **80%**, ditetapkan lewat `--cov-fail-under=80`.
- Jika coverage turun di bawah 80%, langkah test gagal dan pipeline berstatus merah,
  sehingga merge ke `main` terblokir oleh branch protection.
- Saat ini seluruh fungsi di `main.py` (`tambah`, `kurang`, `kali`) teruji,
  sehingga coverage mencapai **100%**.

## Menjalankan Lint dan Test Secara Lokal

```bash
# 1. Siapkan virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. Install dependensi
pip install -r requirements.txt

# 3. Pasang pre-commit hook (sekali saja per clone)
pre-commit install

# 4. Jalankan seluruh pemeriksaan
ruff check .
black --check .
pytest --cov=. --cov-report=term-missing --cov-fail-under=80
```

Untuk menjalankan hook secara manual pada semua file:

```bash
pre-commit run --all-files
```

Untuk melihat baris yang belum ter-cover, tambahkan `--cov-report=term-missing`
(opsional dengan `--cov-report=html` lalu buka `htmlcov/index.html`).

## Struktur Proyek

```
.
├── .github/workflows/ci.yml   # pipeline CI
├── .pre-commit-config.yaml    # hook ruff + ruff-format
├── main.py                    # fungsi tambah, kurang, kali
├── test_main.py               # test pytest
├── pyproject.toml             # konfigurasi ruff dan black
└── requirements.txt           # dependensi dengan versi ter-pin
```

## Alur Kontribusi (Quality Gate)

1. Buat branch baru: `git checkout -b nama-fitur`.
2. Commit perubahan; pre-commit hook otomatis memeriksa kode.
3. Push branch lalu buka Pull Request ke `main`.
4. Tunggu seluruh status check hijau — merge baru diizinkan setelah itu.

## Catatan Codecov (Opsional)

Upload ke Codecov hanya berjalan bila secret `CODECOV_TOKEN` sudah diisi di
**Settings → Secrets and variables → Actions**. Tanpa token, langkah upload
dilewati agar pipeline tetap hijau; langkah test dan coverage gate tetap berjalan.
