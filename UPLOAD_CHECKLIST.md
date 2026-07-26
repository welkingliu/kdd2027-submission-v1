# KDD Upload Checklist

## Submission Policy

The KDD 2027 Datasets & Benchmarks Track is **single-blind**. A normal public
GitHub repository is appropriate; an anonymous GitHub account or anonymous
repository is not required. The paper must list authors and affiliations.

Official track page:
`https://kdd2027.kdd.org/datasets-and-benchmarks-track-call-for-papers/`

## Before Paper Submission

- [ ] Change `\documentclass[sigconf,review,anonymous]{acmart}` to
  `\documentclass[sigconf,review]{acmart}`.
- [ ] Restore the complete author, affiliation, and contact block.
- [ ] Confirm that the main paper contains no more than eight content pages,
  excluding references and the optional appendix.
- [ ] Correct `Oject-Head Calibration` to `Object-Head Calibration` in the
  overview artwork and replace the PDF without changing its filename.
- [ ] Compile the final PDF and inspect every table/figure at 100% zoom.
- [ ] Confirm that all first-eight-page claims are self-contained.

## GitHub / Archival Release

- [ ] Upload the contents of the update ZIP to a normal repository.
- [ ] Keep the repository public or provide reviewer-accessible archival
  supplementary material according to the submission form.
- [ ] Create a tagged release such as `kdd2027-submission-v1`.
- [ ] Archive the tagged release with Zenodo or another immutable service and
  add the DOI to the camera-ready artifact statement when available.
- [ ] Retain `LICENSE`, `README.md`, `REPRODUCIBILITY.md`,
  `THIRD_PARTY_ASSETS.md`, and `MANIFEST.sha256`.
- [ ] Enable issue reporting so failed setup steps can be documented.

## Include

- [ ] Benchmark source under `sgg_core/`.
- [ ] All canonical launchers and setup scripts under `scripts/`.
- [ ] Configuration files and manifest schemas.
- [ ] Unit tests and smoke command.
- [ ] Paper source, bibliography, exact final overview, and generated result
  figures.
- [ ] Sanitized aggregate JSON used by every paper table.
- [ ] Six small Experiment V calibration states and their hashes.
- [ ] Environment requirements and pinned upstream commits.
- [ ] A clear expected runtime/storage table if rerun measurements are
  available on the final hardware.

## Exclude

- [ ] Raw VG, OI, PSG, GQA, and VRD data.
- [ ] Original third-party checkpoints and prediction caches.
- [ ] External repository copies; provide pinned acquisition scripts instead.
- [ ] Passwords, private IP addresses, shell history, home-directory paths, and
  machine-specific manifests.
- [ ] Smoke, failed, partial, and superseded runs from reported-result folders.
- [ ] LaTeX auxiliary files and old overview versions.

## Final Verification

```bash
bash scripts/reproduce_paper.sh smoke
python scripts/build_release_bundle.py --verify-only dist/GroundedSGG-Bench_update_20260727.zip
```

The release is ready only if source compilation, unit tests, shell syntax,
forbidden-path scanning, archive checksums, and a clean extraction smoke test
all pass.
