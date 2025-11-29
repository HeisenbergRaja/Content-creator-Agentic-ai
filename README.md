# Multi-Agent Content Creator System

A sophisticated Python-based content creation system using specialized AI agents (Researcher, Writer, Editor) orchestrated through LangChain. Features automated fact-checking, multi-format export, and social media content generation using the free Groq API.

## 🎯 System Overview

**What It Does:**
- Researches any topic automatically
- Writes professional articles
- Edits for quality and clarity
- Verifies facts and claims
- Generates social media content
- Exports to 4+ formats (PDF, Word, HTML, Markdown)

**Core Technologies:**
- **LangChain 0.1.20** - Multi-agent orchestration
- **Groq API** - Free, unlimited inference (no billing)
- **Python 3.8+** - Clean, maintainable code

## 🏗️ System Architecture

### Three Specialized Agents:

1. **📚 Researcher Agent**
   - Gathers comprehensive information
   - Provides fact-based research briefs
   - Uses specialized prompt templates
   - Outputs: Detailed research content

2. **✍️ Writer Agent**
   - Creates engaging article drafts
   - Structures content logically
   - Maintains readability
   - Outputs: Well-organized articles

3. **✏️ Editor Agent**
   - Polishes for grammar and clarity
   - Improves transitions and flow
   - Checks consistency and tone
   - Outputs: Publication-ready content

### Three Enhancement Tools:

4. **🔍 Fact-Checking Agent**
   - Verifies claims and statistics
   - Assigns confidence scores (0-100%)
   - Identifies sources needed
   - Suggests improvements

5. **📄 Multi-Format Exporter**
   - PDF (print-ready)
   - Word DOCX (editable)
   - HTML (web-ready)
   - Markdown (developer-friendly)

6. **📱 Social Media Generator**
   - Twitter threads (3 tweets)
   - LinkedIn posts
   - Instagram captions
   - Email subject/preview
   - Optimized hashtags

## 📋 Features

- ✅ **Sequential Multi-Agent Workflow** (Research → Write → Edit)
- ✅ **Fact-Checking & Verification** with confidence scores
- ✅ **4-Format Export** (PDF, Word, HTML, Markdown)
- ✅ **Social Media Content** (5 platforms)
- ✅ **Persistent Memory** system for context retention
- ✅ **Multi-Iteration Refinement** loops
- ✅ **JSON Activity Logging** with complete audit trail
- ✅ **User Feedback Integration** for article improvements
- ✅ **Completely Free** (Groq API)
- ✅ **No Dependencies on Paid Services**

## 📦 Dependencies

All packages listed in `requirements.txt`:

| Package | Purpose |
|---------|---------|
| `langchain` | Multi-agent orchestration framework |
| `langchain-groq` | Groq API integration |
| `groq` | Free LLM inference |
| `python-dotenv` | Environment variable management |
| `requests` | HTTP library |
| `beautifulsoup4` | Web scraping |
| `nltk` | NLP toolkit |
| `pydantic` | Data validation |
| `reportlab` | PDF generation |
| `python-docx` | Word document creation |
| `jinja2` | Template rendering |

**Total Dependencies:** 38 packages (lightweight & fast)

**NOT Used:** CrewAI (replaced with custom lightweight agents), OpenAI (replaced with free Groq)

## 🚀 Installation

### Step 1: Navigate to Project
```bash
cd c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic
```

### Step 2: Install Dependencies (Using UV - Recommended)
```bash
python -m uv pip install -r requirements.txt
```

Or with pip:
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
```bash
# Copy template
copy .env.example .env

# Edit .env and add your Groq API key
# Get free key at: https://console.groq.com/keys
GROQ_API_KEY=your_free_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### Step 4: Run the System
```bash
python main.py
```

## 💻 Usage

### Basic Execution
```bash
python main.py
```

### Workflow
1. **Enter topic** when prompted
2. **Research Phase** (~1 minute)
   - Gathers information
   - Generates research brief
3. **Writing Phase** (~1 minute)
   - Creates article draft
   - Structures content
4. **Editing Phase** (~1 minute)
   - Polishes content
   - Verifies quality
5. **Fact-Checking Phase** (~1 minute)
   - Verifies claims
   - Assigns confidence scores
6. **Export Phase** (~30 seconds)
   - Generates 4 file formats
   - Creates social media content

**Total Time:** 3-5 minutes for complete pipeline

### Output Files Generated

| File | Format | Purpose |
|------|--------|---------|
| `article_output.txt` | Plain text | Main article |
| `memory_log.json` | JSON | Complete history |
| `comprehensive_output.txt` | Text | Fact-check report |
| `social_content_*.json` | JSON | Social media data |
| `article_*.md` | Markdown | For blogs |
| `article_*.html` | HTML | Web-ready |
| `article_*.docx` | Word | Editable |
| `article_*.pdf` | PDF | Print-ready |

## 📂 Project Structure

```
content-creator-agentic-ai/
├── main.py                    # Main application (369 lines)
├── content_tools.py           # Enhancement tools (486 lines)
├── requirements.txt           # Dependencies
├── .env.example              # Environment template
├── pyproject.toml            # Python package config
├── .gitignore                # Git exclusions
├── README.md                 # This file
├── QUICKSTART.md             # 2-minute setup guide
├── SETUP_COMPLETE.md         # Detailed setup
├── INDEX.md                  # Project index
├── UV_SETUP.md              # UV package manager guide
└── exports/                  # Generated files
    ├── article_*.md
    ├── article_*.html
    ├── article_*.docx
    └── article_*.pdf
```

## 🔧 Code Structure

### Main Classes in `main.py`

**ContentCreatorMemory**
```python
- add_research(topic, content)      # Store research
- add_draft(draft, iteration)        # Store drafts
- add_edit_feedback(feedback, iter)  # Store edits
- save_to_file(filename)             # Export to JSON
```

**ResearcherAgent**
```python
- research(topic)    # Execute research task
```

**WriterAgent**
```python
- write(research)    # Execute writing task
```

**EditorAgent**
```python
- edit(draft)        # Execute editing task
```

**MultiAgentContentCreator**
```python
- create_content(topic)     # Main pipeline
- execute_iteration(topic)  # Single iteration
- export_results(filename)  # Save outputs
- display_results()         # Display in console
```

### Enhancement Tools in `content_tools.py`

**FactCheckingAgent**
```python
- verify_article(article)           # Verify claims
- generate_fact_check_report(data)  # Create report
```

**MultiFormatExporter**
```python
- export_to_markdown(article)   # Export as .md
- export_to_html(article)       # Export as .html
- export_to_docx(article)       # Export as .docx
- export_to_pdf(article)        # Export as .pdf
```

**SocialMediaGenerator**
```python
- generate_content(article)         # Generate social media
- generate_social_report(data)      # Create report
```

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Groq API Configuration
GROQ_API_KEY=your_free_groq_key_here

# Model Selection
GROQ_MODEL=llama-3.3-70b-versatile    # Latest, best
# GROQ_MODEL=llama-3.1-70b-versatile  # Alternative
# GROQ_MODEL=llama-3.1-8b-instant     # Fastest

# LLM Settings
GROQ_TEMPERATURE=0.7        # 0-1: 0=consistent, 1=creative
GROQ_MAX_TOKENS=2000        # Max output length

# Optional: LangChain
LANGCHAIN_TRACING_V2=false
LANGCHAIN_PROJECT=multi_agent_content_creator
```

### Adjust Max Iterations

In `main.py`:
```python
creator = MultiAgentContentCreator(max_iterations=3)
# Change 3 to 1 for faster runs
# Change 3 to 5 for more refinements
```

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Speed** | 3-5 minutes per article |
| **Quality** | Professional grade |
| **Cost** | Free (Groq API) |
| **Memory** | ~50MB RAM |
| **Files Generated** | 8+ per run |
| **Supported Formats** | 4 (+ JSON data) |
| **Social Platforms** | 5 (+ email) |

## 🔑 Why Groq Over OpenAI?

| Feature | Groq | OpenAI |
|---------|------|--------|
| Cost | FREE | Paid |
| Speed | Ultra-fast | Slower |
| Quota | Unlimited | Limited |
| Billing | None | $0.01-0.10/1K tokens |
| Reliability | Excellent | Good |
| API Key | Free account | Credit card |

## 🚨 Troubleshooting

### Error: "GROQ_API_KEY not found"
```bash
# Check .env file exists
# Ensure key is added: GROQ_API_KEY=your_key
# Restart the program
```

### Error: "Model not found"
```bash
# Verify model name in .env
# Available: llama-3.3-70b-versatile, llama-3.1-70b-versatile
# Update if decommissioned
```

### Error: "Module not found"
```bash
# Reinstall dependencies
python -m uv pip install -r requirements.txt --force-reinstall
```

### Slow Response Times
- Normal for first run (model loading)
- Subsequent runs are faster
- Check internet connection
- Verify API key is valid

## 📈 Example Output

**Input:** "cryptocurrency"

**Output Article:** 6,000+ words covering:
- Key facts & statistics
- Current trends & developments
- Historical context
- Expert perspectives
- FAQ section
- Conclusion

**Fact-Check Report:**
- 80%+ accuracy score
- 15+ verified claims
- 3 claims needing sources
- 5 improvement suggestions

**Social Media Package:**
- 3 Twitter tweets
- 1 LinkedIn post
- 1 Instagram caption
- 1 Email subject/preview
- 4 hashtag recommendations
- 1 key quote extraction

**Export Files:**
- Professional PDF (8KB)
- Editable Word document (39KB)
- Web-ready HTML (8KB)
- Markdown version (7KB)

## 🎓 Learning Resources

### LangChain Documentation
- https://python.langchain.com/
- RunnableSequence patterns
- Prompt templates

### Groq API
- https://console.groq.com/
- Free API key generation
- Available models

### Python Best Practices
- Type hints
- Error handling
- Code organization

## 🤝 Contributing

Improvements welcome! Consider:
- Additional export formats
- More specialized agents
- Database persistence
- Web UI
- API endpoints

## 📄 License

Open source - Free for educational and commercial use

## 🎉 Key Achievements

✅ Multi-agent system without CrewAI  
✅ Free inference (Groq API)  
✅ Production-ready code  
✅ 3 enhancement tools built-in  
✅ 4+ export formats  
✅ 5+ social platforms  
✅ Zero paid dependencies  
✅ Full audit trail & logging  

---

**Version:** 2.0.0  
**Last Updated:** November 2025  
**Python:** 3.8+  
**Status:** Production Ready ✅
