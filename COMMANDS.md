# 🎯 AI Insight Daily - Complete Command Reference

## 📋 ALL COMMANDS YOU'LL NEED

Copy-paste these commands in order for complete setup.

---

## PHASE 1: Initial Setup (Local)

### Navigate to project
```powershell
cd M:\ai-insight-daily
```

### Create virtual environment (optional but recommended)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Create environment file
```powershell
copy .env.example .env
notepad .env
```

**Fill in `.env` with your credentials:**
```env
PERPLEXITY_API_KEY=your_actual_perplexity_key
FROM_EMAIL=your_email@gmail.com
TO_EMAIL=recipient@email.com
APP_PASSWORD=your_gmail_app_password
```

---

## PHASE 2: Test Locally (Optional)

### Load environment variables and run
```powershell
# Load environment
Get-Content .env | ForEach-Object {
    $key, $value = $_ -split '=', 2
    [System.Environment]::SetEnvironmentVariable($key, $value, 'Process')
}

# Run script
cd src
python main.py
cd ..
```

**Expected:** Email sent successfully! ✅

---

## PHASE 3: Git Setup

### Initialize git repository
```powershell
git init
git add .
git commit -m "Initial commit: AI Insight Daily project"
```

---

## PHASE 4: GitHub Repository

### Option A: Using GitHub Website

1. Go to: https://github.com/new
2. Repository name: `ai-insight-daily`
3. Click "Create repository"
4. Run these commands (replace YOUR_USERNAME):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/ai-insight-daily.git
git branch -M main
git push -u origin main
```

### Option B: Using GitHub CLI

```powershell
# If you have GitHub CLI installed
gh repo create ai-insight-daily --public --source=. --remote=origin --push
```

---

## PHASE 5: GitHub Secrets

**Go to:** Repository → Settings → Secrets and variables → Actions → New repository secret

**Add these 4 secrets:**

1. Name: `PERPLEXITY_API_KEY`, Value: `your_perplexity_api_key`
2. Name: `FROM_EMAIL`, Value: `your_email@gmail.com`
3. Name: `TO_EMAIL`, Value: `recipient@email.com`
4. Name: `APP_PASSWORD`, Value: `your_16_char_gmail_password`

---

## PHASE 6: Test GitHub Actions

**Go to:** Actions → Daily AI Concepts Email → Run workflow → Run workflow button

**Wait:** 30-60 seconds for completion

**Check:** 
- ✅ All steps green in Actions
- ✅ Email in your inbox
- ✅ `data/sent_concepts.json` created

---

## 🎉 DONE! 

Your daily AI emails will now arrive automatically every day at 8:00 AM UTC.

---

## 📝 Common Maintenance Commands

### Update code
```powershell
git add .
git commit -m "Description of changes"
git push
```

### Check workflow status
```powershell
# Go to: https://github.com/YOUR_USERNAME/ai-insight-daily/actions
```

### Run tests
```powershell
python -m unittest discover tests
```

### Update dependencies
```powershell
pip install --upgrade -r requirements.txt
pip freeze > requirements.txt
```

---

## 🔧 Customization Commands

### Change email time
```powershell
# Edit .github/workflows/daily_ai_email.yml
# Line 5: - cron: '0 8 * * *'
# Change to your desired time
notepad .github\workflows\daily_ai_email.yml
git add .github/workflows/daily_ai_email.yml
git commit -m "Update email schedule"
git push
```

### Customize email design
```powershell
notepad src\email_template.py
# Make changes
git add src/email_template.py
git commit -m "Update email design"
git push
```

---

## 🐛 Troubleshooting Commands

### View recent workflow logs
```powershell
# Go to: https://github.com/YOUR_USERNAME/ai-insight-daily/actions
# Click latest run → Click job → View logs
```

### Test API connection
```powershell
# Test Perplexity API
curl -X POST https://api.perplexity.ai/chat/completions `
  -H "Authorization: Bearer YOUR_KEY" `
  -H "Content-Type: application/json" `
  -d '{"model":"sonar","messages":[{"role":"user","content":"Test"}]}'
```

### Check Python environment
```powershell
python --version
pip list
```

### Re-run failed workflow
```powershell
# Go to: Actions → Failed run → Re-run all jobs
```

---

## 📊 Monitoring Commands

### Check storage file
```powershell
cat data\sent_concepts.json
# Or open in browser on GitHub
```

### View git history
```powershell
git log --oneline
git log --graph --all
```

### Check repository status
```powershell
git status
git remote -v
```

---

## 🔄 Update Project

### Pull latest changes (if forked)
```powershell
git pull origin main
```

### Sync with upstream (if you forked someone's repo)
```powershell
git remote add upstream https://github.com/ORIGINAL_OWNER/ai-insight-daily.git
git fetch upstream
git merge upstream/main
git push origin main
```

---

## 🎯 Quick Reference

### File Locations
- Main script: `src\main.py`
- Configuration: `src\config.py`
- Email template: `src\email_template.py`
- Workflow: `.github\workflows\daily_ai_email.yml`
- Storage: `data\sent_concepts.json`
- Environment: `.env` (local only, not in git)

### Important URLs
- Perplexity API: https://www.perplexity.ai/
- Gmail App Passwords: https://myaccount.google.com/apppasswords
- GitHub Secrets: https://github.com/YOUR_USERNAME/ai-insight-daily/settings/secrets/actions
- Cron Helper: https://crontab.guru/

---

**Save this file for future reference!**

*All commands tested on Windows PowerShell*
