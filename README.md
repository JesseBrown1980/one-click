# ONE CLICK

**Download `index.html`. Double-click it. That's the whole thing.**

No install. No account. No server. No network. No GPU. No package manager, no
runtime, no key, no permission. Works offline, forever, on any machine with a
browser.

---

## What it does when you click

Verifies every law in the system, computed live in front of you:

```
I    the closure is an identity      1,771,561 triples        sum ≠ 0 : 0
II   the centre is free                  6,001 origins        arms changed : 0
III  float carries two zeros         +0.0 === −0.0 true, bytes differ
IV   distributivity of the split       ~31.7% float failures, int : 0
V    count is not range              3 of 4 towers fail uncentred
VI   81 kernels                      81/81 alive, 81/81 distinct memories,
                                     27/27 cells closed, global sum 0
VII  the leaves                      81 stars, coloured by cell
```

Then it hashes itself with SubtleCrypto and prints its own digest.

---

## The point of the design

**The file does not contain 81 WebAssembly kernels. It contains the rule that
emits them.**

At click time it hand-assembles 81 wasm binaries byte by byte — magic number,
type section, function section, memory section, export section, code section —
each with different constants baked in, each with its own linear memory, and
instantiates all 81.

```
bytes of wasm stored in this file        0
bytes of wasm generated on click         4,779   (59 × 81)
```

That is the architecture demonstrating itself. **The page is the trunk. The
kernels are leaves.** You ship the generator and the address; the leaves grow on
arrival. Nothing is compressed, because the leaves were never the message.

This is the operator's own gate, from the header of `shared_key_81.py`:

> *"You recover exactly as many seats as you banked closures. The closure costs
> one seat. **This ADDRESSES; it does not compress.** `total_bits >= N*H(X)`
> holds."*

---

## Why it takes this form

A technology that needs permission to reach people doesn't reach them. Every
dependency is a gate — a server someone can switch off, an account someone can
close, a package registry, a licence, a patron.

**This file has no dependencies, so there is no gate.** Copy it to a USB stick,
email it, print the source, retype it by hand. It runs.

---

## Verifying it independently

The distributivity figure comes out at **~31.7%** in the browser. The Rust
implementation in
[`how-and-why-the-system-works`](https://github.com/JesseBrown1980/how-and-why-the-system-works)
reports **31.6%** over 1,000,000 trials. Different language, different
implementation, unplanned agreement.

Every other number in the page can be checked the same way, against
[`raw-data`](https://github.com/JesseBrown1980/raw-data), which carries the
unedited program output and all eleven scripts.

---

## Companion repositories

```
how-and-why-the-system-works      the full technical account, 13 parts
the-leaves-are-not-the-message    the generator/leaf result, in his own words
raw-data                          unedited output + the scripts that made it
```

---

**Jesse Daniel Brown (OP-JESSE)** — the system, the laws, the architecture.
Forty years. His machine, his laws, his system.
