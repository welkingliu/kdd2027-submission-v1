# Official Factory Contract

The object returned by a manifest factory must implement:

- `parameters`, `eval`, and `to`;
- `predict_scene_graph(batch, task)`;
- `predict(batch)` returning `pred_rel_scores`;
- `extract_node_features(batch)`;
- `diagnostic_input_fingerprint(batch)`.

The fingerprint must be computed after adapter preprocessing from the exact
visual inputs consumed by `predict`. A typical implementation is:

```python
from sgg_core.models.official_adapter import fingerprint_tensors

def diagnostic_input_fingerprint(self, batch):
    prepared = self.prepare_diagnostic_inputs(batch)
    return fingerprint_tensors(
        roi=prepared.roi_features,
        union=prepared.union_features,
        boxes=prepared.boxes,
    )
```

Calling `prepare_diagnostic_inputs` in both `predict` and the fingerprint method
is required. Hashing raw batch keys that the official model does not consume is
not a valid implementation.

Prediction-cache factories are restricted to Experiment-IV standard metrics.
They must declare `execution_mode=prediction_cache` and every perturbation and
mitigation flag as false.

For Experiment V, a live factory must additionally implement:

- `grounding_parameters()` returning the exact trainable object/relation subset;
- `forward_grounding(batch)` returning `pred_rel_scores` aligned one-to-one
  with `batch['rel_labels']` and `pred_entity_scores` aligned one-to-one with
  `batch['entity_labels']`;
- optional `mask_entity_scores`, with the same shape as
  `pred_entity_scores`, for box/mask consistency.

The manifest must declare `relation_logit_alignment=gt_relations` and
`object_logit_alignment=gt_entities`. Runtime shape checks remain mandatory.
