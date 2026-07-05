# Research Notebook — Barren Plateaus in Variational Quantum Circuits

Dated log of work, decisions, results, and open questions for this project.
Newest entries at the top.

---

## 2026-07-05

**Did:**
- Scaled up the experiment: qubit range extended from [2,4,6,8] to
  [2,4,6,8,10,12], sample size increased from 50 to 200 per qubit count
- Debugged a file organization issue — the plot was saving to `src/`
  instead of `results/` due to a relative path default in `plot_results()`;
  fixed the `save_path` argument and cleaned up stray duplicate files
- Re-ran the experiment with corrected paths and scaled-up parameters

**Result:**
- Qubit range: 2, 4, 6, 8, 10, 12. Depth: 4. Samples per qubit count: 200.
- Gradient variance decays exponentially across the full range, spanning
  roughly 3 orders of magnitude (0.13 down to ~8.8e-5)
- Fitted slope of log(variance) vs. qubit count: **-0.7207**
- Theoretical prediction: **-0.693** (ln(1/2)) for an ideal 2-design
- This is a noticeably cleaner and more convincing result than the initial
  4-point run — six data points spanning a wider range gives a much more
  reliable fit.

**Notes / things to revisit:**
- Still haven't read McClean et al.'s full derivation of the 2-design
  concentration bound — next priority before moving to Week 2.
- Worth remembering for future scripts: always use explicit relative paths
  (e.g., `../results/...`) rather than bare filenames when saving outputs,
  to avoid outputs landing in whatever directory the script happens to be
  run from.

**Next steps:**
1. Read McClean et al. results section, compare their reported numbers/setup
   to mine
2. Update README with the new slope value (-0.72) and 6-point plot
3. Begin planning the local vs. global cost function extension
   (Cerezo et al., 2021)

---

## 2026-07-04

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
