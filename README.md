
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

## Checkpoint Assets

The validated paper setup contains 17 runtime manifests that reference 21
unique SGG checkpoint files. This includes released checkpoints for
TDE-Motifs, EGTR, KERN, OpenPSG Motifs, PSGFormer, PSGTR, VCTree, BGNN, RelTR,
and SGTR, together with the final PredCls/SGCls/SGDet checkpoints for the
trained Motifs and Transformer panels. The SGG checkpoints occupy 28.6 GiB.
The six Experiment I-A foundation backbones occupy a further 4.4 GiB.

The validated 29.7 GiB archive bundle is available from the
[read-only OneDrive folder](https://1drv.ms/f/c/bbaa76995e4a814f/IgCQZ7iYJDccSJI8ZuWpmCHbAYAUMITf-03j9fxU5yVb5vg?e=rd23fq).
Download `README.md`, `SHA256SUMS`, and the eight `.tar.zst` parts, then verify
every part before extraction.

Checkpoints are not tracked in Git. Acquire released weights through
`THIRD_PARTY_ASSETS.md` and place every file at its declared relative path.
Each runtime manifest records the expected SHA-256 value, model family,
ontology, supported task, and evaluation contract. Periodic training
snapshots, prediction caches, datasets, smoke outputs, and logs are not part
of the checkpoint bundle.

See `REPRODUCIBILITY.md` for the full command and output map,
`THIRD_PARTY_ASSETS.md` for provenance and hashes, and
`UPLOAD_CHECKLIST.md` for the KDD artifact checklist.
