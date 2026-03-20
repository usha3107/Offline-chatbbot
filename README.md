# Offline E-Commerce Customer Support Chatbot
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama3.2:3b-green.svg)](https://ollama.com/)

##  Overview
This project demonstrates an **offline customer support chatbot** for e-commerce using **Ollama** and **Llama 3.2 (3B)** model. It evaluates **zero-shot** vs **one-shot prompting** on 20 realistic customer queries for 'Chic Boutique' online store.

**Key Goals:**
- Privacy-focused (100% local inference)
- Zero API costs
- Compare prompting techniques
- Generate evaluation table for manual scoring (Relevance, Coherence, Helpfulness)

Results saved to `eval/results.md`.

##  Features
- Local LLM inference via Ollama
- Zero-shot and one-shot prompt templates
- 20 e-commerce customer support queries
- Automatic evaluation table generation
- Manual scoring framework (1-5 scale)

##  Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed & running

### Installation
1. **Install Ollama**: [Download Ollama](https://ollama.com/download)
2. **Pull model**:
   ```bash
   ollama pull llama3.2:3b
   ```
3. **Start Ollama** (keep running)
4. **Install Python deps**:
   ```bash
   pip install requests datasets
   ```

### Usage
Run the evaluation:
```bash
python chatbot.py
```

**Output**: 
- Processing progress printed to console
- Results saved to `eval/results.md` (Markdown table with queries, responses, scoring columns)

### View Results
Open `eval/results.md` and manually score responses (1-5):
- **Relevance**: Does it answer the query?
- **Coherence**: Is the response clear/logical?
- **Helpfulness**: Would this help a real customer?

##  Project Structure
```
Offline-chatbbot/
├── chatbot.py              # Main evaluation script
├── README.md              # 📄 This file
├── setup.md              # Detailed setup instructions
├── report.md             # Analysis & conclusions
├── eval/
│   └── results.md        # Generated results table
└── prompts/
    ├── zero_shot_template.txt   # Zero-shot prompt
    └── one_shot_template.txt    # One-shot prompt (w/ example)
```

##  Example Output
| Query # | Customer Query                     | Prompting Method | Response | Relevance | Coherence | Helpfulness |
| ------- | ---------------------------------- | ---------------- | -------- | --------- | --------- | ----------- |
| 1       | My discount code is not working... | Zero-Shot        | ...      | 5         | 4         | 5           |

**Key Findings** (from `report.md`):
- One-shot > Zero-shot for structure/consistency
- Good for basic queries
- Limitations: No real-time order data, potential hallucinations

##  Prompt Templates
- **Zero-shot**: Basic role + query
- **One-shot**: Includes example response for style guidance

##  Future Improvements
- Multi-turn conversations
- Database integration for order lookup
- Larger models (Llama 8B+)
- Automated evaluation metrics
- RAG for product catalog

##  Full Report
See [report.md](report.md) for detailed methodology, results analysis, & conclusions.



##  License
MIT License - see [LICENSE](LICENSE) (create if needed) for details.

##  Acknowledgments
- [Ollama](https://ollama.com/) for local inference
- [Llama 3.2](https://ollama.com/library/llama3.2) for the model
- E-commerce support query inspiration from common helpdesk scenarios

---


