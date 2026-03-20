# Offline E-Commerce Customer Support Chatbot - Setup Guide

##  Project Overview
This project implements a privacy-focused, offline customer support chatbot for an e-commerce store ('Chic Boutique') using local LLM inference with Ollama and Llama 3.2 (3B) model.

**Key Features**:
- 100% local (no API costs or data leaks)
- Evaluates **zero-shot vs one-shot prompting** on 20 realistic customer queries
- Generates `eval/results.md` for manual scoring (Relevance, Coherence, Helpfulness on 1-5 scale)
- See [README.md](README.md) for full details and [report.md](report.md) for analysis.

##  Prerequisites
- **OS**: Windows 11
- **Python**: 3.8+ ([download](https://www.python.org/downloads/))
- **RAM**: At least 8GB free (for model loading)
- **Hardware**: CPU/GPU compatible with Ollama (most modern PCs)

##  Step 1: Install and Setup Ollama
Ollama runs the local LLM.

1. Download from [ollama.com/download](https://ollama.com/download) (Windows installer).
2. Run the installer (adds `ollama` to PATH).
3. Open **PowerShell or Command Prompt as Administrator** and verify:
   ```
   ollama --version
   ```
4. Pull the model (downloads ~2GB, takes 5-10 min):
   ```
   ollama pull llama3.2:3b
   ```
5. Start Ollama service (runs in background):
   ```
   ollama serve
   ```
   - Keep this terminal open, or it auto-starts on Windows.
6. **Verify** (new terminal):
   ```
   ollama list
   ollama ps
   ```
   - Should show `llama3.2:3b` and service running on `http://localhost:11434`.

##  Step 2: Python Environment and Dependencies
Use virtual environment for isolation.

1. Open terminal in project dir (`c:/Users/USHODAYA/Desktop/GPP/Offline-chatbbot`).
2. Create virtual env:
   ```
   python -m venv venv
   ```
3. Activate:
   - **Command Prompt**: `venv\Scripts\activate.bat`
   - **PowerShell**: `venv\Scripts\Activate.ps1` (run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` if blocked).
   - Prompt shows `(venv)`.
4. Install dependencies (only `requests` needed):
   ```
   pip install requests
   ```

## ▶ Step 3: Run the Evaluation
1. Ensure Ollama running (Step 1).
2. Run script:
   ```
   python chatbot.py
   ```
3. **Expected Output**:
   - Console progress: `🔹 Processing Query 1... ✅ Zero-shot done ✅ One-shot done` (x20).
   - Generates `eval/results.md` with Markdown table:
     ```
     |Query #|Customer Query|Prompting Method|Response|Relevance|Coherence|Helpfulness|
     ```
   - Takes ~2-5 min depending on hardware.

##  Verification Checklist
- [ ] `ollama list` shows `llama3.2:3b`
- [ ] `ollama ps` shows service running
- [ ] `python chatbot.py` runs without import errors
- [ ] `eval/results.md` created with 40 rows (20 zero-shot + 20 one-shot)
- [ ] No errors like 'Error querying Ollama'

##  Troubleshooting
| Issue                           | Solution                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `ollama: command not found`     | Restart terminal, reinstall Ollama, check PATH.                                                                          |
| `Error: Could not get response` | Run `ollama serve`, check `http://localhost:11434` in browser (should show Ollama page). Kill via Task Manager if stuck. |
| Model not loading               | Free RAM, pull again `ollama pull llama3.2:3b`.                                                                          |
| Port 11434 busy                 | `netstat -ano \| findstr :11434`, kill process or change Ollama port.                                                    |
| Virtual env activation fails    | Use `.\venv\Scripts\Activate.ps1` in PowerShell.                                                                         |
| Python not found                | Add Python to PATH during install.                                                                                       |

**Logs**: Check Ollama logs in its terminal.

##  Next Steps
1. Open `eval/results.md` and score columns (1-5).
2. Read [report.md](report.md) for analysis.
3. Customize: Edit `prompts/*.txt` or add queries in `chatbot.py`.

##  Resources
- [Ollama Docs](https://ollama.com/docs)
- [Python Virtual Env](https://docs.python.org/3/library/venv.html)
- Project ready! No internet needed after setup.

