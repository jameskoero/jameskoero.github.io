# Claims ledger

Every number shown on this site, where it comes from, and how far it is checked.
"Verified" means read from the named file. "README" means stated on the public GitHub profile README and not yet re-derived from a file in this review.

## Nyando Flood AI (github.com/jameskoero/nyando-flood-ai)

| Claim | Value | Source | Status | Last checked |
|---|---|---|---|---|
| hgb:con mean per-event AUC, 27 sealed events, mappable frame | 0.971 (0.9708) | docs/D20_RESULTS.json block_a_auc.mappable | Verified | 15 Nov 2026 |
| Elevation-only, same events and frame | 0.939 (0.9385) | same | Verified | 15 Nov 2026 |
| Registered logistic champion, same events and frame | 0.950 (0.9502) | same | Verified | 15 Nov 2026 |
| Full frame: hgb:con / champion / elevation | 0.965 / 0.948 / 0.928 | computed from per-event values in D20_RESULTS.json | Verified | 15 Nov 2026 |
| hgb:con minus champion, full frame | +0.0164, interval 0.0052 to 0.0273, 19 wins, 8 losses | D20_RESULTS.json analysis.frames.full | Verified | 15 Nov 2026 |
| Champion minus elevation, full frame | +0.0207, interval -0.0005 to 0.0448, 17 wins, 10 losses | same | Verified, interval includes zero | 15 Nov 2026 |
| Champion minus elevation, mappable | +0.0117, interval -0.0107 to 0.0381, 11 wins, 16 losses | docs/D20_PROTOCOL.md R-A line | Verified, does not replicate | 15 Nov 2026 |
| Registered model minus elevation-only, pooled events | +0.0384, interval 0.0193 to 0.0611, 36 wins, 9 losses, pooled over 50 events | docs/REGISTRATION.json versus_elevation_only.pooled_mappable; README | Verified | 15 Nov 2026 |
| Dataset | 4,420 rows, 35 Sentinel-1 scene dates, Copernicus GFM labels, Google Earth Engine features, no synthetic data | README | README | 15 Nov 2026 |
| Leave-one-event-out mean per-event AUC | 0.943 on 23 events | site | Source file not yet cross-checked | 15 Nov 2026 |
| ONNX parity | 3.3e-16 | README | README | 15 Nov 2026 |
| Docker | hash-locked, 31 packages, 483 hashes | site | Source file not yet cross-checked | 15 Nov 2026 |
| Model choice | gradient boosting chosen against logistic, XGBoost and a PyTorch physics-constrained network that violated the constraints | README | README | 15 Nov 2026 |
| No advantage under 1 km buffer or out-of-time split | statement | model card, README | README | 15 Nov 2026 |
| Release | v2.0.0, DOI 10.5281/zenodo.23919053 | Zenodo | Not re-checked in this review | 15 Nov 2026 |

## Retracted figures (earlier version, not to be reused)

AUC 0.9717, F1 0.9022, cross-validation 0.9727, 2,308 rows. Retracted with a Zenodo erratum.

## Other projects

| Project | Claims | Source | Status | Last checked |
|---|---|---|---|---|
| AfriSalaries | XGBoost with TF-IDF and SHAP, 1,526 real records, 8 markets, 59.5% band accuracy, two regression designs rejected (R-squared 0.34, 0.38) | README, project notes | README | 15 Nov 2026 |
| Loan Default Risk | German Credit, test ROC-AUC 0.791, Gini 0.582, recall 0.833, threshold 0.22 from a 5:1 cost matrix | README | README | 15 Nov 2026 |
| Titanic | hold-out ROC-AUC 0.8661, bootstrap 95% intervals, DOI 10.5281/zenodo.20387973 | README | README | 15 Nov 2026 |
| SegmentIQ | K-Means, 5 segments, CSV batch upload, FastAPI and React | README | README | 15 Nov 2026 |
| ChurchOS | JWT, 5-role access control (admin, pastor, secretary, treasurer, viewer), finance audit log, M-Pesa; version 3.4.0 live; billing, offline attendance, SMS with consent, regions, encrypted backups; 192 test functions in 26 files; 21 merged pull requests; own M-Pesa and SMS sign-in ship switched off. Flutterwave removed: only a key setting exists in backend/config.py, no routes | Repository at ea168c8: backend/app.py, backend/models.py, backend/routes/, backend/tests/; live /api/health | Verified | 18 Nov 2026 |
| Kenya at Gold | 39 Olympic golds, four-dimension governance framework, code MIT, data CC-BY 4.0 | README | README | 15 Nov 2026 |

## Added 15 Nov 2026

| Claim | Source | Status | Last checked |
|---|---|---|---|
| SegmentIQ live app at kmeans-customer-segmentation.vercel.app | URL supplied by the owner; page title "SegmentIQ - Customer Segmentation" read on 15 Nov 2026 | Verified that the page loads, interface not exercised | 15 Nov 2026 |
| Roles, employers, titles and dates on /experience/ | Owner's own account of his career | Owner stated, no documents checked here | 15 Nov 2026 |
| Best Unit Manager countrywide, October 2017 | Owner's own account | Owner stated | 15 Nov 2026 |
| Education, certifications and the B.Sc. research project title | Owner's own account | Owner stated | 15 Nov 2026 |
| Nyando: selected neural network violated the monotonic constraints and was not promoted | Project notes, README | README | 15 Nov 2026 |
| Nyando: early-warning (temporal) skill not demonstrated; 26 further events held sealed | Project notes | Project notes | 15 Nov 2026 |
| Skill levels (Proficient, Working knowledge, Currently developing) | Proposed from project evidence | Owner may adjust | 15 Nov 2026 |
| Role line "Machine Learning Engineer" | Default adopted 15 Nov 2026 | Owner may change | 15 Nov 2026 |

## Status statements

Sokoni: backend scaffolded, agent logic not built. Retrieval-augmented generation and fine-tuning: learning, nothing shipped.

## Rule

If a number is not in this table, it does not go on the site, the CV or a profile.

## Added 16 Nov 2026

| Claim | Value | Source | Status | Last checked |
|---|---|---|---|---|
| LLM advisory layer | POST /v2/advisory: Gemini, then Groq, then a template; ten named guard rules; providers write only summary and meaning; /v2/score never calls a provider; live-checked 29 Oct 2026 | project record | Recorded, re-read before publishing | 16 Nov 2026 |
| Data licence | V2 data files ODbL 1.0; ward polygons CC BY 4.0; code MIT; legacy v1 files not covered | PR #108, deviation D37 closed | Recorded | 16 Nov 2026 |
| Financial services experience | more than seven years in sales and sales management | author statement | Not documented by a file | 16 Nov 2026 |
| LangGraph level | working knowledge, nothing shipped | author statement | Author statement | 16 Nov 2026 |
| Manuscript | in preparation, not submitted or published | author statement | Author statement | 16 Nov 2026 |
| Next steps for AfriSalaries and SegmentIQ | drafted by Claude, per-band confusion matrix and baseline; cluster-quality measure | draft | Awaiting author approval | 16 Nov 2026 |
| Next steps for Nyando Flood AI and ChurchOS | temporal-skill test, 26 sealed events, legacy endpoint retirement; billing, SMS, offline attendance | project record and README | Recorded | 16 Nov 2026 |
| Archive status | Loan Default Risk and Titanic Survival: completed. Kenya at Gold: no label yet | author | Kenya at Gold pending | 16 Nov 2026 |
| Archive projects (Pack 14) | Loan: deployed, CV ROC-AUC 0.916 (README). Titanic: hold-out ROC-AUC 0.8661, live demo (README). Kenya at Gold: in progress (README status list), live dashboard not verified, stack not stated | project READMEs | README | 16 Nov 2026 |

## Added 18 Nov 2026 (Part B pages)

All figures read from github.com/jameskoero/nyando-flood-ai at commit 0c63e78.

| Claim | Source | Status | Last checked |
|---|---|---|---|
| Physics-constrained MLP vs hgb:con, mappable: -0.0098 [-0.0204, -0.0005], 4 wins, 13 losses, 6 ties, 23 events; vs elevation +0.0358 [+0.0046, +0.0721]; means 0.943, 0.937, 0.933, 0.897 | docs/PHASE_D_RESULTS.json (stats.mappable, mean_micro.mappable) | Verified | 18 Nov 2026 |
| MLP violations of 200 rows: rainfall 79, elevation 148, distance 80, slope 198; penalty-0 control 125, 136, 160, 197; hgb:con 0 | docs/PHASE_D_RESULTS.json (violations); docs/PHASE_D_PROTOCOL.md Section 11 | Verified | 18 Nov 2026 |
| X3 set in Stage 0; r4 added after the violation check; 14 inputs, tanh, Adam, 100 epochs, seed 42, CPU | docs/PHASE_D_PROTOCOL.md lines 16-22, 47, 85-87 | Verified | 18 Nov 2026 |
| ONNX parity 3.3e-16 Block A, 2.5e-16 training; AUC difference 0; zero violations; 100 trees, 1,013 nodes, 1,113 leaves; skl2onnx difference up to 0.981 | docs/REGISTRATION.json; docs/ROADMAP_DEVIATIONS.md row D42 | Verified | 18 Nov 2026 |
| All Nyando intervals are 97.5% paired per-event bootstrap intervals (10,000 resamples); research and Nyando pages corrected from "95%" | docs/PROMOTION_PROTOCOL.md line 15; docs/PHASE_D_PROTOCOL.md line 28; docs/REGISTRATION.json | Corrected | 18 Nov 2026 |
| Logistic champion vs elevation on 27 sealed events, mappable: +0.0117 [-0.0107, +0.0381], 11 wins, 16 losses | docs/D20_RESULTS.json | Verified | 18 Nov 2026 |
| Phase L: land cover adds no within-class discrimination on Block A; observed clay adds discrimination | docs/PHASE_L_RESULTS.json (claims.d14, claims.d55) | Verified | 18 Nov 2026 |
| Retraction: 0.9717 / 0.9022 / 0.9727; 2 flood rows of 2,308; SMOTE before split; erratum on both records 2026-11-03; bare 4-feature logistic 0.841 | nyando-flood-ai README.md lines 10, 72, 208 | Verified | 18 Nov 2026 |
| Certificates: Google Developers Launchpad Certificate of Excellence (2023, Excellent); Programiz Python Basic | Existing Experience page and CV | Carried over, not re-verified | 18 Nov 2026 |
