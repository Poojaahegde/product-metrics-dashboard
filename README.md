# Product Metrics Dashboard 📊 — AI-Augmented Growth & Retention Tracker

> **Simulate, visualize, and interpret core product health metrics — the way a data-driven PM would.**
>
> [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org) [![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)](https://streamlit.io) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
>
> ---
>
> ## 🚀 Product Overview
>
> **The Problem:** Most PMs talk about metrics (DAU, retention, conversion) but can't quickly prototype a live dashboard to demonstrate product health thinking. Data teams are often backlogged. Waiting weeks for a BI dashboard to be built means decisions get delayed — or get made without data.
>
> **The Solution:** This interactive Streamlit dashboard generates synthetic DAU, retention cohort, and conversion funnel data and visualizes it in real-time. PMs can adjust growth scenarios, simulate retention drops, and explore funnel optimization — without waiting for a data team or connecting to live systems.
>
> **The Impact:**
> - 🚀 Lets PMs **prototype metric dashboards** and communicate data strategy visually — in minutes
> - - 🔍 Demonstrates **how to detect anomalies** in DAU trends, retention cliffs, and conversion drop-offs
>   - - 🎓 Provides a **hands-on sandbox** for experimenting with growth scenarios and what-if analysis
>     - - 📣 Turns abstract metric conversations into **concrete, visual product narratives**
>      
>       - ---
>
> ## 🎯 Why This Matters (Product Perspective)
>
> Every PM interview involves metrics. Every product review requires data. This dashboard shows I don't just talk about metrics — I build tools to track and visualize them. It demonstrates that I understand the **North Star metric framework**, the difference between leading and lagging indicators, and how to communicate product health visually to stakeholders.
>
> ---
>
> ## 🧠 Metrics Framework
>
> ### Core Metrics Tracked
>
> | Metric | What It Measures | Why It Matters |
> |---|---|---|
> | **DAU (Daily Active Users)** | Engagement volume day-over-day | Leading indicator of product health and growth momentum |
> | **Retention Rate (D1, D7, D30)** | % of users who return after first use | Best predictor of long-term product value (LTV proxy) |
> | **Conversion Rate** | % of users who complete a key action | Direct revenue and activation signal |
> | **DAU/MAU Ratio** | Stickiness — how often monthly users return | Measures habit formation (target: >0.5 for sticky products) |
>
> ### Anomaly Detection Logic
> - **DAU drop > 15% week-over-week** → Flagged as warning
> - - **Retention D7 < 20%** → Product-market fit concern
>   - - **Conversion drop > 10% in 3 days** → Funnel issue alert
>    
>     - ---
>
> ## 🛠 Tech Stack
>
> | Layer | Technology |
> |---|---|
> | UI | Streamlit |
> | Data Generation | NumPy (synthetic time-series) |
> | Data Processing | Pandas |
> | Visualization | Matplotlib (trend lines, cohort heatmaps, funnel charts) |
> | Language | Python 3.8+ |
>
> ---
>
> ## 📊 Sample Dashboard Outputs
>
> **DAU Trend (30-day simulated):**
>
> | Week | Avg DAU | WoW Change | Signal |
> |---|---|---|---|
> | Week 1 | 4,820 | Baseline | — |
> | Week 2 | 5,140 | +6.6% | Growing |
> | Week 3 | 5,380 | +4.7% | Growing |
> | Week 4 | 4,720 | -12.3% | ⚠️ Alert: Investigate |
>
> **Retention Cohort (D1 / D7 / D30):**
>
> | Cohort | D1 Retention | D7 Retention | D30 Retention |
> |---|---|---|---|
> | Jan Users | 62% | 38% | 18% |
> | Feb Users | 65% | 41% | 22% |
> | Mar Users | 59% | 35% | 16% |
>
> **PM Insight:** Feb cohort has notably better D30 retention — correlate with product changes shipped in Feb to identify what drove improvement.
>
> **Conversion Funnel:**
>
> | Step | Users | Conversion |
> |---|---|---|
> | Visited landing page | 10,000 | — |
> | Started onboarding | 6,200 | 62.0% |
> | Completed onboarding | 3,800 | 61.3% |
> | First core action | 2,100 | 55.3% |
> | Retained at D7 | 860 | 41.0% |
>
> **PM Insight:** Biggest drop is between onboarding completion and first core action (55.3%). This is the activation gap — a common PM optimization target.
>
> ---
>
> ## 📸 Demo Instructions
>
> ```bash
> # 1. Clone the repo
> git clone https://github.com/Poojaahegde/product-metrics-dashboard.git
> cd product-metrics-dashboard
>
> # 2. Install dependencies
> pip install streamlit pandas numpy matplotlib
>
> # 3. Launch the dashboard
> streamlit run app.py
> ```
>
> Open **http://localhost:8501** in your browser. Use the sidebar sliders to adjust growth rate, retention parameters, and conversion rates to explore different product health scenarios.
>
> ---
>
> ## 🎯 Product Thinking Layer
>
> ### 👥 Target Users
> - **Product Managers** who need to prototype metric dashboards quickly without waiting for data teams
> - - **APMs / Associate PMs** building intuition for product health metrics and what anomalies look like
>   - - **Startup founders** who need a fast way to visualize early product performance metrics
>    
>     - ### 😣 Pain Points Solved
>     - 1. **No live dashboard** — Many early-stage or small teams don't have a BI tool set up yet
>       2. 2. **Metric illiteracy** — PMs often describe metrics they want to track but can't show what "healthy" looks like
>          3. 3. **Slow iteration** — Waiting for data engineering to build dashboards delays product decisions
>            
>             4. ### 🧩 Key Product Decisions Made
>             5. - **Synthetic data over real data connection (v1):** Eliminates data privacy/security concerns, works for any audience, and focuses the tool on metric interpretation rather than data plumbing
>                - - **DAU + Retention + Conversion as core trio:** These three metrics cover the full user lifecycle (acquisition → engagement → monetization) — the minimum viable metric set for any product
>                  - - **Anomaly flags baked in:** Not just visualization — the dashboard tells you *when something is wrong*, which is the actual product value
>                    - - **Streamlit for interactivity:** Sliders for scenario simulation transform this from a static chart into an interactive decision-support tool
>                     
>                      - ### 🗺 Future Roadmap
>                      - | Priority | Feature | Expected Impact |
>                      - |---|---|---|
>                      - | P0 | Connect to real data via SQL or CSV upload | Transform from demo to production tool |
>                      - | P0 | North Star metric tracking with goal vs. actual | Align team on what matters most |
>                      - | P1 | AI-generated metric commentary ("DAU dropped 12% — possible causes: ...") | Automated insight generation using LLM |
>                      - | P1 | Retention cohort heatmap (week x cohort) | Industry-standard retention visualization |
>                      - | P2 | A/B test results view: control vs. variant metrics | Experiment-aware dashboard |
>                      - | P2 | Slack/email alerts when metrics breach thresholds | Proactive PM monitoring |
>                      - | P3 | Exportable PM weekly metrics report (PDF) | Stakeholder communication artifact |
>                     
>                      - ---
>
> ## 📁 Project Structure
>
> ```
> product-metrics-dashboard/
> ├── app.py               # Streamlit dashboard — DAU, retention, conversion visualization
> ├── README.md            # This file
> ```
>
> ---
>
> ## 🔗 Related Projects in This Portfolio
> - [**ScopeCreep**](https://github.com/Poojaahegde/scopecreep) — AI-powered real-time scope drift detector
> - - [**PriorityLens**](https://github.com/Poojaahegde/prioritylens) — AI feature prioritization engine with bias detection
>  
>   - ---
>
> *Built as part of an AI PM portfolio — demonstrating deep metrics fluency and the ability to turn data strategy into working tools.*
