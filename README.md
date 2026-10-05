
# GroundedSGG-Bench

## 2026-10-05 Rebuttal Update

Updated code and selected evidence are published separately so that the original
submission snapshot remains traceable. This update contains research artifacts,
not reviewer reports or the private author response.

- **Revised code and evidence:** [rebuttal-20261005](https://github.com/welkingliu/rebuttal-20261005).
  The additional matched-control revision is commit
  `a469a347b3fac32cbdaba7fbbe017df2896db5e8` (450 files covered by
  `MANIFEST.sha256`, locally verified). Earlier revision `d4c4742` remains
  in the repository history; do not confuse its 432-file manifest with this update.
- **Prediction records and supplemental checkpoints:** [OneDrive read-only folder](https://1drv.ms/f/c/bbaa76995e4a814f/IgDQLM6an3FGR4QcPttIInadAfUA6Bp_-s6IHhmloTWIS98?e=qabT4l).
  The root retains `paired_channel_records_20261005.zip`, `README.md`, and `SHA256SUMS`.
  The ZIP contains 4,000 NPZ records across two model/task runs and is
  2,510,792,544 bytes (approximately 2.34 GiB).
  An unsigned-in download on 2026-10-05 matched the published SHA-256 checksum
  and passed ZIP integrity checks. SHA-256:
  `f2d2e803044031c2e58f8a3c6459e20e82ca4788ea443e488d9b836f9cbcae31`.

### Additional Controls and Checkpoints

- `evidence/matched_controls_20261005/`: the new
  `matched_identity_controls_20261005.zip`, with 4,000 image-level JSON/NPZ pairs
  and semantic paired statistics; 6,393,267 bytes. SHA-256:
  `48f292e02221e986aaa7cd1042675338b9c7ca4ccf84578cabc8a44c9ed52995`.
- `checkpoints/revision_20261005/`: three newly trained plain Neural Motifs
  task checkpoints and the corrected Transformer SGDet checkpoint, with
  configuration, provenance and checksums (four ZIPs, approximately 4.95 GiB).
  Apply the bundled Transformer inference overrides, not just its saved config.
- These supplements passed local checksum checks. Cloud upload/download
  verification of the new files remains pending; the historical archive's
  successful download check does not certify the supplements.

With visual evidence and replacement sites fixed, reference labels in the
frequency-prior channel improve predicate Top-1 by 5.45 pp for Motifs SGCls
and 8.80 pp for Transformer SGDet. Frequency-stratum-matched incorrect labels
instead reduce accuracy by 10.40--11.37 and 14.21--14.71 pp across three
intervention seeds. These post-hoc diagnostics use previously inspected images;
they are not independent confirmation or deployable repairs. Semantic-channel
contrasts remain model dependent. The joint SGCls/SGDet repair gate remains unmet.

See the revised repository's `evidence/R23_controls/` for summaries, protocols,
source provenance and the archive checksum. Preserve the original artifacts;
new controls do not silently replace historical records.

### How to Interpret the Update

- Fixed-visual paired interventions separate semantic-class and frequency-prior
  inputs. Ground-truth label substitutions are diagnostic, not deployable repairs.
- Corrected Motifs/Transformer task results pass the declared reference-metric
  tolerance; this does not establish identical upstream training settings.
- A bounded SAM probe refit checks optimization sensitivity. Raw-feature refits
  are distinct from the historical normalized-probe results.
- **Original Experiment V is reinterpreted as affine object-score calibration.**
  Its nominal relation penalties do not backpropagate into the updated readout.
  Its results do not demonstrate effective relation-protective training.
- **Historical Experiment III paired contrasts and confidence intervals are
  withdrawn from revised claims** because the paired records were not recovered.
- Exploratory repairs have not established joint SGCls/SGDet acceptance;
  an SGCls-only pass is not a successful SGDet repair.

Use the revised repository's `README.md` and `REPRODUCIBILITY.md` for current
checks and deployment boundaries. The instructions and snapshots below are
historical; their presence is not a claim that every original result remains
validated. Distribution checks are not independent full-experiment reproduction.
No dataset images or third-party checkpoints are included in this paired archive.
The linked destinations are public, non-anonymous resources.

## Original Submission Snapshot

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
