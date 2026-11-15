# Claims ledger

Every number shown on this site, where it comes from, and how far it is checked.
"Verified" means read from the named file. "README" means stated on the public GitHub profile README and not yet re-derived from a file in this review.

## Nyando Flood AI (github.com/jameskoero/nyando-flood-ai)

| Claim | Value | Source | Status |
|---|---|---|---|
| hgb:con mean per-event AUC, 27 sealed events, mappable frame | 0.971 (0.9708) | docs/D20_RESULTS.json block_a_auc.mappable | Verified |
| Elevation-only, same events and frame | 0.939 (0.9385) | same | Verified |
| Registered logistic champion, same events and frame | 0.950 (0.9502) | same | Verified |
| Full frame: hgb:con / champion / elevation | 0.965 / 0.948 / 0.928 | computed from per-event values in D20_RESULTS.json | Verified |
| hgb:con minus champion, full frame | +0.0164, interval 0.0052 to 0.0273, 19 wins, 8 losses | D20_RESULTS.json analysis.frames.full | Verified |
| Champion minus elevation, full frame | +0.0207, interval -0.0005 to 0.0448, 17 wins, 10 losses | same | Verified, interval includes zero |
| Champion minus elevation, mappable | +0.0117, interval -0.0107 to 0.0381, 11 wins, 16 losses | docs/D20_PROTOCOL.md R-A line | Verified, does not replicate |
| Registered model minus elevation-only, pooled events | +0.0384, interval 0.0193 to 0.0611, 36 wins, 9 losses, pooled over 50 events | docs/REGISTRATION.json versus_elevation_only.pooled_mappable; README | Verified |
| Dataset | 4,420 rows, 35 Sentinel-1 scene dates, Copernicus GFM labels, Google Earth Engine features, no synthetic data | README | README |
| Leave-one-event-out mean per-event AUC | 0.943 on 23 events | site | Source file not yet cross-checked |
| ONNX parity | 3.3e-16 | README | README |
| Docker | hash-locked, 31 packages, 483 hashes | site | Source file not yet cross-checked |
| Model choice | gradient boosting chosen against logistic, XGBoost and a PyTorch physics-constrained network that violated the constraints | README | README |
| No advantage under 1 km buffer or out-of-time split | statement | model card, README | README |
| Release | v2.0.0, DOI 10.5281/zenodo.23919053 | Zenodo | Not re-checked in this review |

## Retracted figures (earlier version, not to be reused)

AUC 0.9717, F1 0.9022, cross-validation 0.9727, 2,308 rows. Retracted with a Zenodo erratum.

## Other projects

| Project | Claims | Source | Status |
|---|---|---|---|
| AfriSalaries | XGBoost with TF-IDF and SHAP, 1,526 real records, 8 markets, 59.5% band accuracy, two regression designs rejected (R-squared 0.34, 0.38) | README, project notes | README |
| Loan Default Risk | German Credit, test ROC-AUC 0.791, Gini 0.582, recall 0.833, threshold 0.22 from a 5:1 cost matrix | README | README |
| Titanic | hold-out ROC-AUC 0.8661, bootstrap 95% intervals, DOI 10.5281/zenodo.20387973 | README | README |
| SegmentIQ | K-Means, 5 segments, CSV batch upload, FastAPI and React | README | README |
| ChurchOS | JWT, 5-role access control, finance audit log, M-Pesa and Flutterwave, Phase 1 live | README | README |
| Kenya at Gold | 39 Olympic golds, four-dimension governance framework, code MIT, data CC-BY 4.0 | README | README |

## Added 15 Nov 2026

| Claim | Source | Status |
|---|---|---|
| SegmentIQ live app at kmeans-customer-segmentation.vercel.app | URL supplied by the owner; page title "SegmentIQ - Customer Segmentation" read on 15 Nov 2026 | Verified that the page loads, interface not exercised |
| Roles, employers, titles and dates on /experience/ | Owner's own account of his career | Owner stated, no documents checked here |
| Best Unit Manager countrywide, October 2017 | Owner's own account | Owner stated |
| Education, certifications and the B.Sc. research project title | Owner's own account | Owner stated |
| Nyando: selected neural network violated the monotonic constraints and was not promoted | Project notes, README | README |
| Nyando: early-warning (temporal) skill not demonstrated; 26 further events held sealed | Project notes | Project notes |
| Skill levels (Proficient, Working knowledge, Currently developing) | Proposed from project evidence | Owner may adjust |
| Role line "Machine Learning Engineer" | Default adopted 15 Nov 2026 | Owner may change |

## Status statements

Sokoni: backend scaffolded, agent logic not built. Retrieval-augmented generation and fine-tuning: learning, nothing shipped.

## Rule

If a number is not in this table, it does not go on the site, the CV or a profile.
