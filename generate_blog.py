import os
import google.generativeai as genai
from datetime import datetime

# Konfigurasi Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_article():
    # Menggunakan model Flash (Gratis & Cepat)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "Buatlah satu artikel blog tentang tips web development atau e-commerce di Indonesia. Gunakan format Markdown lengkap dengan judul dan sub-judul."
    
    response = model.generate_content(prompt)
    return response.text

def save_to_markdown(content):
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    filename = f"posts/artikel-{date_str}.md"
    
    os.makedirs("posts", exist_ok=True)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Berhasil membuat: {filename}")

if __name__ == "__main__":
    try:
        text = generate_article()
        save_to_markdown(text)
    except Exception as e:
        print(f"Error: {e}")
