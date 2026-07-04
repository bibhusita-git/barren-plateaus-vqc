# Research Notebook — Barren Plateaus in Variational Quantum Circuits

Dated log of work, decisions, results, and open questions for this project.
Newest entries at the top.

---

## 04-07-2026

**Did:**
- Set up project environment (PennyLane 0.45.1, Python 3.12.3)
- Wrote and ran `reproduce_barren_plateau.py` — reproduces the barren plateau
  effect from McClean et al. (2018) for a random hardware-efficient ansatz
- Fixed a terminal output buffering issue (no output was printing; resolved
  by running with `python -u`)
- Set up GitHub repo (`barren-plateaus-vqc`), organized into `src/` and
  `results/` folders
- Wrote initial `README.md`

**Result:**
- Qubit range: 2, 4, 6, 8. Depth: 4. Samples per qubit count: 50.
- Gradient variance decays exponentially with qubit count (see
  `results/gradient_variance_vs_qubits.png`)
- Fitted slope of log(variance) vs. qubit count: **-0.6833**
- Theoretical prediction for an ideal unitary 2-design: **-0.693** (ln(1/2))
- These are close (~1.5% difference), consistent with McClean et al.'s
  central claim.

**Notes / things to revisit:**
- Current run uses a small sample size (50) and narrow qubit range (up to 8).
  Should scale up to ~200 samples and extend to 10-12 qubits for a more
  robust result.
- Haven't yet read McClean et al.'s full derivation (unitary 2-design /
  Haar-measure concentration argument) — need to understand this well enough
  to explain in an interview, not just cite the empirical match.
- Depth was fixed at 4 throughout. McClean et al.'s claim is tied to circuit
  depth approaching a 2-design, not qubit count alone — worth testing how
  the slope changes at, e.g., depth 2 vs. depth 8.

**Next steps:**
1. Scale up the experiment (more samples, wider qubit range)
2. Read McClean et al. results section, compare their numbers to mine
3. Start planning the local vs. global cost function extension
   (Cerezo et al., 2021)

---

<!--
Template for future entries — copy this block for each new day of work:

## YYYY-MM-DD

**Did:**
-

**Result:**
-

**Notes / things to revisit:**
-

**Next steps:**
-

---
-->
