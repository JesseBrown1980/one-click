# Rainbow81 synthetic mixture audit — 2026-10-14

This branch is a **non-main, public audit deposit** for the user's existing Asolaria `one-click` code. It does not replace the original index.html, alter the original WASM emitter or claim a new repository was created.

## Run

```bash
python3 experiments/rainbow81-mixture-2026-10-14.py
```

### Results observed on local CPU (Python 3.13.5 / Node 22.16.0)

- Original WASM rerun: **81/81 modules, 81 independent linear memories, 27/27 zero-sum cells, global arm sum 0**.
- Constructed four-feature addresses: **81 unique addresses**.
- Newly measured: **15,876** single-feature noise trials pass, **32,400** seeded joint-feature noise trials pass, **648** ±25 uncertainty-boundary cases are rejected.
- Across 3,240 unordered distinct synthetic spectral pairs: **272 normalized 50/50 mixtures exactly alias a third valid address across all 401 sampled wavelengths**. **2,968** others are rejected. The 272 aliases cover **65** third-seat addresses.
- Example: spectral profiles for seats 0 and 80, combined with equal normalized weights, are exactly seat 40's profile.

## Interpretation

This constructed address system uniquely identifies individual signatures, but not every equal-weight blend. The zero-trit neutral signature at seat 40 is a *seat*, **not** the separate uncoloured Brown-Hilbert free centre. This is a synthetic algebra/decoder test, not measured physical spectra, gravitational dynamics or quantum hardware.

Source package: the uploaded `asolaria-wasm81-hf-model-ready-2026-10-14.zip`, prepared against `JesseBrown1980/one-click` blob `72b7c6d53949fa0f4b819e801199a0faa7361390`. This branch adds a small standalone reproduction of the new negative control. The user's Hugging Face model repository `Jessedbrown/asolaria-wasm81-rainbow-audit` exists but has not been written through ChatGPT.

## Verification

The original ZIP integrity checks passed (54 source files). The exact fuller Python test and results are in the downloadable new experiments archive supplied in the current ChatGPT conversation. The committed reproduction uses the same deterministic law and assertions; independent third-party execution remains welcome.
