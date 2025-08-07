# 🤖 AI Content Generator

A free AI agent that generates YouTube Shorts content including facts, pronunciation, video titles, descriptions, meta tags, and image prompts. The content is automatically emailed to you.

## ✨ Features

- **Professional Video Scripts**: Generates 2-3 minute YouTube Shorts scripts with hooks, facts, and outros
- **AI Image Generation Prompts**: AI dynamically generates 7 detailed 9:16 vertical prompts (intro + 5 facts + outro) for DALL·E, Midjourney, etc.
- **YouTube Shorts Optimization**: Creates click-worthy titles, SEO descriptions, and trending hashtags
- **Email Delivery**: Automatically emails generated content
- **Beautiful Web Interface**: Modern, responsive design
- **Free Hosting**: Deployed on free platforms
- **No API Costs**: Uses free AI services and hosting

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `env_example.txt` to `.env`
   - Fill in your Gmail credentials:
     - `GMAIL_USER`: Your Gmail address
     - `GMAIL_PASSWORD`: Your Gmail app password (not regular password)
     - `RECIPIENT_EMAIL`: Email where you want to receive content

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the web interface**
   - Open http://localhost:5000
   - Enter a topic and generate content!

### Gmail Setup

To use Gmail SMTP, you need to:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
   - Use this password in your `.env` file

## 🌐 Free Deployment

### Option 1: Render.com (Recommended)

1. **Create a Render account** at https://render.com
2. **Connect your GitHub repository**
3. **Create a new Web Service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. **Add environment variables** in Render dashboard:
   - `GMAIL_USER`
   - `GMAIL_PASSWORD`
   - `RECIPIENT_EMAIL`
   - `HUGGINGFACE_TOKEN` (optional)

### Option 2: Railway.app

1. **Create a Railway account** at https://railway.app
2. **Connect your GitHub repository**
3. **Add environment variables** in Railway dashboard
4. **Deploy automatically**

### Option 3: Heroku (Free tier discontinued)

If you have an existing Heroku account with free dynos:
1. Install Heroku CLI
2. `heroku create your-app-name`
3. `git push heroku main`
4. Add environment variables in Heroku dashboard

## 📧 Email Configuration

The app uses Gmail SMTP to send emails. Make sure to:

1. Use your Gmail address as `GMAIL_USER`
2. Use an App Password (not your regular password) as `GMAIL_PASSWORD`
3. Set `RECIPIENT_EMAIL` to where you want to receive content

## 🤖 AI Services Used

- **Hugging Face**: Free inference APIs for text generation
- **Fallback System**: Template-based generation when AI services are unavailable
- **No API Keys Required**: Works completely free

## 📁 Project Structure

```
ai-agent/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version
├── templates/
│   └── index.html       # Web interface
├── env_example.txt      # Environment variables template
└── README.md           # This file
```

## 🔧 Customization

### Modify the AI Prompt

Edit the `prompt_template` in `app.py`:

```python
prompt_template = """
Your custom prompt here for {topic}.
Make it engaging and educational.
"""
```

### Add More AI Services

You can add more free AI services in the `generate_ai_content` function:

```python
# Add more free AI APIs here
# - Hugging Face Inference API
# - Free tier APIs
# - Local models with Ollama
```

## 🐛 Troubleshooting

### Email Not Sending
- Check your Gmail app password
- Ensure 2FA is enabled
- Verify environment variables are set correctly

### AI Generation Failing
- The app has a fallback system that will work even without AI APIs
- Check if Hugging Face token is valid (optional)

### Deployment Issues
- Ensure all environment variables are set in your hosting platform
- Check the build logs for any dependency issues
- Verify the Procfile is correct

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to contribute by:
- Adding more free AI services
- Improving the UI/UX
- Adding new content generation features
- Optimizing for different platforms

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the deployment logs
3. Ensure all environment variables are configured correctly

---

**Made with ❤️ for free AI content generation**
