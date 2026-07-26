# GroundedSGG-Bench

GroundedSGG-Bench decomposes scene graph generation into spatial support,
object identity, and relation prediction. The release contains the benchmark
code, fixed experiment contracts, paper-result snapshots, and one entry point
for the complete five-experiment workflow.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .

bash scripts/reproduce_paper.sh preflight
bash scripts/reproduce_paper.sh smoke
```

After the datasets, official repositories, and checkpoints listed in
`THIRD_PARTY_ASSETS.md` are installed:

```bash
PAPER_RUN_ID=reviewer_reproduction \
  bash scripts/reproduce_paper.sh formal
```

The formal launcher runs:

| Stage | Paper experiment |
| --- | --- |
| `1a` | PSG support-conditioned object probes |
| `1a_external` | GQA/VRD box-only object diagnostics |
| `1b` | VG PredCls relation-depth component study |
| `2a` | Endpoint-agreement observational audit |
| `2b` | Controlled live endpoint interventions |
| `3` | Strict motif-conditioned terminal audit |
| `4_native` | Eleven native full-split SGDet runs |
| `4_depth` | Matched Motifs/Transformer tri-task evaluation |
| `5` | TDE-Motifs, two modes, three seeds |
| `5_posthoc` | Selected VG test plus frozen GQA/VRD transfer |

Use `PAPER_STAGES="3 5 5_posthoc"` to reproduce a subset. Every GPU task emits
prefixed progress, writes a dedicated log, and supports `RESUME=1`.

## Reproduction Contract

- Smoke outputs never populate formal tables.
- Model selection uses the disjoint VG validation holdout only.
- Prediction caches can support standard evaluation, but not live
  interventions or gradient-based mitigation.
- Dataset ontologies remain native; cross-dataset values are not a leaderboard.
- Missing support, incomplete coverage, and reference mismatches remain
  explicit statuses rather than being converted to zero.
- Experiment V is the preregistered one-family TDE-Motifs study with learning
  rate `3e-5`, frozen relation parameters, and three seeds.

See `REPRODUCIBILITY.md` for the full command and output map,
`THIRD_PARTY_ASSETS.md` for provenance and hashes, and
`UPLOAD_CHECKLIST.md` for the KDD artifact checklist.
