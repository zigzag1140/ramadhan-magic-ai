import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_key = os.getenv("DASHSCOPE_API_KEY")

# 1. GENERATE CAPTION (Qwen-Max)
def get_caption(msg):
    pro_prompt = f"""
    CONTEXT: Kamu adalah Social Media Specialist ahli konten viral Ramadan Indonesia.
    USER TOPIC: {msg}
    TASK: Buat 1 caption pendek (max 20 kata), lucu/relate, bahasa gaul Jakarta, akhiri 2-3 hashtag unik.
    CONSTRAINT: JANGAN gunakan tanda kutip, langsung berikan teksnya.
    """
    
    url = "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "qwen-max",
        "input": {
            "messages": [{"role": "user", "content": pro_prompt}]
        }
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        res_json = response.json()
        return res_json['output']['text']
    except:
        return "Gagal membuat caption, tapi gambarnya sudah jadi!"

# 2. GENERATE GAMBAR (Wan2.6-T2I) 
def get_image(msg):
    master_visual_prompt = f"""
    ACTION SCENE: A dynamic 3D scene of an Indonesian character: {msg}.
    
    [STRICT VARIATION RULE]
    - Unique environment based on: {msg}.
    - Dynamic camera angle (wide, close-up, or side-view).
    
    [CHARACTER & STYLE]
    - Style: High-end cinematic 3D stylized animation.
    - Character: One Indonesian person, facial expression and clothes MUST match the mood of: {msg}.
    - Lighting: Atmosphere must strictly follow the vibe of: {msg}.
    
    [STRICT NO-TEXT]
    - NO LETTERS, NO WORDS, NO LOGOS ANYWHERE.
    """
    
    url = "https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "wan2.6-t2i",
        "input": {
            "messages": [{"role": "user", "content": [{"text": master_visual_prompt}]}]
        },
        "parameters": {"n": 1, "size": "1024*1024"}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        res_json = response.json()
        if response.status_code == 200:
            choices = res_json.get('output', {}).get('choices', [])
            if choices:
                return choices[0]['message']['content'][0].get('image')
        return None
    except Exception as e:
        print(f"Error Get Image: {str(e)}")
        return None

@app.route('/magic', methods=['POST'])
def magic_endpoint():
    data = request.json or {}
    user_msg = data.get('msg', 'Puasa lemas nunggu bedug')
    
    try:
        caption = get_caption(user_msg)
        image_url = get_image(user_msg)
        
        return jsonify({
            "status": "success",
            "caption": caption,
            "image_url": image_url
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return "Ramadan Magic AI is Live and Solid!", 200

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)