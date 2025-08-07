from setuptools import setup, find_packages

setup(
    name="ai-agent",
    version="1.0.0",
    description="AI Agent for content generation",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "requests==2.31.0",
        "beautifulsoup4==4.12.2",
        "python-dotenv==1.0.0",
        "gunicorn==21.2.0",
        "transformers==4.36.2",
        "torch==2.1.2",
        "Pillow==10.1.0",
    ],
    python_requires=">=3.11",
)
