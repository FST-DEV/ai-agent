from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

load_dotenv()

app = Flask(__name__)

# Configuration
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

# Hugging Face API configuration
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/"
MODELS = {
    "text_generation": "gpt2",  # Free model for text generation
    "summarization": "facebook/bart-large-cnn"  # Free model for summarization
}

def generate_ai_content(topic, prompt_template):
    """Generate content using Hugging Face free API"""
    try:
        # Using a simple approach with Hugging Face's free inference API
        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN', '')}"}
        
        # For free usage, we'll use a simple text generation approach
        payload = {
            "inputs": prompt_template.format(topic=topic),
            "parameters": {
                "max_length": 1000,  # Increased for more detailed response
                "temperature": 0.7,
                "do_sample": True
            }
        }
        
        response = requests.post(
            f"{HUGGINGFACE_API_URL}{MODELS['text_generation']}",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            ai_response = response.json()[0]["generated_text"]
            # Parse the AI response to extract different sections
            return parse_ai_response(ai_response, topic)
        else:
            # Fallback to a simple template-based generation
            return generate_fallback_content(topic)
            
    except Exception as e:
        print(f"Error generating AI content: {e}")
        return generate_fallback_content(topic)

def parse_ai_response(ai_response, topic):
    """Parse AI response to extract script, title, description, meta tags, and image prompts"""
    try:
        # Initialize content dictionary
        content = {
            'script': '',
            'video_name': '',
            'description': '',
            'meta_tags': '',
            'image_prompts': []
        }
        
        # Split response into sections
        sections = ai_response.split('---')
        
        for section in sections:
            if '**1. Video Script' in section:
                # Extract script
                content['script'] = section.split('**1. Video Script')[1].strip()
            elif '**3. YouTube Shorts Title' in section:
                # Extract video name
                content['video_name'] = section.split('**3. YouTube Shorts Title')[1].strip()
            elif '**4. Video Description' in section:
                # Extract description
                content['description'] = section.split('**4. Video Description')[1].strip()
            elif '**5. Meta Tags' in section:
                # Extract meta tags
                content['meta_tags'] = section.split('**5. Meta Tags')[1].strip()
            elif '**2. AI Image Generation Prompts' in section:
                # Extract image prompts
                prompts_text = section.split('**2. AI Image Generation Prompts')[1].strip()
                # Split into individual prompts (assuming they're separated by newlines)
                prompts = [p.strip() for p in prompts_text.split('\n') if p.strip()]
                content['image_prompts'] = prompts[:7]  # Take first 7 prompts
        
        # If any section is empty, use fallback content
        if not all(content.values()):
            return generate_fallback_content(topic)
            
        return content
        
    except Exception as e:
        print(f"Error parsing AI response: {e}")
        return generate_fallback_content(topic)

def generate_fallback_content(topic):
    """Fallback content generation when AI API fails"""
    
    # Video Script (2-3 minutes)
    script = f"""
🎬 **VIDEO SCRIPT: 5 Interesting and Unknown Facts About {topic}**

[HOOK - First 10 seconds]
Hey there! Did you know that {topic} has some secrets that will absolutely blow your mind? Stick around because you're about to discover 5 fascinating facts about {topic} that almost nobody knows!

[FACT 1]
Here's something incredible: {topic} has been around for much longer than you might think. Scientists have discovered evidence that suggests {topic} has been influencing our world for centuries, and the way it works is absolutely mind-bending. What's even more surprising is that most people use {topic} every single day without even realizing its true potential.

[FACT 2]
Get this: {topic} has some properties that scientists are still trying to fully understand. Recent research has revealed that {topic} behaves in ways that completely defy our expectations. It's like nature decided to play a trick on us, and the more we learn about {topic}, the more mysterious it becomes.

[FACT 3]
This next fact will change how you think about {topic} forever. Did you know that {topic} has played a crucial role in some of the most important discoveries in human history? Without {topic}, many of the things we take for granted today might never have been possible. It's literally been a game-changer throughout history.

[FACT 4]
Here's where it gets really interesting: {topic} has some hidden connections that most people never discover. The way it interacts with other elements in our world is absolutely fascinating, and once you understand these connections, you'll see {topic} in a completely new light.

[FACT 5]
And finally, the most mind-blowing fact of all: {topic} is still evolving and changing even today. Modern technology has given us new ways to understand and utilize {topic}, and what we're discovering now is just the beginning. The future of {topic} is going to be absolutely incredible!

[OUTRO]
If you found these facts about {topic} as fascinating as I do, make sure to hit that like button and follow for more amazing discoveries! There's always something new to learn, and I can't wait to share more incredible facts with you. Thanks for watching!
"""
    
    # YouTube Shorts Title
    video_name = f"5 Unknown Facts About {topic} That Will Shock You! 🤯"
    
    # Video Description
    description = f"Discover 5 mind-blowing and lesser-known facts about {topic} that will completely change how you see the world! From ancient discoveries to modern breakthroughs, this video reveals secrets about {topic} that almost nobody knows. Follow for more amazing facts! 🔔"
    
    # Meta Tags / Hashtags
    meta_tags = f"#shorts #{topic}facts #{topic}shorts #{topic}trivia #curiousfacts #didyouknow #amazingfacts #mindblowing #education #learning #viral #trending #youtubeshorts"
    
    # AI Image Generation Prompts (9:16 vertical aspect ratio)
    # These will be generated by the AI based on the actual content
    image_prompts = [
        # INTRO IMAGE
        f"Epic cinematic 9:16 vertical shot for YouTube Shorts intro: {topic} concept with dramatic golden hour lighting, mysterious fog swirling around, floating holographic text saying '5 Unknown Facts', scientific diagrams and formulas glowing in the background, professional photography style with shallow depth of field, high contrast, cinematic composition, trending on social media aesthetic, perfect for grabbing viewer attention in first 3 seconds",
        
        # FACT 1 IMAGE
        f"Detailed 9:16 vertical illustration for fact 1: {topic} with ancient historical elements, vintage parchment texture background, detailed hand-drawn diagrams and maps, mystical atmosphere with glowing elements, historical accuracy, renaissance-style artwork, intricate details, warm sepia tones, professional illustration quality, perfect for educational content",
        
        # FACT 2 IMAGE
        f"Modern laboratory setting 9:16 vertical shot: {topic} research equipment with clean white background, scientific instruments and microscopes, blue and white LED lighting, professional photography style, high-tech atmosphere, clean minimalist design, perfect for scientific content, trending aesthetic",
        
        # FACT 3 IMAGE
        f"Timeline visualization 9:16 vertical format: {topic} development through history with chronological progression, modern infographic style, clean design, educational illustration, colorful timeline elements, professional graphic design, perfect for educational content, social media optimized",
        
        # FACT 4 IMAGE
        f"Connection network visualization 9:16 vertical shot: {topic} with interconnected elements, neural network style graphics, flowing lines and connections, modern digital art style, vibrant colors, professional illustration, perfect for showing relationships and connections, trending design aesthetic",
        
        # FACT 5 IMAGE
        f"Futuristic visualization 9:16 vertical shot: {topic} applications with sci-fi atmosphere, holographic displays floating in space, advanced technology elements, neon lighting effects, cutting-edge design, cyberpunk aesthetic, professional 3D rendering style, perfect for showing future possibilities",
        
        # OUTRO IMAGE
        f"Engaging 9:16 vertical outro shot: {topic} concept with call-to-action elements, like and subscribe buttons floating, social media icons, vibrant colors, modern design, perfect for encouraging viewer engagement, trending YouTube Shorts aesthetic, professional graphic design, optimized for viewer retention"
    ]
    
    return {
        "script": script,
        "video_name": video_name,
        "description": description,
        "meta_tags": meta_tags,
        "image_prompts": image_prompts
    }

def send_email(content, topic):
    """Send email with generated content"""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"AI Generated Content: {topic}"
        
        # Create email body
        labels = ['INTRO', 'FACT 1', 'FACT 2', 'FACT 3', 'FACT 4', 'FACT 5', 'OUTRO']
        body = f"""
        Topic: {topic}
        
        🎬 VIDEO SCRIPT (2-3 minutes):
        {content['script']}
        
        📺 YOUTUBE SHORTS CONTENT:
        Video Title: {content['video_name']}
        
        Description:
        {content['description']}
        
        Meta Tags: {content['meta_tags']}
        
        🖼️ AI IMAGE GENERATION PROMPTS (9:16 vertical):
        {chr(10).join([f"{labels[i]}: {prompt}" for i, prompt in enumerate(content['image_prompts'])])}
        
        ---
        Generated by AI Agent
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(GMAIL_USER, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        topic = data.get('topic', '').strip()
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Your predefined prompt template
        prompt_template = """
        You are a creative content producer making highly engaging YouTube Shorts with a duration of 2 to 3 minutes.

        Your goal is to create a script titled **"5 Interesting and Unknown Facts About {topic}"** that educates, surprises, and entertains the viewer.

        Here's what I need you to generate based on the topic **{topic}**:

        ---

        🧠 **1. Video Script (2-3 minutes max):**

        - Start with a catchy hook in the first 10 seconds to grab attention.
        - Include 5 interesting, **lesser-known** or surprising facts about the topic.
        - Each fact should be about 3–5 sentences long, and written in a tone that's clear, fun, and informative.
        - Use proper grammar, punctuation, and transitions.
        - End with a strong, curious outro encouraging likes or follows.

        ---

        🖼️ **2. AI Image Generation Prompts:**

        For each of the 5 facts and for intro and outro, provide a **very detailed and vivid visual prompt with 9:16 vertical aspect ratio** that can be used to generate an image (e.g., with DALL·E, Midjourney, or similar tools). The prompts should be clear, specific, and cinematic or visually exciting.

        IMPORTANT: Generate 7 separate image prompts:
        - 1 INTRO image prompt
        - 5 FACT image prompts (one for each fact)
        - 1 OUTRO image prompt

        Each prompt should be very detailed (100+ words) and specifically tailored to the content of that section.

        ---

        🎬 **3. YouTube Shorts Title:**

        Generate a **click-worthy, SEO-friendly, and emotionally intriguing title** with a maximum of 80 characters. Should include a hook or surprising adjective.

        ---

        📄 **4. Video Description (SEO Optimized):**

        - A short paragraph (2–4 lines) explaining what the video covers.
        - Add a subtle CTA (call to action) like "Follow for more amazing facts!"
        - Use keywords relevant to the topic and Shorts audience.

        ---

        🏷️ **5. Meta Tags / Hashtags:**

        List 10–15 **relevant tags and hashtags** for better discoverability on YouTube Shorts. Include both general and niche terms related to the topic, such as:

        - #shorts  
        - #{topic}facts  
        - #{topic}shorts  
        - #{topic}trivia  
        - #curiousfacts  
        - #didyouknow

        ---

        🔁 Repeat the format above for **every new topic** I give you. Always keep the **script length appropriate for a 2–3 minute video** when read at a normal pace (approx. 250–400 words total).
        """
        
        # Generate content
        content = generate_ai_content(topic, prompt_template)
        
        # Send email
        email_sent = send_email(content, topic)
        
        return jsonify({
            'success': True,
            'content': content,
            'email_sent': email_sent,
            'message': 'Content generated and email sent successfully!'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
