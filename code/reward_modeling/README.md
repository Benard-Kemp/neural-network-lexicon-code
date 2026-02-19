# Reward Modeling (Pairwise Preferences) — PyTorch

This folder contains a minimal PyTorch example of **reward modeling** trained from **pairwise preferences**.

- Script: `reward_modeling_pairwise.py`
- Objective: maximize `log sigmoid(r_chosen - r_rejected)` (Bradley–Terry / logistic)

Run:
```bash
python reward_modeling_pairwise.py