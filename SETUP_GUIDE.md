# 📋 Complete GitHub Setup Guide for AI Insight Daily

This guide will walk you through setting up the AI Insight Daily project on GitHub with automated daily emails.

## 🎯 Overview

By the end of this guide, you'll have:
- ✅ A GitHub repository with the project code
- ✅ Automated daily emails with AI concepts
- ✅ No server costs (runs free on GitHub Actions)

---

## 📦 Prerequisites

Before starting, make sure you have:

1. **GitHub Account** - [Sign up free](https://github.com/join)
2. **Gmail Account** - For sending emails
3. **Perplexity API Key** - [Get it free](https://www.perplexity.ai/)
4. **Git Installed** - [Download Git](https://git-scm.com/downloads)

---

## 🚀 Step-by-Step Setup

### Step 1: Get Perplexity API Key

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Sign up or log in to your account
3. Navigate to **Settings** → **API**
4. Click **"Generate New API Key"**
5. Copy and save the API key securely (you'll need it later)

**Example:** `pplx-abc123def456...`

---

### Step 2: Generate Gmail App Password

**Important:** You need 2-Step Verification enabled for this.

1. Go to your [Google Account](https://myaccount.google.com/)
2. Click **Security** in the left sidebar
3. Under "Signing in to Google", find **2-Step Verification**
   - If not enabled, click to enable it first
4. Once enabled, scroll down to **App Passwords**
5. Click **App Passwords**
6. In the "Select app" dropdown, choose **Mail**
7. In the "Select device" dropdown, choose **Other (Custom name)**
8. Type: `AI Insight Daily`
9. Click **Generate**
10. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)
11. Save it securely - you can't see it again!

**Note:** Remove the spaces when using it: `xxxxxxxxxxxxxxxx`

---

### Step 3: Create GitHub Repository

#### Option A: Using GitHub Web Interface

1. Go to [GitHub](https://github.com/) and log in
2. Click the **"+"** icon in the top-right
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name:** `ai-insight-daily`
   - **Description:** "Automated daily AI learning via email"
   - **Visibility:** Choose **Public** or **Private**
   - **✅ Check:** "Add a README file" (optional, we'll replace it)
   - **Don't** initialize with .gitignore or license (we have those)
5. Click **"Create repository"**

#### Option B: Using Git Command Line

```bash
# Navigate to your project folder
cd M:\ai-insight-daily

# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: AI Insight Daily project"

# Create repository on GitHub (replace YOUR_USERNAME)
gh repo create ai-insight-daily --public --source=. --remote=origin --push
```

**If you don't have GitHub CLI (`gh`):**

```bash
# After creating empty repo on GitHub.com, run:
git remote add origin https://github.com/YOUR_USERNAME/ai-insight-daily.git
git branch -M main
git push -u origin main
```

---

### Step 4: Configure GitHub Secrets

Secrets keep your API keys and passwords secure.

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **"New repository secret"** button

Add these **4 secrets** one by one:

#### Secret 1: PERPLEXITY_API_KEY
- **Name:** `PERPLEXITY_API_KEY`
- **Value:** Your Perplexity API key (from Step 1)
- Click **Add secret**

#### Secret 2: FROM_EMAIL
- **Name:** `FROM_EMAIL`
- **Value:** Your Gmail address (e.g., `yourname@gmail.com`)
- Click **Add secret**

#### Secret 3: TO_EMAIL
- **Name:** `TO_EMAIL`
- **Value:** Recipient email (can be same as FROM_EMAIL)
- Click **Add secret**

#### Secret 4: APP_PASSWORD
- **Name:** `APP_PASSWORD`
- **Value:** Your Gmail App Password (from Step 2, without spaces)
- Click **Add secret**

**✅ Verification:** You should now see 4 secrets listed.

---

### Step 5: Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If you see a prompt to enable workflows, click **"I understand my workflows, go ahead and enable them"**
3. You should see the workflow: **"Daily AI Concepts Email"**

---

### Step 6: Test the Workflow (Manual Run)

Before waiting for the daily schedule, test it manually:

1. Go to **Actions** tab
2. Click on **"Daily AI Concepts Email"** in the left sidebar
3. Click the **"Run workflow"** dropdown on the right
4. Select branch: **main**
5. Click **"Run workflow"** button (green)
6. Wait 30-60 seconds, then refresh the page
7. You should see a workflow run appear
8. Click on it to see the progress
9. Check your email inbox for the AI concepts!

**Expected output:**
- ✅ Green checkmarks for all steps
- ✅ Email in your inbox with 5 AI concepts
- ✅ File `data/sent_concepts.json` created in repo

---

### Step 7: Configure Daily Schedule (Optional)

The workflow runs daily at **8:00 AM UTC** by default.

**To change the time:**

1. Open `.github/workflows/daily_ai_email.yml`
2. Find this line:
   ```yaml
   - cron: '0 8 * * *'  # 8:00 AM UTC
   ```
3. Change the time using cron syntax:
   - `0 8` = 8:00 AM UTC
   - `0 14` = 2:00 PM UTC
   - `30 9` = 9:30 AM UTC
   
4. Save and commit the file

**Cron Format:** `minute hour day month day-of-week`

**Examples:**
- `0 6 * * *` - 6:00 AM UTC daily
- `0 18 * * *` - 6:00 PM UTC daily
- `0 9 * * 1-5` - 9:00 AM UTC, Monday-Friday only

**Time Zone Converter:** [WorldTimeBuddy](https://www.worldtimebuddy.com/)

---

## 🧪 Local Testing (Optional)

Test the project on your computer before deploying:

### 1. Set up Python environment

```powershell
# Navigate to project folder
cd M:\ai-insight-daily

# Create virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Create `.env` file

```powershell
# Copy the example file
copy .env.example .env

# Edit .env with your actual values
notepad .env
```

Fill in:
```env
PERPLEXITY_API_KEY=your_actual_api_key
FROM_EMAIL=your_email@gmail.com
TO_EMAIL=recipient@email.com
APP_PASSWORD=your_app_password
```

### 3. Run the script

```powershell
# Load environment variables (PowerShell)
Get-Content .env | ForEach-Object {
    $key, $value = $_ -split '=', 2
    [System.Environment]::SetEnvironmentVariable($key, $value, 'Process')
}

# Run the script
cd src
python main.py
```

### 4. Check output

You should see:
```
==================================================
AI INSIGHT DAILY - Starting Daily Email Process
==================================================

[1/6] Validating configuration...
✅ Configuration validated successfully

[2/6] Initializing storage...
✅ Loaded 0 previously sent concepts

[3/6] Generating 5 new AI concepts...
✅ Generated concepts: [...]

[4/6] Creating HTML email template...
✅ Email template created

[5/6] Sending email...
✅ Email sent successfully to recipient@email.com

[6/6] Updating concept storage...
✅ Storage updated. Total concepts tracked: 5

==================================================
✅ DAILY EMAIL SENT SUCCESSFULLY!
==================================================
```

---

## 🔧 Customization Options

### Change Number of Concepts

Edit `src/ai_generator.py`:
```python
# Change "5 new" to your desired number
prompt = f"""Generate 3 new and important concepts...
```

### Customize Email Design

Edit `src/email_template.py`:
- Change colors in the `background: linear-gradient(...)` line
- Modify fonts, spacing, or layout
- Add your logo or branding

### Change AI Model

Edit `src/config.py`:
```python
self.model_name = "sonar-pro"  # Or other Perplexity models
```

### Add Multiple Recipients

Edit `src/email_sender.py`, change:
```python
msg['To'] = to_email
```
To:
```python
msg['To'] = ", ".join(['email1@example.com', 'email2@example.com'])
```

---

## 🐛 Troubleshooting

### Issue: "Workflow not running"

**Solution:**
1. Check Actions are enabled: Settings → Actions → General
2. Verify workflow file is in `.github/workflows/`
3. Check for YAML syntax errors

### Issue: "API Error 401 Unauthorized"

**Solution:**
- Verify your Perplexity API key in GitHub Secrets
- Check key hasn't expired
- Ensure no extra spaces in the secret value

### Issue: "Email not sending"

**Solution:**
1. Verify Gmail App Password is correct (no spaces)
2. Check 2-Step Verification is enabled on Gmail
3. Look at workflow logs for specific error
4. Try sending test email from Gmail web interface

### Issue: "No concepts generated"

**Solution:**
- Check Perplexity API quota/limits
- Verify API response in workflow logs
- Test API key with curl:
  ```bash
  curl -X POST https://api.perplexity.ai/chat/completions \
    -H "Authorization: Bearer YOUR_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"sonar","messages":[{"role":"user","content":"Hello"}]}'
  ```

### Issue: "Secrets not found"

**Solution:**
- Secret names must match exactly (case-sensitive)
- Re-create secrets if unsure
- Check you're looking at the correct repository

---

## 📊 Monitoring

### View Workflow History

1. Go to **Actions** tab
2. See all past runs with status (✅ success or ❌ failed)
3. Click any run to see detailed logs

### Check Concept Storage

1. Navigate to `data/sent_concepts.json` in your repository
2. See all previously sent topics
3. Ensures no duplicates

### Email Delivery

- Check spam/junk folder if email missing
- Gmail may group automated emails
- View workflow logs for confirmation

---

## 💡 Tips & Best Practices

1. **Test First:** Always run workflow manually before relying on schedule
2. **Monitor Quota:** Free Perplexity tier has limits - check usage
3. **Backup Secrets:** Store credentials securely outside GitHub
4. **Update Dependencies:** Run `pip list --outdated` periodically
5. **Star the Repo:** Helps others find the project!

---

## 🎓 What You've Learned

- ✅ GitHub Actions for automation
- ✅ Working with API secrets securely
- ✅ Email automation with Python
- ✅ AI API integration (Perplexity)
- ✅ Cron scheduling
- ✅ Git workflows and CI/CD basics

---

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Perplexity API Docs](https://docs.perplexity.ai/)
- [Cron Expression Generator](https://crontab.guru/)
- [Gmail SMTP Settings](https://support.google.com/mail/answer/7126229)

---

## ❓ Need Help?

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Review workflow logs in GitHub Actions
3. Open an issue on GitHub repository
4. Double-check all secrets are set correctly

---

## 🎉 Congratulations!

You now have a fully automated AI learning system that will:
- 📧 Send you 5 new AI concepts every day
- 🔄 Never repeat topics
- 💰 Cost you $0 (using free tiers)
- 🚀 Run automatically without your input

**Enjoy your daily AI insights!** 🤖✨
