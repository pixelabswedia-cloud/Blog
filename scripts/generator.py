import google.generativeai as genai
import os
from datetime import datetime

# Konfigurasi API
# Pastikan kamu memasukkan API KEY di GitHub Secrets nanti
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_article():
    # Topik bisa kamu ganti secara dinamis atau ambil dari list
    topic = "The Impact of Artificial Intelligence on Modern Web Design"
    
    prompt = f"""
    Act as a professional tech journalist. Write a 1200-word article about '{topic}'.
    - Target audience: USA/UK (Native English speakers).
    - Tone: Engaging, slightly informal, and empathetic.
    - Style: Use burstiness (mix of short/long sentences), avoid cliché AI phrases.
    - Format: Use Markdown with H2 and H3 tags.
    - Content: Include a practical 'Case Study' or 'Real-world Example' section.
    - Conclusion: End with a unique 'Final Thoughts' section.
    """

    response = model.generate_content(prompt)
    content = response.text

    # Membuat Frontmatter (Metadata untuk Website)
    file_name = f"{topic.lower().replace(' ', '-')}.md"
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    header = f"---\ntitle: \"{topic}\"\ndate: {date_str}\ndraft: false\n---\n\n"
    
    # Simpan ke folder content
    os.makedirs('content', exist_ok=True)
    with open(f"content/{file_name}", "w", encoding="utf-8") as f:
        f.write(header + content)
    
    print(f"Success: {file_name} created.")

if __name__ == "__main__":
    generate_article()
