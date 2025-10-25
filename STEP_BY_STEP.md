# 📝 Step-by-Step Guide: From Zero to Automated AI Emails

This is your complete walkthrough to get AI Insight Daily running. Follow each step carefully!

Guide prepared by Moussaab Boutelis, creator of AI Insight Daily.

---

## ⏱️ Time Required: 15-20 Minutes

---

## 📋 Checklist

Before you begin, ensure you have:
- [ ] GitHub account
- [ ] Gmail account
- [ ] Git installed on your computer
- [ ] Python 3.11+ installed
- [ ] Internet connection

---

## 🎯 PHASE 1: Get Your API Credentials (5 minutes)

### Step 1.1: Get Perplexity API Key

1. **Open browser** and go to: https://www.perplexity.ai/
2. **Click** "Sign Up" (or "Log In" if you have an account)
3. After logging in, **click your profile icon** (top-right)
4. **Select** "API"
5. **Click** "Generate New API Key"
6. **Copy** the key (format: `pplx-abc123...`)
7. **Save it** in a text file temporarily (you'll need it later)

✅ **You should have:** A long string starting with `pplx-`

---

### Step 1.2: Generate Gmail App Password

1. **Open browser** and go to: https://myaccount.google.com/
2. **Click** "Security" in the left menu
3. **Find** "2-Step Verification"
   - If it says "Off", **click it** and follow steps to enable
   - If already on, continue to next step
4. **Scroll down** to "App passwords" (near bottom of page)
5. **Click** "App passwords"
6. **Select app:** Choose "Mail"
7. **Select device:** Choose "Other (Custom name)"
8. **Type:** "AI Insight Daily"
9. **Click** "Generate"
10. **Copy** the 16-character password (format: `xxxx xxxx xxxx xxxx`)
11. **Remove spaces** → becomes: `xxxxxxxxxxxxxxxx`
12. **Save it** in your text file

✅ **You should have:** 16-character password (no spaces)

---

## 🎯 PHASE 2: Set Up Your Local Project (5 minutes)

### Step 2.1: Navigate to Your Project

Open PowerShell and run:

```powershell
# Go to your project folder
cd M:\ai-insight-daily

# Verify you're in the right place
ls
```

You should see files like: `README.md`, `requirements.txt`, `src/`, etc.

---

### Step 2.2: Create Local Environment File

```powershell
# Copy the example file
copy .env.example .env

# Open it for editing
notepad .env
```

In Notepad, **replace** the placeholder values:

```env
PERPLEXITY_API_KEY=pplx-YOUR_ACTUAL_KEY_HERE
FROM_EMAIL=your_email@gmail.com
TO_EMAIL=recipient@email.com  # Can be same as FROM_EMAIL
APP_PASSWORD=your16charpassword
```

**Save** and **close** Notepad.

✅ **You should have:** `.env` file with your real credentials

---

### Step 2.3: Test Locally (Optional but Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Load environment variables
Get-Content .env | ForEach-Object {
    $key, $value = $_ -split '=', 2
    [System.Environment]::SetEnvironmentVariable($key, $value, 'Process')
}

# Run the script
cd src
python main.py
```

**Expected output:**
```
==================================================
AI INSIGHT DAILY - Starting Daily Email Process
==================================================
[1/6] Validating configuration...
✅ Configuration validated successfully
...
✅ DAILY EMAIL SENT SUCCESSFULLY!
==================================================
```

**Check your email inbox!** You should receive the first AI concepts email.

✅ **You should have:** Email with 5 AI concepts

---

## 🎯 PHASE 3: Create GitHub Repository (3 minutes)

### Step 3.1: Initialize Git Repository

```powershell
# Make sure you're in the project root
cd M:\ai-insight-daily

# Initialize git
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: AI Insight Daily"
```

---

### Step 3.2: Create GitHub Repository

**Option A: Using GitHub Website**

1. Go to: https://github.com/new
2. **Repository name:** `ai-insight-daily`
3. **Description:** "Automated daily AI learning via email"
4. **Visibility:** Public (or Private if you prefer)
5. **Do NOT** check any initialization options
6. **Click** "Create repository"

**Option B: Using GitHub CLI (if installed)**

```powershell
gh repo create ai-insight-daily --public --source=. --remote=origin --push
```

---

### Step 3.3: Push Code to GitHub

If you used Option A above:

```powershell
# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-insight-daily.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Refresh GitHub page** - you should see all your files!

✅ **You should have:** Repository with all project files on GitHub

---

## 🎯 PHASE 4: Configure GitHub Secrets (5 minutes)

### Step 4.1: Navigate to Secrets Settings

1. **Go to** your repository on GitHub
2. **Click** "Settings" (top menu bar)
3. **Click** "Secrets and variables" in left sidebar
4. **Click** "Actions"
5. **Click** "New repository secret" (green button)

---

### Step 4.2: Add Secret #1 - PERPLEXITY_API_KEY

1. **Name:** `PERPLEXITY_API_KEY` (exactly like this, case-sensitive)
2. **Secret:** Paste your Perplexity API key (from Step 1.1)
3. **Click** "Add secret"

---

### Step 4.3: Add Secret #2 - FROM_EMAIL

1. **Click** "New repository secret" again
2. **Name:** `FROM_EMAIL`
3. **Secret:** Your Gmail address (e.g., `yourname@gmail.com`)
4. **Click** "Add secret"

---

### Step 4.4: Add Secret #3 - TO_EMAIL

1. **Click** "New repository secret" again
2. **Name:** `TO_EMAIL`
3. **Secret:** Recipient email (can be same as FROM_EMAIL)
4. **Click** "Add secret"

---

### Step 4.5: Add Secret #4 - APP_PASSWORD

1. **Click** "New repository secret" again
2. **Name:** `APP_PASSWORD`
3. **Secret:** Your 16-character Gmail app password (from Step 1.2, NO SPACES)
4. **Click** "Add secret"

---

### Step 4.6: Verify Secrets

You should now see **4 secrets** listed:
- PERPLEXITY_API_KEY
- FROM_EMAIL
- TO_EMAIL
- APP_PASSWORD

✅ **You should have:** All 4 secrets added correctly

---

## 🎯 PHASE 5: Enable and Test GitHub Actions (2 minutes)

### Step 5.1: Enable Workflows

1. **Click** "Actions" tab (top of repository)
2. If you see a prompt about workflows:
   - **Click** "I understand my workflows, go ahead and enable them"
3. You should see: "Daily AI Concepts Email" workflow

---

### Step 5.2: Run Manual Test

1. **Click** "Daily AI Concepts Email" (in left sidebar)
2. **Click** "Run workflow" button (right side)
3. **Select** branch: `main`
4. **Click** "Run workflow" (green button)
5. **Wait** 5 seconds, then **refresh** the page
6. You should see a workflow run appear
7. **Click** on it to watch progress
8. Wait for all steps to complete (~30-60 seconds)

---

### Step 5.3: Verify Success

**In GitHub:**
- All steps should show ✅ green checkmarks
- A new file appears: `data/sent_concepts.json`

**In Your Email:**
- Check inbox (and spam folder)
- You should see: "🤖 AI Insight Daily: 5 Concepts, 5 Minutes"
- Open it - beautiful HTML email with 5 AI concepts!

✅ **You should have:** 
- Successful workflow run
- Email received with AI concepts
- `data/sent_concepts.json` created

---

## 🎯 PHASE 6: Configure Daily Schedule (1 minute)

The workflow is already set to run **daily at 8:00 AM UTC**.

**To change the time:**

1. **Go to** your repository
2. **Click** `.github/workflows/daily_ai_email.yml`
3. **Click** pencil icon (Edit this file)
4. **Find** line 5: `- cron: '0 8 * * *'`
5. **Change** to your preferred time:
   - `0 6 * * *` → 6:00 AM UTC
   - `0 14 * * *` → 2:00 PM UTC
   - `30 9 * * 1-5` → 9:30 AM UTC, weekdays only
6. **Click** "Commit changes"
7. **Add message:** "Update schedule to X:XX UTC"
8. **Click** "Commit changes"

**Time zone converter:** https://www.worldtimebuddy.com/

✅ **You're done!** The workflow will now run automatically every day.

---

## 🎉 SUCCESS CHECKLIST

Verify everything is working:

- [x] Perplexity API key obtained
- [x] Gmail app password generated
- [x] Local test successful (optional)
- [x] GitHub repository created
- [x] All 4 secrets added
- [x] GitHub Actions enabled
- [x] Manual workflow run successful
- [x] Email received with AI concepts
- [x] Daily schedule configured

---

## 🔮 What Happens Next?

Starting tomorrow (and every day):

1. **8:00 AM UTC** (or your chosen time) → GitHub Actions triggers
2. **Script runs** → Generates 5 new AI concepts (avoiding duplicates)
3. **Email sent** → Beautiful HTML email arrives in your inbox
4. **Storage updated** → `data/sent_concepts.json` tracks sent topics
5. **Repeat tomorrow** → Fresh concepts every day!

**Cost:** $0/month (free tier for everything!)

---

## 📊 Monitoring Your Setup

### Daily Checks (Optional)
- **Check inbox** each morning for email
- **Check spam** if email missing
- **View Actions tab** to see workflow history

### Weekly Checks (Recommended)
- **Review** `data/sent_concepts.json` to see topics covered
- **Monitor** Perplexity API usage (stay within limits)
- **Verify** workflows still running successfully

### Monthly Checks
- **Update** dependencies: `pip list --outdated`
- **Review** and star GitHub repo
- **Share** with friends who want to learn AI!

---

## 🆘 Common Issues & Solutions

### Issue: "Secrets not found" in workflow logs

**Solution:**
1. Verify secret names match EXACTLY (case-sensitive)
2. No typos: `PERPLEXITY_API_KEY`, `FROM_EMAIL`, `TO_EMAIL`, `APP_PASSWORD`
3. Re-create secrets if unsure

---

### Issue: Email not received

**Solution:**
1. Check spam/junk folder
2. Verify FROM_EMAIL and APP_PASSWORD are correct
3. Test sending email from Gmail web interface
4. Check workflow logs for error messages

---

### Issue: API Error 401 Unauthorized

**Solution:**
1. Verify Perplexity API key is correct
2. Check API key hasn't expired
3. Ensure no extra spaces in secret value
4. Test API with curl (see QUICK_REFERENCE.md)

---

### Issue: Workflow not running daily

**Solution:**
1. Check Actions are enabled: Settings → Actions → General
2. Verify cron schedule syntax is correct
3. Wait - sometimes delayed by a few minutes
4. Check GitHub status page for outages

---

## 🎓 You Did It!

Congratulations! You now have:

✨ **Automated AI learning** delivered daily  
✨ **No maintenance required** - runs forever  
✨ **$0 cost** - completely free  
✨ **Professional setup** - using industry best practices  

---

## 📚 Next Steps

1. **Customize** email design (see `src/email_template.py`)
2. **Add features** (see Roadmap in README.md)
3. **Share** your setup with others
4. **Star** the repository on GitHub
5. **Contribute** improvements back to the project

---

## 🤝 Need Help?

- 📖 **Documentation:** [README.md](README.md)
- 🔧 **Quick Reference:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- 🐛 **Troubleshooting:** [SETUP_GUIDE.md](SETUP_GUIDE.md#-troubleshooting)
- 💬 **Issues:** Open issue on GitHub

---

**Happy Learning! 🚀🤖**

*You're now receiving daily AI insights automatically. Enjoy the journey!*
