# ⚡ Quick Start Guide (2 Minutes)

## 🎯 Goal
Get the multi-agent content creator running in 2 minutes!

---

## 📋 Prerequisites Check

- ✅ Python installed: You have Python 3.12.9
- ✅ UV installed: Already done
- ✅ Dependencies: Already installed (38 packages)
- ✅ Code: Ready to run (main.py)
- ⚠️ **TODO**: Add OpenAI API key to `.env`

---

## 🔑 Step 1: Add Your OpenAI API Key (1 minute)

### Open `.env` file:
```
c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic\.env
```

### Find this line:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Replace with your actual key:
```
OPENAI_API_KEY=sk-proj-... (your actual key)
```

**How to get a key:**
1. Go to https://platform.openai.com/account/api-keys
2. Create new secret key
3. Copy and paste here
4. Save the file

---

## 🚀 Step 2: Run the Application (1 minute)

### Open PowerShell and run:
```powershell
cd "c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic"
D:\miniforge\python.exe main.py
```

### Or use the shortcut:
```powershell
. ./commands.ps1
Start-ContentCreator
```

---

## 📝 Step 3: Enter Your Topic

When the application starts, you'll see:
```
📌 Enter the topic for content creation
   (e.g., 'The impact of AI on business automation'): 
```

**Type any topic you want researched**, for example:
```
Future of Renewable Energy
```

Then press **Enter**

---

## ⏳ Step 4: Wait for Results (2-3 minutes)

The system will run through 3 phases:

```
📚 RESEARCH PHASE...        (30-40 seconds)
✍️  WRITING PHASE...        (30-40 seconds)
✏️  EDITING PHASE...        (30-40 seconds)
```

You'll see progress messages like:
```
✅ Research completed - 1200 characters generated
✅ Draft completed - 2500 characters generated
✅ Editing completed - Article polished and refined
```

---

## 📄 Step 5: View Results

After completion, you'll see:

1. **Full article printed to console**
2. **Files created:**
   - `article_output.txt` - Your generated article
   - `memory_log.json` - Process history

### To view the article:
```powershell
# Using commands:
. ./commands.ps1
View-Output

# Or manually:
Get-Content article_output.txt
```

---

## 🎉 Done!

Your multi-agent content creator is working!

---

## 💡 Tips & Tricks

### **Faster Testing**
Edit `main.py` line 19 to use gpt-3.5-turbo instead of gpt-4:
```python
model="gpt-3.5-turbo",  # 10x faster, less capable
```

### **Check Installed Packages**
```powershell
D:\miniforge\python.exe -m uv pip list
```

### **Add a New Package**
```powershell
D:\miniforge\python.exe -m uv pip install <package-name>
```

### **Run with Different Topic**
Just run the command again and enter a new topic

### **Batch Processing**
Modify `main.py` to process multiple topics in a loop

---

## 🐛 If Something Goes Wrong

### **Error: "API key not set"**
```
✅ Solution: Edit .env and add your actual API key
```

### **Error: "Module not found"**
```
✅ Solution: 
D:\miniforge\python.exe -m uv pip install -r requirements.txt
```

### **Error: "ConnectionError"**
```
✅ Solution: Check your internet connection
```

### **Error: "Rate limit exceeded"**
```
✅ Solution: Wait a few moments and try again
```

---

## 📚 Next: Read Full Documentation

After your first successful run, check out:
- **[SETUP_COMPLETE.md](./SETUP_COMPLETE.md)** - Complete setup guide
- **[README.md](./README.md)** - Full documentation
- **[INDEX.md](./INDEX.md)** - Project index
- **[UV_SETUP.md](./UV_SETUP.md)** - Package manager details

---

## 🎯 What's Happening Behind the Scenes

```
1. YOU enter a topic
        ↓
2. RESEARCHER Agent 📚
   - Searches for information
   - Gathers facts and trends
   - Creates research brief
        ↓
3. WRITER Agent ✍️
   - Reads research data
   - Writes engaging article
   - Creates first draft
        ↓
4. EDITOR Agent ✏️
   - Reads draft
   - Fixes grammar
   - Improves clarity
   - Returns polished article
        ↓
5. YOU get professional article!
```

---

## ⚙️ System Requirements

✅ **What You Have:**
- Python 3.12.9 ✓
- UV package manager ✓
- All dependencies ✓
- Main application ✓

⚠️ **What You Need:**
- OpenAI API key (free with credits) ✓
- Internet connection ✓

💾 **Resources:**
- Disk space: ~500MB (for dependencies)
- RAM: ~200MB during execution
- Network: Required for API calls

---

## 🔒 Important Security Notes

- ⚠️ **Never share your API key**
- ⚠️ **Never commit `.env` to git**
- ⚠️ **Keep `.env` file private**
- ✅ **Add `.env` to `.gitignore`**

---

## 📊 Expected Output Example

```
=====================================
FINAL ARTICLE
=====================================

Future of Renewable Energy: Trends and Innovations

In recent years, renewable energy has emerged as a
critical component of global energy strategy...

[Full article content here...]

=====================================
PROCESS SUMMARY
=====================================
✅ Research phase: Completed (1 research(s))
✅ Writing phase: Completed (1 draft(s))
✅ Editing phase: Completed (1 iteration(s))
```

---

## 🎓 After Your First Run

1. **Celebrate!** 🎉 You've successfully run an agentic AI system
2. **Review the output** - Check the generated article
3. **Explore the code** - See how agents work in main.py
4. **Experiment** - Try different topics
5. **Customize** - Modify prompts and behavior
6. **Learn** - Read the full documentation

---

## 🚀 You're All Set!

**Ready to generate amazing content?**

Run this command now:
```bash
D:\miniforge\python.exe main.py
```

---

**Questions?** Check [INDEX.md](./INDEX.md) for documentation links.

**Version**: 1.0.0 | **Status**: ✅ Ready | **Date**: November 21, 2025
