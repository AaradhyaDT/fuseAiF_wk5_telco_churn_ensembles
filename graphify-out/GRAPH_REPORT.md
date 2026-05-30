# Graph Report - .  (2026-05-30)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 10 nodes · 10 edges · 3 communities (2 shown, 1 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]

## God Nodes (most connected - your core abstractions)
1. `Aaradhya Dev Tamrakar` - 6 edges
2. `Telco Churn Tree-Based Ensemble Pipeline` - 3 edges
3. `Text-to-SQL Agentic Pipeline` - 2 edges
4. `Week 5 Project Guide: Tree-Based Models & Ensembles` - 2 edges
5. `Telco Customer Churn Dataset` - 2 edges
6. `Fusemachines AI Fellowship` - 1 edges
7. `Gesture-Controlled Self-Balancing Robot (GCSBR)` - 1 edges
8. `Telco Customer Churn ML Pipeline` - 1 edges
9. `Alpha Android Super-App` - 1 edges
10. `IT4D 2026 Concept Paper` - 1 edges

## Surprising Connections (you probably didn't know these)
- `Telco Churn Tree-Based Ensemble Pipeline` --references--> `Week 5 Project Guide: Tree-Based Models & Ensembles`  [INFERRED]
  AARADHYA_MASTER_v59.md → W5_Project_Guide.md
- `Telco Churn Tree-Based Ensemble Pipeline` --references--> `Telco Customer Churn Dataset`  [EXTRACTED]
  AARADHYA_MASTER_v59.md → W5_Project_Guide.md

## Communities (3 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.40
Nodes (5): Aaradhya Dev Tamrakar, Alpha Android Super-App, Fusemachines AI Fellowship, Gesture-Controlled Self-Balancing Robot (GCSBR), Telco Customer Churn ML Pipeline

### Community 1 - "Community 1"
Cohesion: 1.00
Nodes (3): Telco Churn Tree-Based Ensemble Pipeline, Telco Customer Churn Dataset, Week 5 Project Guide: Tree-Based Models & Ensembles

## Knowledge Gaps
- **5 isolated node(s):** `Fusemachines AI Fellowship`, `Gesture-Controlled Self-Balancing Robot (GCSBR)`, `Telco Customer Churn ML Pipeline`, `Alpha Android Super-App`, `IT4D 2026 Concept Paper`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Aaradhya Dev Tamrakar` connect `Community 0` to `Community 1`, `Community 2`?**
  _High betweenness centrality (0.889) - this node is a cross-community bridge._
- **Why does `Telco Churn Tree-Based Ensemble Pipeline` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.389) - this node is a cross-community bridge._
- **Why does `Text-to-SQL Agentic Pipeline` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.222) - this node is a cross-community bridge._
- **What connects `Fusemachines AI Fellowship`, `Gesture-Controlled Self-Balancing Robot (GCSBR)`, `Telco Customer Churn ML Pipeline` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._