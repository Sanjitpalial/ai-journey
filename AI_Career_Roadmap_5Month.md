# From Zero to AI-Job-Ready — 5 Month Roadmap
**Profile:** Complete beginner → AI/ML role | 3–4 hrs/day (ramping to 6+ hrs) | ~5 months

---

## How to use this doc (read this first)

You said your real problem isn't understanding things — it's **forgetting them**. So this roadmap isn't just "watch these videos." It's built around 3 anti-forgetting rules. Break these and the 5 months won't stick.

1. **Never just watch. Always build.** After every topic, close YouTube and write the code from memory, even badly. Watching = recognition. Coding from scratch = recall. Recall is what survives in your brain.
2. **Sunday Recall Ritual.** Every Sunday, before new content, spend 30 min reviewing last week's notes/code with no video playing. If you can't explain a concept out loud in plain language, you didn't learn it — you watched it.
3. **One repo, daily commits.** One GitHub repo called `ai-journey`. Every single day you touch it — even just notes. This becomes your second brain *and* your placement portfolio at the same time.

Keep an **Anki deck** (free app) for formulas, definitions, and "why does X exist" questions. 10 min/day reviewing flashcards beats 2 hours of re-watching a video you forgot.

---

## Tonight's checklist (do this before you sleep)

- [ ] Install Python (3.11+) + VS Code + Jupyter extension
- [ ] Create GitHub account → create repo `ai-journey` → make your first commit (even just a README saying "Day 1")
- [ ] Install Anki (anki.web app or desktop)
- [ ] Open CampusX's YouTube channel, subscribe, and watch **Video 1 of "100 Days of Machine Learning"** intro video just to see the full roadmap they've laid out (you won't start ML yet — just orient yourself)
- [ ] Start the **Python** playlist below — Day 1, Lecture 1. Just begin.

---

## The Order (Big Picture)

```
Python  →  Math for ML  →  Data Analysis (Numpy/Pandas/SQL)  →  Classical ML
   →  Deep Learning  →  NLP  →  LLMs / GenAI  →  Agentic AI  →  Portfolio + Interviews
```

Running in parallel the *entire time*: **DSA** (placements still test this) and **Math** (drip-fed, not a wall).

---

## Phase 0 — Python Foundations (Weeks 1–2)

**Goal:** Comfortable writing scripts, functions, OOP basics, reading error messages without panic.

**Primary:**
- CampusX — *Python* playlist (full beginner-to-intermediate, Hinglish)
- Backup/alternate explanations: CodeWithHarry "Python Tutorial for Beginners" or Telusko Python playlist (use these if a CampusX explanation doesn't click — different teacher, same topic, helps retention)

**Cover:** variables, data types, loops, functions, OOP (classes/objects/inheritance), file handling, exception handling, list/dict comprehensions, basic modules (`os`, `datetime`), virtual environments, pip.

**Project (mandatory before moving on):** Build a small CLI tool — e.g., an expense tracker or a quiz game that reads/writes to a file. Push to `ai-journey`.

---

## Phase 1 — Math for ML (Weeks 2–5, runs alongside Phase 0/2)

Don't binge math for a month straight — you'll forget it before you ever use it. Drip it in alongside Python/Pandas so you immediately see *why* it matters.

**Primary:**
- CampusX — *Maths for ML* playlist (built specifically for this exact use case)

**Supplement for intuition (these are gold — don't skip):**
- 3Blue1Brown — *"Essence of Linear Algebra"* series (visual, builds real intuition for vectors/matrices — this is what makes neural nets make sense later)
- 3Blue1Brown — *"Essence of Calculus"* series (you need derivatives/gradients for backprop, nothing more)
- StatQuest with Josh Starmer — Probability & Statistics videos (best plain-English stats explanations on YouTube, also genuinely funny which helps memory)

**Cover:**
- Linear Algebra: vectors, matrices, dot product, matrix multiplication, eigenvalues/eigenvectors (just enough to understand PCA later)
- Calculus: derivatives, partial derivatives, chain rule, gradients (this directly becomes "gradient descent" and "backpropagation")
- Probability & Statistics: mean/median/variance/std dev, distributions (normal, binomial), conditional probability, Bayes' theorem, hypothesis testing, p-values, correlation

**Anti-forgetting tip:** For every math concept, immediately code it in NumPy by hand (e.g., write your own `mean()`, `gradient descent on y=x²` from scratch). Math you've coded sticks. Math you've only watched evaporates in 2 weeks.

---

## Phase 2 — Data Analysis: NumPy, Pandas, Matplotlib, SQL (Weeks 3–5)

**Primary:**
- CampusX — *Data Analysis using Python* playlist (NumPy + Pandas + Matplotlib/Seaborn)
- CampusX — *SQL* playlist

**Cover:** array operations & broadcasting (NumPy), dataframes, filtering, groupby, merging, pivot tables, handling missing data (Pandas), plotting distributions/relationships (Matplotlib/Seaborn), SQL joins, group by, subqueries, window functions.

**Project:** Pick a Kaggle dataset (e.g., Titanic or any dataset you find genuinely interesting) and do a full exploratory data analysis (EDA) notebook. Push it.

---

## Phase 3 — Classical Machine Learning (Weeks 5–9)

This is the core of "ML Engineer" interviews. Go slow here — this is the highest-leverage phase.

**Primary:**
- CampusX — *100 Days of Machine Learning* playlist (this is THE flagship CampusX series — MLDLC, feature engineering, every major algorithm, end-to-end projects)

**Supplement:**
- StatQuest — algorithm-specific videos (Linear/Logistic Regression, Decision Trees, Random Forest, SVM, Naive Bayes, PCA, Clustering) — watch StatQuest's version right after CampusX's version of the same algorithm. Two explanations of the same idea from two teachers = much better retention than one long explanation.
- Krish Naik or codebasics — ML playlists as a third angle if a concept still isn't sticking

**Cover:**
- ML lifecycle, train/test split, cross-validation, bias-variance tradeoff
- Feature engineering: scaling, encoding, transformations, binning
- Algorithms: Linear & Logistic Regression, Decision Trees, Random Forest, Gradient Boosting (XGBoost/LightGBM), SVM, KNN, Naive Bayes
- Unsupervised: K-Means, Hierarchical Clustering, PCA
- Model evaluation: confusion matrix, precision/recall/F1, ROC-AUC, R², RMSE
- Hyperparameter tuning: GridSearch, RandomSearch

**Project (mandatory):** One full end-to-end ML project — data → EDA → feature engineering → model → evaluation → a simple deployed app (Streamlit). This is portfolio piece #1.

---

## Side-track starts here — DSA (Weeks 5 onward, 30–45 min/day)

Placements still test data structures & algorithms even for AI roles. Don't let this pile up till the end.

- CampusX — *DSA for AI* playlist (tailored specifically for AI-role interviews, not generic CS interview grind)
- Practice on LeetCode/GeeksforGeeks alongside — arrays, strings, hashmaps, recursion, basic trees/graphs. You don't need competitive-programming depth, you need "can solve a medium problem cleanly."

---

## Phase 4 — Deep Learning (Weeks 10–14)

**Primary:**
- CampusX — *100 Days of Deep Learning* playlist
- CampusX — *Practical Deep Learning using PyTorch* playlist (do this right after/alongside the theory series so the math doesn't stay abstract)

**Supplement (genuinely essential, not optional):**
- 3Blue1Brown — *"Neural Networks"* series (the visual explanation of backpropagation that makes it finally click)
- Andrej Karpathy — *"Neural Networks: Zero to Hero"* playlist, starting with *"The spelled-out intro to neural networks and backpropagation"* — Karpathy builds things from raw Python with no framework, which is the single best way to actually understand what's happening under the hood instead of just calling `.fit()`

**Cover:** perceptron, activation functions, forward/backward propagation, loss functions, optimizers (SGD, Adam), regularization (dropout, batch norm), CNNs (image tasks), RNNs/LSTMs (sequence tasks), basics of PyTorch (tensors, autograd, `nn.Module`, training loops).

**Project:** Image classifier (CNN) on a dataset like CIFAR-10 or your own images, built and trained in PyTorch. Push it with a clear README explaining your architecture choices.

---

## Phase 5 — NLP Fundamentals (Weeks 14–16)

**Primary:**
- CampusX — *Natural Language Processing (NLP)* playlist

**Cover:** text preprocessing (tokenization, stemming/lemmatization, stopwords), Bag of Words, TF-IDF, Word2Vec/embeddings, intro to RNN/LSTM for text, **intro to the Transformer architecture** (this is the bridge into the LLM phase — don't rush past "Attention Is All You Need" intuition).

**Supplement for transformer intuition:**
- 3Blue1Brown — the Transformer/attention visual explainer video

---

## Phase 6 — LLMs & Generative AI (Weeks 16–19)

This is where most current AI-role job descriptions actually live right now.

**Primary:**
- Andrej Karpathy — *"Let's build GPT: from scratch, in code, spelled out"* and his *"Deep Dive into LLMs like ChatGPT"* / *"LLMs in an hour"* type videos — this is widely considered the best from-scratch LLM explainer on YouTube, by someone who actually built these at OpenAI/Tesla
- CampusX — *Generative AI using LangChain* playlist (practical building: calling LLM APIs, prompt engineering, building chains, RAG pipelines)

**Cover:** transformer architecture deep-dive (attention, multi-head attention, positional encoding), how GPT-style models are trained (pretraining → fine-tuning → RLHF, at a conceptual level), tokenization, embeddings & vector databases, prompt engineering, Retrieval-Augmented Generation (RAG), basics of fine-tuning (LoRA conceptually), LangChain fundamentals (chains, memory, retrievers).

**Project:** Build a RAG-based "chat with your documents" app using LangChain + a vector DB + an LLM API. This is portfolio piece #2 and very interview-relevant right now.

---

## Phase 7 — Agentic AI (Weeks 19–21)

The newest and currently highest-demand layer. This is "LLM + memory + tools + autonomy."

**Primary:**
- CampusX — *Agentic AI using LangGraph* playlist
- CampusX — *Model Context Protocol (MCP)* playlist (MCP is becoming a standard way agents connect to tools/data — worth knowing for interviews)

**Supplement:**
- LangChain's official YouTube channel (framework creators, practical and current)
- CrewAI's own quickstart docs/videos (genuinely the easiest framework to get a first working multi-agent system in, good for building intuition fast)
- Cole Medin — production-style agent-building content (good for seeing how agents are built for real use cases, not just demos)

**Cover:** what makes something an "agent" vs a chatbot, tool calling/function calling, agent memory, multi-agent orchestration (LangGraph/CrewAI), planning & reasoning loops, MCP basics.

**Project:** Build one multi-agent system that does something real — e.g., an agent that researches a topic, summarizes it, and emails/saves the result, using tools. This is portfolio piece #3 — and the most "currently in demand" one.

---

## Phase 8 — Deployment, MLOps Basics & Polish (Weeks 9–10 and ongoing)

Don't skip this — "I built a model in a notebook" doesn't get hired; "I shipped something that runs" does.

**Primary:**
- CampusX — *FastAPI for Machine Learning* playlist
- Git & GitHub basics (CampusX has a playlist for this too — make sure your repo history actually looks professional)

**Cover:** wrapping a model in a FastAPI/Flask endpoint, basic Docker (containerizing your app), Streamlit for quick demo UIs, basic CI awareness, writing a clean README for every project.

---

## Weeks 21–22 — Portfolio + Interview Prep

- Polish your 3 main projects (ML end-to-end, RAG app, Agentic system) with clean READMEs, demo videos/GIFs, and deployed links if possible (Streamlit Cloud/HuggingFace Spaces are free)
- Write/update your resume around these 3 projects + DSA practice
- Revisit your Anki deck and Sunday notes — do a full "explain every phase out loud to yourself" pass
- Mock interviews: ML theory questions (the "why logistic regression not linear regression" type), one DSA round, one project deep-dive round
- LinkedIn: post about your projects as you build them — recruiters do look, and writing about it forces you to articulate it, which fights the forgetting problem too

---

## Quick Reference — Channel Cheat Sheet

| Need | Channel/Playlist |
|---|---|
| Python from scratch | CampusX Python / CodeWithHarry |
| Math intuition (visual) | 3Blue1Brown |
| Stats explained simply | StatQuest |
| Full ML curriculum | CampusX "100 Days of ML" |
| Second opinion on ML algos | Krish Naik / codebasics |
| Full DL curriculum | CampusX "100 Days of DL" + "Practical DL w/ PyTorch" |
| Deep neural net intuition | 3Blue1Brown Neural Networks series |
| Build LLM from scratch | Andrej Karpathy ("Zero to Hero", "Let's build GPT") |
| NLP fundamentals | CampusX NLP playlist |
| LangChain / RAG practical | CampusX "GenAI using LangChain" |
| Agentic AI / LangGraph | CampusX "Agentic AI using LangGraph" + LangChain official |
| DSA for AI interviews | CampusX "DSA for AI" |
| Deployment | CampusX "FastAPI for ML" |

---

## The one thing to remember

5 months is genuinely enough time **if** every topic ends in code, not just a checked-off video. The moment you catch yourself watching 3 videos in a row without typing anything, stop, close the laptop's recording, open VS Code, and rebuild what you just watched from memory. That single habit is what will separate "I learned this" from "I forgot this in 3 weeks," which is exactly the problem you said you have.

Good luck — start tonight, and don't aim for perfect, aim for consistent.
