#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple test script for AI Agent (Python 2.7 compatible)
This is a basic version to test the concept before upgrading to Python 3
"""

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
                script_parts = section.split('**1. Video Script')[1].split('\n')
                # Remove any empty lines and the "(2-3 minutes max):" line
                script_parts = [p for p in script_parts if p.strip() and not p.strip().startswith('(')]
                content['script'] = '\n'.join(script_parts).strip()
            elif '**3. YouTube Shorts Title' in section:
                # Extract video name
                title_parts = section.split('\n')
                # Find the line that's not empty and doesn't contain "**3."
                for part in title_parts:
                    if part.strip() and '**3.' not in part:
                        content['video_name'] = part.strip()
                        break
            elif '**4. Video Description' in section:
                # Extract description
                desc_parts = section.split('\n')
                # Find the line that's not empty and doesn't contain "**4." or "(SEO"
                for part in desc_parts:
                    if part.strip() and '**4.' not in part and '(SEO' not in part:
                        content['description'] = part.strip()
                        break
            elif '**5. Meta Tags' in section:
                # Extract meta tags
                tags_parts = section.split('\n')
                # Find the line that's not empty and doesn't contain "**5." or "/"
                for part in tags_parts:
                    if part.strip() and '**5.' not in part and '/' not in part:
                        content['meta_tags'] = part.strip()
                        break
            elif '**2. AI Image Generation Prompts' in section:
                # Extract image prompts
                prompts = []
                current_prompt = []
                lines = section.split('\n')
                for line in lines:
                    line = line.strip()
                    if line:
                        if any(marker in line for marker in ['[INTRO IMAGE]', '[FACT 1 IMAGE]', '[FACT 2 IMAGE]', '[FACT 3 IMAGE]', '[FACT 4 IMAGE]', '[FACT 5 IMAGE]', '[OUTRO IMAGE]']):
                            if current_prompt:
                                prompts.append(' '.join(current_prompt))
                                current_prompt = []
                        elif '**2.' not in line and ':' not in line:
                            current_prompt.append(line)
                if current_prompt:
                    prompts.append(' '.join(current_prompt))
                content['image_prompts'] = prompts[:7]  # Take first 7 prompts
        
        # If any section is empty, use fallback content
        if not all(content.values()):
            return generate_fallback_content(topic)
            
        return content
        
    except Exception as e:
        print("Error parsing AI response: {0}".format(e))
        return generate_fallback_content(topic)

def generate_fallback_content(topic):
    """Generate fallback content for a given topic"""
    # For testing purposes, we'll use a simple template
    content = {
        'script': """
🎬 **VIDEO SCRIPT: 5 Interesting and Unknown Facts About {0}**

[HOOK - First 10 seconds]
Hey there! Did you know that {0} has some secrets that will absolutely blow your mind? Stick around because you're about to discover 5 fascinating facts about {0} that almost nobody knows!

[FACT 1]
Here's something incredible: {0} has been around for much longer than you might think. Scientists have discovered evidence that suggests {0} has been influencing our world for centuries, and the way it works is absolutely mind-bending. What's even more surprising is that most people use {0} every single day without even realizing its true potential.

[FACT 2]
Get this: {0} has some properties that scientists are still trying to fully understand. Recent research has revealed that {0} behaves in ways that completely defy our expectations. It's like nature decided to play a trick on us, and the more we learn about {0}, the more mysterious it becomes.

[FACT 3]
This next fact will change how you think about {0} forever. Did you know that {0} has played a crucial role in some of the most important discoveries in human history? Without {0}, many of the things we take for granted today might never have been possible. It's literally been a game-changer throughout history.

[FACT 4]
Here's where it gets really interesting: {0} has some hidden connections that most people never discover. The way it interacts with other elements in our world is absolutely fascinating, and once you understand these connections, you'll see {0} in a completely new light.

[FACT 5]
And finally, the most mind-blowing fact of all: {0} is still evolving and changing even today. Modern technology has given us new ways to understand and utilize {0}, and what we're discovering now is just the beginning. The future of {0} is going to be absolutely incredible!

[OUTRO]
If you found these facts about {0} as fascinating as I do, make sure to hit that like button and follow for more amazing discoveries! There's always something new to learn, and I can't wait to share more incredible facts with you. Thanks for watching!
""".format(topic),
        'video_name': "5 Unknown Facts About {0} That Will Shock You! 🤯".format(topic),
        'description': "Discover 5 mind-blowing and lesser-known facts about {0} that will completely change how you see the world! From ancient discoveries to modern breakthroughs, this video reveals secrets about {0} that almost nobody knows. Follow for more amazing facts! 🔔".format(topic),
        'meta_tags': "#shorts #{0}facts #{0}shorts #{0}trivia #curiousfacts #didyouknow #amazingfacts #mindblowing #education #learning #viral #trending #youtubeshorts".format(topic),
        'image_prompts': [
            # INTRO IMAGE
            "Epic cinematic 9:16 vertical shot for YouTube Shorts intro: {0} concept with dramatic golden hour lighting, mysterious fog swirling around, floating holographic text saying '5 Unknown Facts', scientific diagrams and formulas glowing in the background, professional photography style with shallow depth of field, high contrast, cinematic composition, trending on social media aesthetic, perfect for grabbing viewer attention in first 3 seconds".format(topic),
            
            # FACT 1 IMAGE
            "Detailed 9:16 vertical illustration for fact 1: {0} with ancient historical elements, vintage parchment texture background, detailed hand-drawn diagrams and maps, mystical atmosphere with glowing elements, historical accuracy, renaissance-style artwork, intricate details, warm sepia tones, professional illustration quality, perfect for educational content".format(topic),
            
            # FACT 2 IMAGE
            "Modern laboratory setting 9:16 vertical shot: {0} research equipment with clean white background, scientific instruments and microscopes, blue and white LED lighting, professional photography style, high-tech atmosphere, clean minimalist design, perfect for scientific content, trending aesthetic".format(topic),
            
            # FACT 3 IMAGE
            "Timeline visualization 9:16 vertical format: {0} development through history with chronological progression, modern infographic style, clean design, educational illustration, colorful timeline elements, professional graphic design, perfect for educational content, social media optimized".format(topic),
            
            # FACT 4 IMAGE
            "Connection network visualization 9:16 vertical shot: {0} with interconnected elements, neural network style graphics, flowing lines and connections, modern digital art style, vibrant colors, professional illustration, perfect for showing relationships and connections, trending design aesthetic".format(topic),
            
            # FACT 5 IMAGE
            "Futuristic visualization 9:16 vertical shot: {0} applications with sci-fi atmosphere, holographic displays floating in space, advanced technology elements, neon lighting effects, cutting-edge design, cyberpunk aesthetic, professional 3D rendering style, perfect for showing future possibilities".format(topic),
            
            # OUTRO IMAGE
            "Engaging 9:16 vertical outro shot: {0} concept with call-to-action elements, like and subscribe buttons floating, social media icons, vibrant colors, modern design, perfect for encouraging viewer engagement, trending YouTube Shorts aesthetic, professional graphic design, optimized for viewer retention".format(topic)
        ]
    }
    return content

def generate_content(topic):
    """Generate content for the given topic"""
    # For testing purposes, we'll simulate an AI response
    ai_response = """
You are a creative content producer making highly engaging YouTube Shorts with a duration of 2 to 3 minutes.

Your goal is to create a script titled **"5 Interesting and Unknown Facts About {0}"** that educates, surprises, and entertains the viewer.

---

🧠 **1. Video Script (2-3 minutes max):**

[HOOK - First 10 seconds]
Hey there! Did you know that {0} has some secrets that will absolutely blow your mind? Stick around because you're about to discover 5 fascinating facts about {0} that almost nobody knows!

[FACT 1]
Here's something incredible: {0} has been around for much longer than you might think. Scientists have discovered evidence that suggests {0} has been influencing our world for centuries, and the way it works is absolutely mind-bending. What's even more surprising is that most people use {0} every single day without even realizing its true potential.

[FACT 2]
Get this: {0} has some properties that scientists are still trying to fully understand. Recent research has revealed that {0} behaves in ways that completely defy our expectations. It's like nature decided to play a trick on us, and the more we learn about {0}, the more mysterious it becomes.

[FACT 3]
This next fact will change how you think about {0} forever. Did you know that {0} has played a crucial role in some of the most important discoveries in human history? Without {0}, many of the things we take for granted today might never have been possible. It's literally been a game-changer throughout history.

[FACT 4]
Here's where it gets really interesting: {0} has some hidden connections that most people never discover. The way it interacts with other elements in our world is absolutely fascinating, and once you understand these connections, you'll see {0} in a completely new light.

[FACT 5]
And finally, the most mind-blowing fact of all: {0} is still evolving and changing even today. Modern technology has given us new ways to understand and utilize {0}, and what we're discovering now is just the beginning. The future of {0} is going to be absolutely incredible!

[OUTRO]
If you found these facts about {0} as fascinating as I do, make sure to hit that like button and follow for more amazing discoveries! There's always something new to learn, and I can't wait to share more incredible facts with you. Thanks for watching!

---

🖼️ **2. AI Image Generation Prompts:**

[INTRO IMAGE]
Epic cinematic 9:16 vertical shot for YouTube Shorts intro: {0} concept with dramatic golden hour lighting, mysterious fog swirling around, floating holographic text saying '5 Unknown Facts', scientific diagrams and formulas glowing in the background, professional photography style with shallow depth of field, high contrast, cinematic composition, trending on social media aesthetic, perfect for grabbing viewer attention in first 3 seconds.

[FACT 1 IMAGE]
Detailed 9:16 vertical illustration for fact 1: {0} with ancient historical elements, vintage parchment texture background, detailed hand-drawn diagrams and maps, mystical atmosphere with glowing elements, historical accuracy, renaissance-style artwork, intricate details, warm sepia tones, professional illustration quality, perfect for educational content.

[FACT 2 IMAGE]
Modern laboratory setting 9:16 vertical shot: {0} research equipment with clean white background, scientific instruments and microscopes, blue and white LED lighting, professional photography style, high-tech atmosphere, clean minimalist design, perfect for scientific content, trending aesthetic.

[FACT 3 IMAGE]
Timeline visualization 9:16 vertical format: {0} development through history with chronological progression, modern infographic style, clean design, educational illustration, colorful timeline elements, professional graphic design, perfect for educational content, social media optimized.

[FACT 4 IMAGE]
Connection network visualization 9:16 vertical shot: {0} with interconnected elements, neural network style graphics, flowing lines and connections, modern digital art style, vibrant colors, professional illustration, perfect for showing relationships and connections, trending design aesthetic.

[FACT 5 IMAGE]
Futuristic visualization 9:16 vertical shot: {0} applications with sci-fi atmosphere, holographic displays floating in space, advanced technology elements, neon lighting effects, cutting-edge design, cyberpunk aesthetic, professional 3D rendering style, perfect for showing future possibilities.

[OUTRO IMAGE]
Engaging 9:16 vertical outro shot: {0} concept with call-to-action elements, like and subscribe buttons floating, social media icons, vibrant colors, modern design, perfect for encouraging viewer engagement, trending YouTube Shorts aesthetic, professional graphic design, optimized for viewer retention.

---

🎬 **3. YouTube Shorts Title:**

5 Unknown Facts About {0} That Will Shock You! 🤯

---

📄 **4. Video Description (SEO Optimized):**

Discover 5 mind-blowing and lesser-known facts about {0} that will completely change how you see the world! From ancient discoveries to modern breakthroughs, this video reveals secrets about {0} that almost nobody knows. Follow for more amazing facts! 🔔

---

🏷️ **5. Meta Tags / Hashtags:**

#shorts #{0}facts #{0}shorts #{0}trivia #curiousfacts #didyouknow #amazingfacts #mindblowing #education #learning #viral #trending #youtubeshorts
""".format(topic)

    # Parse the AI response
    return parse_ai_response(ai_response, topic)

def send_email(content, topic, gmail_user, gmail_password, recipient_email):
    """Send email with generated content"""
    try:
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = recipient_email
        msg['Subject'] = "AI Generated Content: {0}".format(topic)
        
        # Create email body
        labels = ['INTRO', 'FACT 1', 'FACT 2', 'FACT 3', 'FACT 4', 'FACT 5', 'OUTRO']
        body = """
        Topic: {0}
        
        🎬 VIDEO SCRIPT (2-3 minutes):
        {1}
        
        📺 YOUTUBE SHORTS CONTENT:
        Video Title: {2}
        
        Description:
        {3}
        
        Meta Tags: {4}
        
        🖼️ AI IMAGE GENERATION PROMPTS (9:16 vertical):
        {5}
        
        ---
        Generated by AI Agent
        """.format(
            topic,
            content['script'],
            content['video_name'],
            content['description'],
            content['meta_tags'],
            '\n'.join(["{0}: {1}".format(labels[i], prompt) for i, prompt in enumerate(content['image_prompts'])])
        )
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(gmail_user, recipient_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print("Error sending email: {0}".format(e))
        return False

def main():
    """Main function to test the AI agent"""
    print("🤖 AI Content Generator Test")
    print("=" * 40)
    
    # Get topic from user
    topic = raw_input("Enter a topic: ").strip()
    
    if not topic:
        print("Error: Topic is required")
        return
    
    print("\nGenerating content for: {0}".format(topic))
    print("..." * 10)
    
    # Generate content
    content = generate_content(topic)
    
    # Display results
    print("\n" + "=" * 40)
    print("GENERATED CONTENT")
    print("=" * 40)
    
    print("\n🎬 VIDEO SCRIPT (2-3 minutes):")
    print(content['script'])
    
    print("\n📺 YOUTUBE SHORTS CONTENT:")
    print("Video Name: {0}".format(content['video_name']))
    print("Description: {0}".format(content['description']))
    print("Meta Tags: {0}".format(content['meta_tags']))
    
    print("\n🖼️ AI IMAGE GENERATION PROMPTS (9:16 vertical):")
    labels = ['INTRO', 'FACT 1', 'FACT 2', 'FACT 3', 'FACT 4', 'FACT 5', 'OUTRO']
    for i, prompt in enumerate(content['image_prompts']):
        print("{0}: {1}".format(labels[i], prompt))
    
    # Ask if user wants to send email
    send_email_choice = raw_input("\nDo you want to send this via email? (y/n): ").lower()
    
    if send_email_choice == 'y':
        print("\n📧 EMAIL SETUP")
        print("You need to set up Gmail with an App Password:")
        print("1. Enable 2-Factor Authentication on your Gmail")
        print("2. Generate an App Password: Google Account → Security → 2-Step Verification → App passwords")
        print("3. Use the App Password (not your regular password)")
        
        gmail_user = raw_input("Gmail address: ").strip()
        gmail_password = raw_input("Gmail app password: ").strip()
        recipient_email = raw_input("Recipient email: ").strip()
        
        if gmail_user and gmail_password and recipient_email:
            print("\nSending email...")
            if send_email(content, topic, gmail_user, gmail_password, recipient_email):
                print("✅ Email sent successfully!")
            else:
                print("❌ Failed to send email. Check your credentials.")
        else:
            print("❌ Email credentials incomplete.")
    
    print("\n" + "=" * 40)
    print("Test completed! 🎉")
    print("=" * 40)

if __name__ == '__main__':
    main()
