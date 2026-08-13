# Side-Hustle Map — Cracking DA / BA / DE / Product Analyst Interviews *While* You Grind Toward AI

Good instinct. Your main roadmap overlaps with these 4 roles way more than people realize — SQL, Pandas, and stats are basically the shared foundation under all of them. This doc tells you **exactly when** (which week/phase of your main roadmap) you become interview-ready for each, and what small **extra add-on** you need bolted onto the core syllabus to actually clear that specific interview.

Think of your main roadmap as the trunk of a tree. These 4 roles are short branches off it — you don't need to finish the whole tree to harvest a branch.

---

## The Checkpoint Table (the part you actually need)

| Role | ✅ Ready to interview after (from main roadmap) | ➕ Extra add-on needed | Extra time |
|---|---|---|---|
| **Data Analyst** | Phase 2 (NumPy/Pandas/SQL) + Phase 1 stats — roughly end of **Week 5** | Excel mastery, Power BI/Tableau, advanced SQL (window functions), case-study communication | ~1–1.5 weeks |
| **Business Analyst** | Phase 2 (SQL/Pandas) + Phase 1 stats — roughly end of **Week 5** | Business case frameworks (SWOT, MECE, market sizing), Excel + PowerPoint, stakeholder-communication practice | ~1 week |
| **Product Analyst** | Phase 2 + Phase 1 stats + model-evaluation metrics from Phase 3 — roughly end of **Week 9–10** | A/B testing deep-dive, product metrics (funnels, retention, North Star metric), product-sense case studies | ~1.5–2 weeks |
| **Data Engineer** | Phase 0 (Python) + Phase 2 (SQL) + DSA side-track + Phase 8 (Docker) — roughly end of **Week 10–12** | Apache Airflow, Spark basics, data warehousing concepts, cloud basics (AWS/GCP), pipeline system design | ~3–4 weeks |

**Reading this table:** the moment you hit that checkpoint week in your main roadmap, you don't have to wait — pause, do the extra add-on for that role, and you can start sending applications/giving interviews for it while continuing the main grind toward the AI role.

---

## 1. Data Analyst — ready ~Week 5

You already have Pandas, SQL, and basic stats from the main roadmap. What's missing is the "tooling + business polish" layer.

**Add-on topics:**
- **Excel**: pivot tables, VLOOKUP/XLOOKUP, conditional formatting, basic dashboards
- **Power BI or Tableau** (pick one — Power BI if you're in India/targeting Indian companies, it's more commonly asked): DAX basics, building dashboards, slicers/filters
- **Advanced SQL for interviews**: window functions (RANK, LAG/LEAD), CTEs, subqueries — this is what separates "knows SQL" from "passes the SQL round"
- **Communicating insights**: turning a number into a one-line business takeaway ("revenue dropped 12% in Q3, driven mainly by region X")

**Resources:**
- CampusX — *Power BI* playlist
- **techTFQ** (Thoufiq) — best channel specifically for interview-style SQL questions, advanced queries, window functions
- **Alex The Analyst** — full Data Analyst career path, SQL, Excel, portfolio/resume advice, mock interview content
- StrataScratch / InterviewQuery (practice platforms, not just videos) — real SQL interview questions companies have actually asked

**Typical interview format:** SQL live coding round → Excel/BI tool round → a small case study ("here's messy data, find an insight and present it") → resume/project walkthrough.

---

## 2. Business Analyst — ready ~Week 5

This role is the *least* coding-heavy of the four — it's judgment + communication wearing a data costume. Your SQL/stats foundation is already overkill for most BA interviews; the real gap is **case-interview thinking**.

**Add-on topics:**
- **Case frameworks**: SWOT, MECE (Mutually Exclusive, Collectively Exhaustive), Porter's Five Forces, the "4 C's"
- **Case types**: market sizing ("estimate how many X are sold in India per year"), profitability cases ("why did profit drop"), market entry, operations improvement
- **Structuring an answer out loud**: state the problem clearly → form a hypothesis → ask for the data you need → walk through the math → land on a clear recommendation (not just "it depends")
- Excel + PowerPoint basics for presenting findings

**Resources:**
- "Hacking the Case Interview" style content (originally consulting-focused, but tech BA interviews borrow the same case structure) — search YouTube for "business analyst case interview framework"
- Practice with a friend: take any real product (Swiggy, Zomato, Ola) and do a 15-min mock case ("Ola's ride completion rate dropped 10% last month, why, and what would you do")

**Typical interview format:** Behavioral round (your past projects, STAR method) → a case study round (live or take-home) → sometimes a basic SQL/Excel screen → final round often with someone product-facing.

---

## 3. Product Analyst — ready ~Week 9–10

This is the most "AI-roadmap-adjacent" of the four, because by Week 9–10 you've already touched model evaluation metrics (precision/recall, etc.) and basic stats — which is most of what's needed for the A/B-testing half of this interview.

**Add-on topics:**
- **A/B testing deep-dive**: null/alternative hypothesis, p-values, statistical significance vs. practical significance, sample size, novelty effects, what to do when a metric doesn't move or moves in only one segment
- **Product metrics literacy**: funnels, retention/churn, DAU/MAU, North Star metric, how to pick the *right* metric for a feature (not just "more users = good")
- **Product-sense case studies**: "how would you measure the success of feature X," "a metric dropped 15% overnight, what's your first move"

**Resources:**
- StatQuest's hypothesis testing / p-value videos (you'll already have watched these in Phase 1 — just revisit with an A/B-testing lens)
- StrataScratch and InterviewQuery — both have dedicated Product Analyst question banks with real SQL + product-sense questions from actual companies (Meta, Amazon, Spotify-style interviews)
- Search "product sense case study framework" — most good breakdowns follow: clarify → structure (e.g. by user segment/funnel stage) → hypothesize → prioritize → recommend

**Typical interview format:** SQL round → product-sense/case round (totally open-ended, they're grading your thinking process, not a "correct" answer) → sometimes an A/B-testing stats question → behavioral.

---

## 4. Data Engineer — ready ~Week 10–12 (biggest extra add-on)

Heads up: this is the role where your main roadmap covers the *least* ground relative to the other three. ML/DL skills barely show up in DE interviews — what you need instead is backend/infrastructure thinking. Your Python + SQL + DSA foundation is necessary but not sufficient here.

**Add-on topics (this is essentially a mini-syllabus of its own):**
- **ETL/orchestration**: Apache Airflow (or Prefect/Dagster) — how pipelines are scheduled and monitored
- **Big data processing**: Apache Spark basics (PySpark), why distributed processing exists, partitioning
- **Data warehousing concepts**: star schema vs snowflake schema, OLAP vs OLTP, Snowflake/BigQuery/Redshift at a conceptual level
- **Cloud basics**: pick one (AWS is most commonly asked) — S3, basic IAM, a managed data warehouse service
- **System design for data pipelines**: "design a pipeline that ingests clickstream data and serves it for analytics" type questions — this is the senior-style question even juniors get asked a lighter version of

**Resources:**
- **Sumit Mittal** — covers the traditional + modern big data stack (Spark, Hadoop, Hive, Kafka) with genuinely strong interview-prep content including pipeline system-design questions
- CampusX doesn't have a dedicated DE playlist, so this is the one role where you'll lean on outside channels more — freeCodeCamp has a full "Data Engineering" course-length video that's a good single-resource starting point
- Practice explaining a pipeline design out loud — even just to yourself or a rubber duck — this is what trips people up most, not the tool syntax

**Typical interview format:** SQL round (often harder than DA/BA rounds) → Python/DSA coding round → a pipeline/system-design discussion → sometimes a tool-specific round (Spark/Airflow) depending on the company's stack.

---

## How to actually run this side-hustle without breaking your main grind

1. **Don't context-switch mid-week.** Pick one weekend day every 1–2 weeks as your "interview-prep day" — do the add-on content in a block, not scattered across weekday evenings where it'll eat into your main roadmap time.
2. **Reuse your `ai-journey` repo.** Add a `/interview-prep` folder with SQL practice queries, case-study notes, A/B testing notes. Same anti-forgetting logic applies here — write, don't just watch.
3. **Order of attack if you want quick wins first:** Data Analyst → Business Analyst (these two are reachable fastest and have high interview volume) → Product Analyst → Data Engineer (biggest extra lift, but pairs naturally with your later DL/deployment phases).
4. **Every case study or SQL problem you solve, log one line in Anki:** the question + the one-sentence "trick" you used. These interview question banks repeat patterns constantly — recognizing the pattern is 80% of the battle.

---

## Practice platforms worth bookmarking now

- **StrataScratch** — real SQL + product-sense questions from actual companies
- **InterviewQuery** — DA/BA/Product Analyst question banks + guides
- **LeetCode (SQL section specifically, not just DSA)** — for the SQL rounds across all four roles

You don't need to finish your AI roadmap to start earning/interviewing. The branch points above are real — hit the checkpoint, bolt on the add-on, and go take the interview.
