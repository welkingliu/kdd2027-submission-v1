# Generated PySGG Configurations

The formal PySGG YAML files contain machine-local dataset, checkpoint, output,
and runtime paths. Generate them after cloning the release:

```bash
source scripts/project_env.sh
"$SGG_PYTHON" scripts/generate_pysgg_vg_tritask_configs.py \
  --project_root "$SGG_PROJECT_ROOT"
```

Generated files are written to `configs/pysgg_vg_tritask/` and are deliberately
excluded from the release archive. Their hyperparameters are fixed by the
generator and the paper-specific launchers.
