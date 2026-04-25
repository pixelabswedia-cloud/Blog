import google.generativeai as genai
import os
from datetime import datetime

# Konfigurasi API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# MENGGUNAKAN MODEL YANG PASTI ADA
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def generate_article():
    topic = "The Future of Web Development with AI in 2026"
    
    prompt = f"""
    Write a 1200-word professional article in English about '{topic}'.
    Target: USA/UK audience. Tone: Human-like, engaging, and expert.
    Format: Markdown with H2 and H3 tags.
    """

    try:
        response = model.generate_content(prompt)
        content = response.text

        # Metadata
        file_name = f"{topic.lower().replace(' ', '-')}.md"
        date_str = datetime.now().strftime("%Y-%m-%d")
        header = f"---\ntitle: \"{topic}\"\ndate: {date_str}\ndraft: false\n---\n\n"
        
        os.makedirs('content', exist_ok=True)
        with open(f"content/{file_name}", "w", encoding="utf-8") as f:
            f.write(header + content)
        
        print(f"Success: {file_name} created.")
    except Exception as e:
        print(f"Error during generation: {e}")

if __name__ == "__main__":
    generate_article()
