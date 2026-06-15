# Cash Transfers & School Attendance (Kenya)

**Status**: Active
**Stage**: Analysis
**Last Updated**: 2026-06-12
**Owner**: A. Researcher

> ⓘ This is a **fictional sample** created for the Thinking with Agents webinar (June 2026).
> Names, paths, and results are made up. It shows the *shape* of a project HUB, not a real study.

---

## Quick Summary

A clustered RCT in 120 primary schools testing whether unconditional cash transfers to
households raise daughters' school attendance. Deliverable: a working paper + replication package
by Fall 2026. We are mid-analysis on the midline data.

---

## Where Everything Lives

| Resource | Service | Path / Link |
|----------|---------|-------------|
| **Raw data** | Box | `Box/CashTransfers_KE/01_raw/` |
| **Working data** | Box | `Box/CashTransfers_KE/02_working/` |
| **Output (tables/figures)** | Box | `Box/CashTransfers_KE/03_output/` |
| **Code** | GitHub | `github.com/aresearcher/cash-transfers-ke` |
| **Local clone** | Dropbox | `~/Dropbox/GitHub/cash-transfers-ke/` |
| **Paper draft** | Overleaf | "Cash Transfers KE — working paper" |
| **IRB** | UVM IRB | Protocol #STUDY00004821 (approved 2025-03) |
| **Pre-registration** | AEA RCT Registry | AEARCTR-00xxxxx |

---

## Team & Human Dependencies

| Person | Role | Waiting on them? | They waiting on you? | Deadline |
|--------|------|-------------------|----------------------|----------|
| A. Researcher | PI | No | — | — |
| J. Co-author | Co-PI (analysis) | Attendance recode decision | No | Jun 20 |
| Field RA (Nairobi) | Data | Cleaned endline roster | No | Jul 1 |

---

## Current State

- **What's done**: Baseline + midline cleaned; balance table built and passing; main attendance regression specified and running.
- **What's in progress**: Heterogeneity by household poverty; deciding how to handle students who transferred schools mid-year.
- **What's blocked**: Endline data not yet delivered from the field (expected ~Jul 1).

---

## Next 3 Steps

1. [ ] Resolve the transfer-student recode with J. Co-author (affects the attendance denominator). Decision needed by Jun 20.
2. [ ] Rebuild the main results table (`03_output/t2_attendance.tex`) once the recode is settled.
3. [ ] Draft the heterogeneity section of the paper from the poverty-interaction results.

---

## Key Decisions & Open Questions

- **Open**: Do students who transfer schools mid-year count as "attending"? Two defensible codings; results move ~2pp depending on choice. Need J. Co-author's call before finalizing tables.
- **Decided (2026-05-30)**: Cluster SEs at the school level (the unit of randomization), not the household.

---

## Project-Specific Config

```yaml
project_id: cash-transfers-ke
github_repo: aresearcher/cash-transfers-ke
box_path: Box/CashTransfers_KE/
primary_email: Gmail
```

---

## Notes

- The randomization is at the **school** level — always cluster SEs there. (Easy to get wrong with household-level data.)
- `01_raw/` is read-only. All cleaning writes to `02_working/`; never edit raw files in place.
- Paired with **`sample-session-log.md`** — that file holds the running session-by-session history. This HUB holds the current state; the log holds how we got here.

---

## Status Log

| Date | Update | Session |
|------|--------|---------|
| 2026-06-12 | Balance table passing; started heterogeneity by poverty | S4 |
| 2026-06-05 | Main attendance spec finalized; SE clustering decided | S3 |
| 2026-05-28 | Midline data cleaned and merged to baseline | S2 |
| 2026-05-20 | Project HUB created; file locations mapped | S1 |
