# Claims ledger

Every number shown on this site, where it comes from, and how far it is checked.
Source repo: github.com/jameskoero/nyando-flood-ai. "Verified" means read from the named file in this review.

## Nyando Flood AI

| Claim | Value | Source | Status |
|---|---|---|---|
| hgb:con mean per-event AUC, 27 sealed events, mappable frame | 0.971 (0.9708) | docs/D20_RESULTS.json block_a_auc.mappable | Verified |
| Elevation-only, same events and frame | 0.939 (0.9385) | same | Verified |
| Registered logistic champion, same events and frame | 0.950 (0.9502) | same | Verified |
| Full frame: hgb:con / champion / elevation | 0.965 / 0.948 / 0.928 | computed from per-event values in D20_RESULTS.json | Verified (means checked against file differences) |
| hgb:con minus champion, full frame | +0.0164, interval 0.0052 to 0.0273, 19 wins, 8 losses | D20_RESULTS.json analysis.frames.full | Verified |
| Champion minus elevation, full frame | +0.0207, interval -0.0005 to 0.0448, 17 wins, 10 losses | same | Verified, interval includes zero |
| Champion minus elevation, mappable | +0.0117, interval -0.0107 to 0.0381, 11 wins, 16 losses | docs/D20_PROTOCOL.md R-A line | Verified, does not replicate |
| Registered model minus elevation-only, pooled mappable events | +0.0384, interval 0.0193 to 0.0611, 36 wins, 9 losses | docs/REGISTRATION.json versus_elevation_only.pooled_mappable | Verified |
| Leave-one-event-out mean per-event AUC | 0.943 on 23 events | stated on site | Source file not yet cross-checked |
| Dataset size | 4,420 rows, 35 Sentinel-1 scene dates, 5 wards | stated on site | Source file not yet cross-checked |
| Hash-locked Docker | 31 packages, 483 hashes | stated on site | Source file not yet cross-checked |
| Release | v2.0.0, DOI 10.5281/zenodo.23919053 | Zenodo | Not re-checked in this review |
| No advantage under 1 km buffer or out-of-time split | statement | docs/REGISTRATION.json versus_previous_model, site text | Partly checked |

## Retracted figures (earlier version, not to be reused)

AUC 0.9717, F1 0.9022, cross-validation 0.9727, 2,308 rows. Retracted with a Zenodo erratum.

## Other projects (from project notes, to cross-check against each repo)

AfriSalaries: XGBoost, 1,526 records, 8 countries, 59.5% band accuracy.
Loan Risk: test ROC-AUC 0.791, Gini 0.582, threshold 0.22.
Titanic: hold-out ROC-AUC 0.8661, DOI 10.5281/zenodo.20387973.

## Rule

If a number is not in this table, it does not go on the site, the CV or a profile.
