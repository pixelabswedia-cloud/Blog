import os
import openai
from datetime import datetime

# Konfigurasi API
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_article():
    prompt = "Buatlah satu artikel blog pendek tentang tren teknologi web tahun 2026 dalam Bahasa Indonesia. Gunakan format Markdown, sertakan Judul (H1) dan beberapa sub-bab (H2)."
    
    response = openai.ChatCompletion.create(
        model="gpt-4o", # Anda bisa ganti ke gpt-3.5-turbo jika ingin lebih hemat
        messages=[{"role": "user", "content": prompt}]
    )
    
    content = response.choices[0].message.content
    return content

def save_to_markdown(content):
    # Membuat nama file berdasarkan tanggal agar unik
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filename = f"posts/artikel-{date_str}.md"
    
    # Pastikan folder 'posts' ada
    os.makedirs("posts", exist_ok=True)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Artikel berhasil disimpan: {filename}")

if __name__ == "__main__":
    article_content = generate_article()
    save_to_markdown(article_content)
