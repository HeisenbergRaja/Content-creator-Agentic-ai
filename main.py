"""
Multi-Agent Content Creator System
Specialized agents for research, writing, and editing content
Enhanced with: Fact-Checking, Multi-Format Export, Social Media Generation
"""

import os
from typing import Dict
from datetime import datetime
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import json
from content_tools import generate_comprehensive_output

# Load environment variables
load_dotenv()

# Configure LLM - Using Groq (Free API with no limitations!)
model = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
temperature = float(os.getenv("GROQ_TEMPERATURE", "0.7"))
max_tokens = int(os.getenv("GROQ_MAX_TOKENS", "2000"))

llm = ChatGroq(
    model=model,
    temperature=temperature,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=max_tokens
)


class ContentCreatorMemory:
    """Persistent memory system for agents"""
    
    def __init__(self):
        self.research_history = []
        self.draft_history = []
        self.edit_history = []
        self.metadata = {
            "created_at": datetime.now().isoformat(),
            "total_iterations": 0
        }
    
    def add_research(self, topic: str, content: str):
        """Store research data"""
        self.research_history.append({
            "topic": topic,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_draft(self, draft: str, iteration: int):
        """Store draft versions"""
        self.draft_history.append({
            "content": draft,
            "iteration": iteration,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_edit_feedback(self, feedback: str, iteration: int):
        """Store editing feedback"""
        self.edit_history.append({
            "feedback": feedback,
            "iteration": iteration,
            "timestamp": datetime.now().isoformat()
        })
    
    def save_to_file(self, filename: str = "memory_log.json"):
        """Save memory to file"""
        data = {
            "metadata": self.metadata,
            "research_history": self.research_history,
            "draft_history": self.draft_history,
            "edit_history": self.edit_history
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Memory saved to {filename}")


class ResearcherAgent:
    """Agent specialized in research and information gathering"""
    
    def __init__(self, memory: ContentCreatorMemory):
        self.memory = memory
        self.role = "Content Researcher"
        self.research_template = PromptTemplate(
            input_variables=["topic"],
            template="""You are an expert research agent. Your task is to provide a comprehensive, 
well-organized research brief on the following topic:

Topic: {topic}

Please include:
1. Key facts and statistics (cite sources where possible)
2. Current trends and developments
3. Historical context and background
4. Expert perspectives if relevant
5. Potential questions readers might have

Format the research as a structured brief with clear sections.
Make it informative, accurate, and accessible to a general audience."""
        )
    
    def research(self, topic: str) -> str:
        """Execute research task"""
        print(f"\n📚 {self.role} is researching: {topic}")
        
        chain = self.research_template | llm
        research_content = chain.invoke({"topic": topic}).content
        
        self.memory.add_research(topic, research_content)
        print(f"✅ Research completed - {len(research_content)} characters generated")
        
        return research_content


class WriterAgent:
    """Agent specialized in content writing"""
    
    def __init__(self, memory: ContentCreatorMemory):
        self.memory = memory
        self.role = "Content Writer"
        self.writing_template = PromptTemplate(
            input_variables=["research"],
            template="""You are a professional content writer. Your task is to create an engaging, 
well-structured article based on the following research data:

Research Data:
{research}

Requirements:
1. Write an engaging introduction that hooks the reader
2. Organize content into clear, logical sections
3. Use compelling language while maintaining clarity
4. Include smooth transitions between sections
5. Provide a strong conclusion that summarizes key points
6. Maintain consistent tone and voice throughout
7. Make it accessible to a general audience

Create a complete article draft that is ready for editing."""
        )
    
    def write(self, research_content: str) -> str:
        """Execute writing task"""
        print(f"\n✍️  {self.role} is drafting article...")
        
        chain = self.writing_template | llm
        draft_content = chain.invoke({"research": research_content}).content
        
        iteration = len(self.memory.draft_history) + 1
        self.memory.add_draft(draft_content, iteration)
        print(f"✅ Draft completed - {len(draft_content)} characters generated")
        
        return draft_content


class EditorAgent:
    """Agent specialized in content editing and refinement"""
    
    def __init__(self, memory: ContentCreatorMemory):
        self.memory = memory
        self.role = "Content Editor"
        self.editing_template = PromptTemplate(
            input_variables=["draft", "iteration"],
            template="""You are a meticulous editor and proofreader. Your task is to review and 
improve the following article draft (iteration {iteration}):

Article Draft:
{draft}

Please provide:
1. A polished, corrected version of the article
2. Corrections for grammar, spelling, and punctuation
3. Improvements to clarity and readability
4. Enhanced transitions and flow
5. Consistency check for tone and style
6. Any suggestions for strengthening the content

Return the final polished article followed by a brief summary of improvements made."""
        )
    
    def edit(self, draft_content: str) -> str:
        """Execute editing task"""
        print(f"\n✏️  {self.role} is reviewing and polishing...")
        
        iteration = len(self.memory.edit_history) + 1
        chain = self.editing_template | llm
        final_content = chain.invoke({"draft": draft_content, "iteration": iteration}).content
        
        self.memory.add_edit_feedback(final_content, iteration)
        print(f"✅ Editing completed - Article polished and refined")
        
        return final_content


class MultiAgentContentCreator:
    """Orchestrates multi-agent content creation workflow"""
    
    def __init__(self, max_iterations: int = 3):
        self.memory = ContentCreatorMemory()
        self.max_iterations = max_iterations
        self.current_iteration = 0
        
        # Initialize agents
        self.researcher = ResearcherAgent(self.memory)
        self.writer = WriterAgent(self.memory)
        self.editor = EditorAgent(self.memory)
        
        # Store results
        self.results = {
            "research": "",
            "drafts": [],
            "final_article": "",
            "iterations": []
        }
    
    def execute_iteration(self, topic: str) -> Dict:
        """Execute one complete iteration of the content creation workflow"""
        self.current_iteration += 1
        print(f"\n{'='*70}")
        print(f"🔄 ITERATION {self.current_iteration}")
        print(f"{'='*70}")
        
        iteration_result = {
            "iteration": self.current_iteration,
            "research": "",
            "draft": "",
            "final_article": ""
        }
        
        # Step 1: Research
        research_content = self.researcher.research(topic)
        iteration_result["research"] = research_content
        self.results["research"] = research_content
        
        # Step 2: Writing
        draft_content = self.writer.write(research_content)
        iteration_result["draft"] = draft_content
        self.results["drafts"].append(draft_content)
        
        # Step 3: Editing
        final_content = self.editor.edit(draft_content)
        iteration_result["final_article"] = final_content
        self.results["final_article"] = final_content
        self.results["iterations"].append(iteration_result)
        
        print(f"\n✅ Iteration {self.current_iteration} completed successfully!")
        return iteration_result
    
    def create_content(self, topic: str, enable_refinement: bool = False) -> str:
        """Main method to orchestrate the entire content creation process"""
        print("\n" + "="*70)
        print("🚀 MULTI-AGENT CONTENT CREATOR STARTED")
        print("="*70)
        print(f"Topic: {topic}")
        print(f"Max iterations: {self.max_iterations}\n")
        
        # Execute initial iteration
        self.execute_iteration(topic)
        
        # Execute refinement iterations if enabled
        if enable_refinement and self.max_iterations > 1:
            for i in range(self.max_iterations - 1):
                user_input = input("\n🔄 Would you like to refine the article further? (yes/no): ").strip().lower()
                if user_input != 'yes':
                    break
                
                feedback = input("📝 Enter specific feedback for refinement: ").strip()
                if feedback:
                    print(f"\n📌 Applying feedback: {feedback}")
                    self.execute_iteration(f"{topic} - Refined based on: {feedback}")
                else:
                    break
        
        self.memory.metadata["total_iterations"] = self.current_iteration
        return self.results["final_article"]
    
    def export_results(self, filename: str = "article_output.txt"):
        """Export results to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("MULTI-AGENT CONTENT CREATOR - FINAL OUTPUT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Total Iterations: {self.current_iteration}\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            f.write("="*70 + "\n")
            f.write("FINAL ARTICLE\n")
            f.write("="*70 + "\n\n")
            f.write(self.results["final_article"])
            f.write("\n\n" + "="*70 + "\n")
            f.write("PROCESS SUMMARY\n")
            f.write("="*70 + "\n")
            f.write(f"✅ Research phase: Completed ({len(self.memory.research_history)} research(es))\n")
            f.write(f"✅ Writing phase: Completed ({len(self.results['drafts'])} draft(s))\n")
            f.write(f"✅ Editing phase: Completed ({self.current_iteration} iteration(s))\n\n")
            f.write("="*70 + "\n")
            f.write("AGENT PERFORMANCE NOTES\n")
            f.write("="*70 + "\n")
            f.write(f"Research Agent (📚): Gathered comprehensive information\n")
            f.write(f"Writer Agent (✍️ ): Created engaging article structure\n")
            f.write(f"Editor Agent (✏️ ): Polished content for quality and clarity\n")
        
        print(f"\n📄 Results exported to {filename}")
        self.memory.save_to_file("memory_log.json")
        
        # Generate comprehensive output with new tools
        print("\n" + "="*70)
        print("📦 GENERATING ENHANCED CONTENT PACKAGE")
        print("="*70)
        
        # Create exports directory
        os.makedirs("exports", exist_ok=True)
        
        # Generate all additional content
        comprehensive_results = generate_comprehensive_output(
            self.results["final_article"],
            "article"
        )
    
    def display_results(self):
        """Display results in console"""
        print("\n" + "="*70)
        print("📰 FINAL ARTICLE")
        print("="*70)
        print(self.results["final_article"])
        print("\n" + "="*70)


def main():
    """Main execution function"""
    print("\n" + "="*70)
    print("🤖 MULTI-AGENT CONTENT CREATOR SYSTEM")
    print("="*70)
    print("\nThis system uses specialized AI agents to create high-quality content:")
    print("  📚 Researcher Agent - Gathers information and insights")
    print("  ✍️  Writer Agent - Creates engaging article drafts")
    print("  ✏️  Editor Agent - Polishes for quality and clarity\n")
    
    # Get topic from user
    topic = input("📌 Enter the topic for content creation\n   (e.g., 'The impact of AI on business automation'): ").strip()
    
    if not topic:
        topic = "The impact of agentic AI on modern automation"
        print(f"   Using default topic: {topic}\n")
    
    # Check for API key
    if not os.getenv("GROQ_API_KEY"):
        print("\n❌ ERROR: GROQ_API_KEY environment variable not set!")
        print("   Please create a .env file with your Groq API key:")
        print("   GROQ_API_KEY=your_actual_key_here")
        print("\n   Get a free API key at: https://console.groq.com/keys")
        return
    
    print("\n✅ Groq API key found. Initializing agents...\n")
    
    # Create the content creator instance
    creator = MultiAgentContentCreator(max_iterations=3)
    
    try:
        # Generate content
        final_article = creator.create_content(topic, enable_refinement=False)
        
        # Display results
        creator.display_results()
        
        # Export results
        creator.export_results()
        
        print("\n✨ Content creation completed successfully!")
        print("📁 Output files created:")
        print("   - article_output.txt (final article)")
        print("   - memory_log.json (process history)")
        print("   - comprehensive_output.txt (fact-check & social media)")
        print("   - social_content_*.json (social media data)")
        print("\n📂 Export formats in /exports/:")
        print("   - article_*.md (Markdown)")
        print("   - article_*.html (Web HTML)")
        print("   - article_*.docx (Word Document)")
        print("   - article_*.pdf (PDF)")
        
    except Exception as e:
        print(f"\n❌ Error during content creation: {str(e)}")
        print("   Please ensure your Groq API key is valid and you have sufficient credits.")
        return


if __name__ == "__main__":
    main()
