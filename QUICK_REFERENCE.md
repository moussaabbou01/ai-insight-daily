# 🎯 Quick Reference - AI Insight Daily

Compiled by Moussaab Boutelis.

## 🚀 Common Commands

### Local Development
```powershell
# Setup virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the script
cd src
python main.py

# Run tests
python -m unittest discover tests
```

### Git Commands
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit"

# Push to GitHub
git remote add origin https://github.com/USERNAME/ai-insight-daily.git
git branch -M main
git push -u origin main

# Update after changes
git add .
git commit -m "Update: description"
git push
```

### Environment Variables
```env
# Required in .env file or GitHub Secrets
PERPLEXITY_API_KEY=pplx-xxxxx
FROM_EMAIL=sender@gmail.com
TO_EMAIL=recipient@email.com
APP_PASSWORD=xxxxxxxxxxxxxxxx
```

---

## 🔧 Configuration Locations

| What to Change | File to Edit |
|----------------|--------------|
| Email schedule | `.github/workflows/daily_ai_email.yml` |
| Email design | `src/email_template.py` |
| Number of concepts | `src/ai_generator.py` |
| AI model | `src/config.py` |
| Storage limit | `src/config.py` |

---

## 📅 Cron Schedule Examples

```yaml
# Daily at 8:00 AM UTC
- cron: '0 8 * * *'

# Daily at 6:00 PM UTC
- cron: '0 18 * * *'

# Monday-Friday at 9:00 AM UTC
- cron: '0 9 * * 1-5'

# Every 6 hours
- cron: '0 */6 * * *'

# First day of month at noon
- cron: '0 12 1 * *'
```

**Format:** `minute hour day month day-of-week`  
**Tool:** https://crontab.guru/

---

## 🐛 Quick Troubleshooting

### Email Not Sending
```bash
# Check Gmail settings
1. Enable 2-Step Verification
2. Generate new App Password
3. Verify password in GitHub Secrets (no spaces!)
```

### API Not Working
```bash
# Test Perplexity API
curl -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"sonar","messages":[{"role":"user","content":"Test"}]}'
```

### GitHub Actions Failed
```bash
# View logs
1. Go to Actions tab
2. Click failed workflow
3. Click failed job
4. Expand step to see error
```

---

## 📂 File Structure Quick View

```
ai-insight-daily/
├── src/                    # All Python code
│   ├── main.py            # Entry point
│   ├── config.py          # Settings
│   ├── storage.py         # Data persistence
│   ├── ai_generator.py    # API calls
│   ├── email_template.py  # HTML templates
│   └── email_sender.py    # SMTP logic
├── .github/workflows/     # Automation
├── data/                  # JSON storage
├── tests/                 # Unit tests
└── .env                   # Secrets (local only)
```

---

## ⚡ Quick Actions

### Manual Trigger Workflow
1. GitHub → Actions → Daily AI Concepts Email
2. Run workflow → Select branch → Run

### Update Secrets
1. Settings → Secrets and variables → Actions
2. Click secret name → Update secret

### View Storage
- Check `data/sent_concepts.json` in repository

### Check Logs
- Actions → Latest run → send-daily-email

---

## 🎨 Customization Snippets

### Change Email Colors
```python
# In src/email_template.py
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# Change to your preferred gradient
background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
```

### Add Multiple Recipients
```python
# In src/config.py
self.to_email = "email1@example.com,email2@example.com"
```

### Change Concept Count
```python
# In src/ai_generator.py, line ~47
prompt = f"""Generate 3 new and important concepts...
# Change 5 to your desired number (remember to update in prompt)
```

---

## 📊 Monitor Your Setup

### Check API Usage
- Perplexity Dashboard → Usage
- Stay within free tier limits

### Verify Emails Delivered
- Check inbox and spam folders
- Look for workflow success in Actions

### Storage Health
- Max 100 concepts stored
- Auto-rotates old entries
- View in `data/sent_concepts.json`

---

## 💡 Pro Tips

1. **Test locally first** before pushing to GitHub
2. **Use workflow_dispatch** for manual testing
3. **Monitor spam folder** for first few emails
4. **Star the repo** to track it easily
5. **Fork before modifying** to keep original intact
6. **Use descriptive commits** for easy rollback

---

## 🔗 Important Links

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Perplexity API](https://docs.perplexity.ai/)
- [Cron Helper](https://crontab.guru/)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)
- [VS Code](https://code.visualstudio.com/)

---

**Need detailed help?** → See [SETUP_GUIDE.md](SETUP_GUIDE.md)
