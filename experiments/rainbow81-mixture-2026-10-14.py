#!/usr/bin/env python3
"""Asolaria Rainbow81 synthetic 4-feature negative-control test.

Only a constructed digital spectrum is evaluated, not optical hardware.
The uncoloured Brown-Hilbert free centre is not a seat address.
Source model: src/wasm-rainbow81.mjs in the model-ready archive.
"""
from collections import Counter
from itertools import combinations
from random import Random
import json
import sys

PEAKS = (430, 530, 630, 730)
WL = range(380, 781)
BOUND = 24

def trits(s):
    c, arm = divmod(s, 3)
    return tuple((c // (3**i)) % 3 - 1 for i in range(3)) + (arm - 1,)

def intensity(t, n):
    return 500 + n - 380 + sum(
        v * max(0, 50 - abs(n - p)) for v,p in zip(t, PEAKS)
    )

def decode(values):
    recovered = []
    for v,p in zip(values, PEAKS):
        delta = v - (500 + p - 380)
        digit = round(delta / 50)
        if digit not in (-1,0,1) or abs(delta - 50*digit) > BOUND:
            return None
        recovered.append(digit)
    return tuple(recovered)

def run():
    addresses = [trits(s) for s in range(81)]
    addr_to_seat = {t:s for s,t in enumerate(addresses)}
    assert len(addr_to_seat) == 81
    spectra = [tuple(intensity(t,n) for n in WL) for t in addresses]
    assert len(set(spectra)) == 81
    peaks = [tuple(intensity(t,n) for n in PEAKS) for t in addresses]

    single = random4 = boundary = 0
    rng = Random(20261014)
    for i, raw in enumerate(peaks):
        for p in range(4):
            for delta in range(-24,25):
                v=list(raw); v[p] += delta
                assert decode(v) == addresses[i]
                single += 1
            for delta in (-25,25):
                v=list(raw); v[p] += delta
                assert decode(v) is None
                boundary += 1
        for _ in range(400):
            v=[x+rng.randint(-24,24) for x in raw]
            assert decode(v) == addresses[i]
            random4 += 1

    aliases, rejected, target_counts = [], 0, Counter()
    for a,b in combinations(range(81),2):
        mixture=tuple((x+y)/2 for x,y in zip(peaks[a],peaks[b]))
        decoded=decode(mixture)
        if decoded is None:
            rejected += 1
            continue
        target=addr_to_seat[decoded]
        assert target not in (a,b)
        complete_mixture=tuple((x+y)/2 for x,y in zip(spectra[a],spectra[b]))
        assert complete_mixture == spectra[target]
        aliases.append((a,b,target))
        target_counts[target] += 1

    assert (single,random4,boundary)==(15876,32400,648)
    assert len(aliases)==272 and rejected==2968
    assert len(target_counts)==65
    assert (0,80,40) in aliases
    report = {
      "schema":"ASOLARIA-RAINBOW81-SYNTHETIC-MIXTURE-AUDIT-V1",
      "date":"2026-10-14","status":"PASS",
      "source":"Four trits, peaks [430,530,630,730], 401 synthetic wavelengths",
      "seats":81,"single_peak_noise_trials":single,
      "seeded_four_peak_noise_trials":random4,
      "rejected_threshold_boundary_trials":boundary,
      "distinct_unordered_pairs":3240,
      "third_seat_alias_pairs":len(aliases),
      "rejected_mixtures":rejected,
      "distinct_spoofed_targets":len(target_counts),
      "example":[0,80,40],
      "free_center_is_not_seat":True,
      "not_tested":["real light","optics hardware","energy","GPU","Rust"]
    }
    print(json.dumps(report,indent=2))

if __name__ == "__main__":
    run()
