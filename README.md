# Metric-Based Emotional NPCs using Shared Fuzzy Logic in Top-Down Games

## 📌 Overview
This repository contains the research artifacts for the paper:

**Metric-Based Emotional NPCs using Shared Fuzzy Logic in Top-Down Games**

This project proposes a **Shared Fuzzy Logic architecture** that enables large numbers of Non-Player Characters (NPCs) to exhibit believable emotional behaviour while maintaining real-time performance and low memory usage.

The repository is created to support:
- Research reproducibility  
- Open science requirements  
- Dataset and documentation sharing  

---

## 🎯 Research Motivation
Traditional NPC AI often relies on deterministic logic such as FSM or Behavior Trees, which leads to predictable behaviour and reduced player immersion.

Emotion-driven NPCs improve realism, but scaling emotional AI for many NPCs introduces:
- High CPU usage  
- Large memory overhead  
- Poor scalability in real-time games  

This research explores how **Shared Fuzzy Logic** can solve this trade-off.

---

## 🧠 Proposed Solution
We introduce a **centralized Fuzzy Inference System (FIS)** shared by all NPCs.

Instead of each NPC owning a full AI brain:
- NPCs send their state to a shared FIS  
- The system returns emotional behaviour probabilities  
- NPCs execute actions individually  

**Pipeline**

`Input Metrics → Shared FIS → Decision Weighting → NPC Action`

Input metrics:
- Health Ratio (H)  
- Distance to Player (D)  
- Game Stage (S)  

Output behaviours:
- Attack  
- Retreat  
- Idle  

---

## 📊 Current Project Status
⚠️ Research in development stage  

This repository currently contains:
- Synthetic dataset (for methodology validation)
- System diagrams and figures
- Research documentation
- Experimental plan  

The actual game experiment has **not yet been conducted**.

---

## 📁 Repository Structure

```
shared-fuzzy-npc-ai/
│
├── dataset/
│   └── npc_player_interaction_dataset.csv
│
├── docs/
│   ├── system_pipeline.png
│   ├── fuzzy_architecture.png
│   └── experimental_workflow.png
│
├── paper/
│   └── research_paper.pdf
│
├── LICENSE
└── README.md
```


---

## 📂 Dataset
Synthetic dataset simulating NPC-player interactions.

Location:
`dataset/npc_player_interaction_dataset.csv`

This dataset is a **placeholder** and will be replaced with real gameplay data in future work.

---

## 🔬 Research Methodology
Research method: **Experimental benchmarking**

Planned evaluation:
1. Compare per-NPC FIS vs Shared FIS  
2. Compare Mamdani vs Sugeno inference  
3. Measure:
   - Frame time
   - Memory usage
   - AI processing throughput

---

## 👥 Authors
**Students**
- Darryl Arief Tananjaya  
- Adriel Kevin Jonathan  
- Jocelyn Tania Harjanto  

**Supervisor**
- Kristien Margi Suryaningrum, S.Kom., M.Cs.  
School of Computer Science  
Bina Nusantara University

---

## 📜 License
Apache License 2.0
