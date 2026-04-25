import os
import google.generativeai as genai
from datetime import datetime

# 1. Konfigurasi API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY tidak ditemukan di Secrets GitHub.")
    exit(1)

genai.configure(api_key=api_key)

def generate_article():
    """Meminta AI untuk menulis artikel"""
    # Menggunakan Gemini 1.5 Flash (Gratis & Cepat)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = (
        "Buatlah satu artikel blog berkualitas tinggi dalam Bahasa Indonesia. "
        "Topik: Tips teknologi web modern, e-commerce, atau digital marketing untuk UMKM. "
        "Format: Markdown. Harus ada Judul (H1), pendahuluan, minimal 3 sub-bab (H2), dan kesimpulan. "
        "Jangan berikan teks pembuka seperti 'Ini adalah artikel Anda', langsung saja ke isi artikelnya."
    )
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gagal generate artikel: {e}")
        return None

def save_to_markdown(content):
    """Menyimpan hasil AI ke folder posts/"""
    if not content:
        return
    
    # Buat folder posts jika belum ada secara otomatis
    folder = "posts"
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Folder '{folder}' berhasil dibuat.")

    # Nama file unik berdasarkan tanggal dan jam
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    filename = f"{folder}/artikel-{date_str}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"SUKSES: Artikel baru disimpan di {filename}")

if __name__ == "__main__":
    print("Memulai proses pembuatan artikel AI...")
    content = generate_article()
    save_to_markdown(content)
