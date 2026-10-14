# Asolaria 81-cell hash-change dependency experiment — 2026-10-14

**Result:** Nine independently reset mutation waves changed all **81/81 constructed cell records** and all **171/171 chained ring commitments** after the shared source HBP checksum was changed and all derived records were explicitly recomputed. Each of the five named commitment fields (`HBI,HBP,SHA,SH,HASH`) changed for every cell in each wave: **405 changed fields per wave**.

**Negative control:** Tampering with one stored derived commitment, without propagating/recomputing dependencies, changes only that one cell and leaves the other **80 stored cells unchanged**. The aggregate commitment changes if and when recalculated.

This is reproducible with:

```bash
python experiments/hash-cascade-81-2026-10-14.py
```

Provenance: scoped reproduction of the **length-prefixed SHA-256 domain_hash**, `FLOWE_ID`, and `CELL_COMMITMENT` shared-source dependency in `JesseBrown1980/FOLLOW-THE-IS-NOT-THE-WILL-AND-WAS/matrix/build_timed_86400_flowes_x3x3.py` (blob `a38ffd2f5b00d2b0008c5be4265f173a1e2e926c`). The full original builder contains **31,824 cells**, not 81. This runnable reproduction is a smaller fixture and its simplified HBP and ring observations are **not an exact full-source replay**.

The separately run local expanded fixture, which includes the original ring observation formulas, gave nine global object-root Hamming distances **[127,131,142,143,134,137,127,129,131] bits out of 256**. Results are not observations of real light, energy, quantum behavior, gravitation or physical signal propagation. The 19 checkpoint values are deterministic labels, not measured transit delays; no claim of faster-than-light influence follows.

**Next test:** authentic full-builder checksum re-sealing, followed by an instrumentation test on two separately clocked and physically distant hosts if a real signal-speed claim is intended.

The Brown-Hilbert free centre is separate from these 81 cell records. All changes were committed to this isolated audit branch, not `main`.
