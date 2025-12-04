# 🎨 AI Image Generator - Full Stack DALL·E App

Website full-stack untuk generate gambar menggunakan OpenAI DALL·E dengan berbagai style artistik.

## ✨ Fitur

- 📤 Upload foto dari HP/laptop dengan drag & drop
- 🎨 7 pilihan style: Anime, Cyberpunk, Studio Ghibli, Realism, Oil Painting, Cartoon, Fantasy
- ⚡ Loading spinner yang smooth
- 📥 Download hasil otomatis
- 🌙 Dark mode dengan gradient background animasi
- 📱 100% responsive (mobile-friendly)
- 🚀 Siap deploy ke Railway, Render, atau VPS

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML + Tailwind CSS + Vanilla JavaScript
- **AI**: OpenAI DALL·E API
- **Deployment**: Railway / Render / Vercel / VPS

## 📁 Struktur Project

```
ai-image-generator/
├── main.py                 # FastAPI backend
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (jangan commit!)
├── .env.example           # Template .env
├── static/
│   └── index.html         # Frontend UI
├── uploads/               # Folder temporary upload
└── generated/             # Folder hasil generate
```

## 🚀 Quick Start (Local)

### 1. Clone & Setup

```bash
# Clone atau download project
git clone <your-repo-url>
cd ai-image-generator

# Install dependencies
pip install -r requirements.txt
```

### 2. Setup OpenAI API Key

```bash
# Copy .env.example ke .env
cp .env.example .env

# Edit .env dan masukkan API key kamu
# Dapatkan API key dari: https://platform.openai.com/api-keys
```

Edit file `.env`:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
PORT=8000
```

### 3. Jalankan Server

```bash
python main.py
```

Buka browser: `http://localhost:8000`

## 🌐 Deploy ke Railway

### Cara Tercepat (1-Click Deploy)

1. Push code ke GitHub
2. Buka [Railway.app](https://railway.app)
3. Klik "New Project" → "Deploy from GitHub"
4. Pilih repository kamu
5. Tambahkan environment variable:
   - Key: `OPENAI_API_KEY`
   - Value: `sk-your-api-key`
6. Railway akan auto-deploy!

### Manual Setup

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up

# Set environment variable
railway variables set OPENAI_API_KEY=sk-your-key
```

Railway akan auto-detect Python dan run `uvicorn main:app`

## 🚢 Deploy ke Render

1. Push code ke GitHub
2. Buka [Render.com](https://render.com)
3. Klik "New Web Service"
4. Connect repository
5. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Tambahkan Environment Variable:
   - `OPENAI_API_KEY`: your-api-key
7. Deploy!

## ☁️ Deploy ke VPS (Linux)

```bash
# SSH ke VPS
ssh user@your-vps-ip

# Install Python & dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx

# Clone project
git clone <your-repo>
cd ai-image-generator

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup .env
nano .env
# Paste API key, save dengan Ctrl+X

# Install & setup Supervisor (auto restart)
sudo apt install supervisor
sudo nano /etc/supervisor/conf.d/ai-generator.conf
```

Paste config ini:
```ini
[program:ai-generator]
directory=/home/user/ai-image-generator
command=/home/user/ai-image-generator/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
user=user
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/ai-generator.log
```

```bash
# Start service
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start ai-generator

# Setup Nginx reverse proxy
sudo nano /etc/nginx/sites-available/ai-generator
```

Paste config:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/ai-generator /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Setup SSL (optional, recommended)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## 🔧 Troubleshooting

### Error: "OpenAI API key not found"
- Pastikan file `.env` ada dan berisi `OPENAI_API_KEY=sk-...`
- Di platform cloud (Railway/Render), set di Environment Variables

### Error: "Image too large"
- Backend otomatis resize gambar ke max 1024x1024
- Jika masih error, coba upload gambar yang lebih kecil (<5MB)

### Error: "DALL·E API quota exceeded"
- API key kamu kehabisan quota
- Beli credit di OpenAI: https://platform.openai.com/account/billing

### Generate lambat
- Normal, DALL·E butuh 10-20 detik
- Jika >30 detik, check koneksi internet

## 💰 Biaya

- **OpenAI DALL·E 3**: $0.04 per image (1024x1024)
- **Railway**: $5/month (500 jam gratis pertama)
- **Render**: Free tier tersedia
- **VPS**: Mulai $5/month (Digital Ocean, Vultr, dll)

## 📝 Catatan Penting

1. **JANGAN commit file `.env`** - sudah ada di `.gitignore`
2. **Gunakan HTTPS di production** - Railway/Render otomatis provide SSL
3. **Rate limiting**: Tambahkan jika traffic tinggi untuk avoid abuse
4. **Storage**: Generated images disimpan di server, setup cleanup cron job jika perlu

## 🎯 Next Features (Optional)

- [ ] History generated images per user
- [ ] Authentication (login/register)
- [ ] Multiple image generation
- [ ] Image upscaling
- [ ] Custom prompts
- [ ] Payment integration (Stripe)
- [ ] Social sharing

## 📄 License

MIT License - Feel free to use for personal/commercial projects

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

**Happy Creating! 🎨✨**

Jika ada pertanyaan, buka issue di GitHub atau DM developer.