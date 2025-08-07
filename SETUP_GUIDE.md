# 🚀 AI Agent Setup Guide

## ✅ Current Status

Great news! The basic AI agent is working perfectly. I just tested it with Python 2.7 and it successfully:
- ✅ Generated content for "car"
- ✅ Created 5 interesting facts
- ✅ Generated YouTube Shorts content (title, description, meta tags)
- ✅ Created image prompts
- ✅ Sent email successfully via Gmail SMTP

## 🔧 Next Steps for Full Web Application

### 1. Install Python 3 (Required for Flask Web App)

**Option A: Download from python.org (Recommended)**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 for Windows
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Restart your terminal/PowerShell

**Option B: Using Windows Store**
1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Install the official Python app

**Option C: Using Chocolatey (if you have it)**
```powershell
choco install python
```

### 2. Verify Python 3 Installation

After installing Python 3, run:
```powershell
python --version
# Should show Python 3.x.x (not 2.7.9)
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:
```
GMAIL_USER=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
RECIPIENT_EMAIL=your-email@gmail.com
HUGGINGFACE_TOKEN=your-huggingface-token
```

### 5. Run the Web Application

```powershell
python app.py
```

Then open http://localhost:5000 in your browser.

## 🌐 Free Deployment Guide

### Step 1: Prepare GitHub Repository

1. **Create GitHub Account** (if you don't have one)
   - Go to https://github.com
   - Sign up for a free account

2. **Create New Repository**
   - Click "New repository"
   - Name it `ai-agent`
   - Keep it Public
   - Don't initialize with README

3. **Push Your Code**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

### Step 2: Deploy on Render.com (Recommended)

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub (Free)
   - Authorize Render to access your repositories

2. **Create New Web Service**
   - Click "New +"
   - Select "Web Service"
   - Choose your `ai-agent` repository
   - Click "Connect"

3. **Configure Service**
   - **Name**: `ai-agent` (or your choice)
   - **Environment**: Python 3
   - **Region**: Choose closest to you
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (stays free forever)
   - Click "Advanced" and set:
     - **Auto-Deploy**: Yes
     - **Health Check Path**: /

4. **Add Environment Variables**
   - Click "Environment" tab
   - Add these variables:
     ```
     GMAIL_USER=your-email@gmail.com
     GMAIL_PASSWORD=your-app-password
     RECIPIENT_EMAIL=your-email@gmail.com
     FLASK_ENV=production
     SECRET_KEY=your-secret-key-here
     ```

5. **Deploy and Monitor**
   - Click "Create Web Service"
   - Watch the build logs
   - Wait for "Deploy successful"
   - Your app is live at `https://ai-agent.onrender.com`

### Step 3: Keep Your App Active (Optional)

1. **Set Up UptimeRobot** (Free)
   - Go to https://uptimerobot.com
   - Sign up for free account
   - Add new monitor:
     - Type: HTTP(s)
     - URL: Your Render app URL
     - Interval: 5 minutes

2. **Alternative: Use Cron-Job.org** (Free)
   - Go to https://cron-job.org
   - Sign up for free account
   - Create new cronjob:
     - URL: Your Render app URL
     - Schedule: Every 10 minutes

### Free Tier Limits & Benefits

1. **Render.com Free Tier**
   - ✅ 750 hours/month (enough for 24/7)
   - ✅ 100 GB/month bandwidth
   - ✅ Automatic HTTPS/SSL
   - ✅ Custom domains supported
   - ℹ️ Spins down after 15 min inactivity
   - ℹ️ Spins up automatically on request

2. **Alternative Platforms**

   **Railway.app**
   - ✅ 500 hours/month free
   - ✅ 1GB RAM, 1GB disk
   - ✅ Easy deployment
   - Visit: https://railway.app

   **PythonAnywhere**
   - ✅ Always free tier
   - ✅ Custom domain
   - ✅ Python-specific hosting
   - Visit: https://www.pythonanywhere.com

   **Google Cloud Run**
   - ✅ Generous free tier
   - ✅ Pay-per-use after free tier
   - ✅ Auto-scaling
   - Visit: https://cloud.google.com/run

## 📧 Gmail Setup (Required for Email)

### Step 1: Enable 2-Factor Authentication
1. Go to https://myaccount.google.com/security
2. Enable "2-Step Verification"

### Step 2: Generate App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" from dropdown
3. Click "Generate"
4. Copy the 16-character password

### Step 3: Use App Password
- Use your Gmail address as `GMAIL_USER`
- Use the 16-character app password as `GMAIL_PASSWORD`
- **NEVER use your regular Gmail password**

## 🤖 AI Services Integration

### Current Implementation
- ✅ **Fallback System**: Works without any AI APIs
- ✅ **Template-based Generation**: Creates engaging content
- ✅ **Hugging Face Integration**: Optional free AI enhancement

### Adding More Free AI Services

You can enhance the AI generation by adding:

1. **Hugging Face Free Inference**
   - Get free token at https://huggingface.co/settings/tokens
   - Add to environment variables

2. **Local AI Models**
   - Install Ollama: https://ollama.ai
   - Use local models for free

3. **Free Web APIs**
   - Add more free AI services to `app.py`

## 🔄 Testing Your Setup

### Test 1: Basic Functionality
```powershell
python test_simple.py
```
Enter a topic and test email functionality.

### Test 2: Web Application
```powershell
python app.py
```
Open http://localhost:5000 and test the web interface.

### Test 3: Deployment
After deploying, test your live URL.

## 🐛 Troubleshooting

### Python Version Issues
- **Problem**: `python --version` shows 2.7
- **Solution**: Install Python 3 and ensure it's in PATH

### Email Not Sending
- **Problem**: SMTP authentication failed
- **Solution**: Use App Password, not regular password

### Dependencies Not Installing
- **Problem**: pip install fails
- **Solution**: Upgrade pip: `python -m pip install --upgrade pip`

### Deployment Issues
- **Problem**: Build fails on hosting platform
- **Solution**: Check Python version in `runtime.txt`

## 📁 Project Files Overview

```
ai-agent/
├── app.py                 # Main Flask web application
├── test_simple.py         # Simple test script (Python 2.7 compatible)
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version specification
├── templates/
│   └── index.html        # Beautiful web interface
├── env_example.txt       # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # Main documentation
└── SETUP_GUIDE.md       # This setup guide
```

## 🎯 What You Get

After setup, you'll have:

1. **Web Interface**: Beautiful, responsive web app
2. **Content Generation**: 5 facts + pronunciation + YouTube content
3. **Email Delivery**: Automatic email with generated content
4. **Free Hosting**: Live on the internet
5. **No API Costs**: Completely free to run

## 🚀 Quick Start Commands

```powershell
# 1. Install Python 3 (if not already done)
# Download from python.org

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file with your Gmail credentials

# 4. Run locally
python app.py

# 5. Deploy to Render/Railway/Vercel
# Follow deployment instructions above
```

## 📞 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Verify Python 3 is installed
3. Ensure Gmail App Password is correct
4. Check deployment logs on your hosting platform

---

**🎉 Your AI Agent is ready to generate amazing content!**
