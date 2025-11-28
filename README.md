# Multi-Agent Content Creator System

A sophisticated Python-based content creation system using specialized AI agents (Researcher, Writer, Editor) orchestrated through LangChain and CrewAI frameworks.

## System Architecture

### Agents:
1. **Researcher Agent**: Gathers comprehensive information and provides fact-based research briefs
2. **Writer Agent**: Creates engaging, well-structured article drafts from research data
3. **Editor Agent**: Polishes articles for clarity, grammar, style, and coherence

### Key Features:
- ✅ Sequential multi-agent workflow (Research → Write → Edit)
- ✅ Persistent memory system for context retention
- ✅ Multi-iteration refinement loops
- ✅ Comprehensive output export (text files + JSON logs)
- ✅ Activity logging and process tracking
- ✅ User feedback integration for article refinement

## Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
All required packages are listed in `requirements.txt`:
- **langchain**: Framework for building agentic AI systems
- **langchain-openai**: OpenAI integration with LangChain
- **crewai**: Multi-agent orchestration framework
- **openai**: OpenAI API client
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for API calls
- **beautifulsoup4**: HTML parsing for web scraping
- **nltk**: Natural language toolkit
- **spacy**: Advanced NLP processing

## Installation

### Step 1: Clone or Navigate to Project
```bash
cd c:\Users\Heisenberg Raja\OneDrive\Desktop\agentic
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

2. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### Step 5: Download NLP Models (Optional)
For enhanced text processing with spaCy:
```bash
python -m spacy download en_core_web_sm
```

## Usage

### Basic Execution
```bash
python main.py
```

### Workflow
1. Enter the topic you want content created for
2. The system will execute in sequence:
   - **Research Phase**: Gathers and summarizes information
   - **Writing Phase**: Creates an engaging article draft
   - **Editing Phase**: Polishes the final output
3. Results are displayed in console and exported to files

### Output Files Generated
- `article_output.txt`: Final polished article
- `memory_log.json`: Complete process history with all phases

## Code Structure

### Main Classes

#### `ContentCreatorMemory`
Persistent memory system that stores:
- Research history with topics and content
- Draft versions across iterations
- Editing feedback and improvements
- Metadata (timestamps, iteration count)

**Key Methods**:
- `add_research()`: Store research data
- `add_draft()`: Store draft versions
- `add_edit_feedback()`: Store editing notes
- `save_to_file()`: Export memory to JSON

#### `MultiAgentContentCreator`
Main orchestrator managing the entire workflow

**Key Methods**:
- `create_research_task()`: Define researcher task
- `create_writing_task()`: Define writer task
- `create_editing_task()`: Define editor task
- `execute_iteration()`: Execute one full cycle
- `create_content()`: Main content generation pipeline
- `export_results()`: Save outputs to files

### Agent Creation Functions
- `create_researcher_agent()`: Initialize researcher with LLM
- `create_writer_agent()`: Initialize writer with LLM
- `create_editor_agent()`: Initialize editor with LLM

## Advanced Features

### Multi-Iteration Refinement
The system supports multiple refinement cycles where users can:
- Review initial output
- Provide specific feedback
- Execute additional iterations for improvement

### Memory Persistence
- All research, drafts, and feedback stored in memory
- Context automatically included in subsequent iterations
- Complete audit trail saved to JSON log

### Logging and Transparency
- Real-time console output of each phase
- Detailed activity logs
- Progress tracking across iterations

## Example Usage

```python
# Create instance with 3 max iterations
creator = MultiAgentContentCreator(max_iterations=3)

# Generate content with topic
final_article = creator.create_content(
    topic="The impact of AI on business automation",
    enable_refinement=False  # Set True for interactive refinement
)

# Export results
creator.export_results(filename="my_article.txt")
```

## Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution**: Ensure `.env` file exists and contains valid API key

### Issue: ImportError for crewai or langchain
**Solution**: Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Slow API responses
**Solution**: This is normal for GPT-4. For faster testing, modify model selection in code to GPT-3.5-turbo

## Configuration Options

### Temperature Settings
Modify LLM temperature in `main.py`:
```python
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7  # 0-1: lower = more consistent, higher = more creative
)
```

### Max Iterations
Control refinement cycles:
```python
creator = MultiAgentContentCreator(max_iterations=5)  # Increase for more refinements
```

## Performance Notes

- **First run**: ~30-60 seconds (depends on topic complexity and API latency)
- **Each iteration**: ~20-30 seconds
- **Memory usage**: Minimal (all in RAM)
- **API costs**: Varies by model and input/output tokens

## Future Enhancements

1. **Web Search Integration**: Real-time information gathering
2. **Multi-format Export**: PDF, Markdown, HTML support
3. **Fact-Checking**: Automated verification layer
4. **Custom Prompts**: User-defined agent behaviors
5. **Database Storage**: Replace JSON with persistent DB
6. **Async Processing**: Parallel agent execution
7. **Web UI**: Interactive dashboard interface
8. **Feedback Loops**: Automated quality scoring

## License

This project is open-source and available for educational and commercial use.

## Support

For issues, questions, or improvements, refer to the documentation above or check framework docs:
- LangChain: https://python.langchain.com/
- CrewAI: https://github.com/joaomdmoura/crewAI
- OpenAI: https://platform.openai.com/docs

---
**Created**: November 2025
**Version**: 1.0.0
