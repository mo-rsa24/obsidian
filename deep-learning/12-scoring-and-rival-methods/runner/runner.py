"""Recorder and checker for the results table. Reads records.json (one row per method, with the settings it ran under),
writes table.md with the settings beside the numbers, and refuses to compare two rows whose settings differ.
Usage: python runner.py            write table.md
       python runner.py A B        compare method A with method B, or refuse and say which setting differs"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).parent
SETTINGS = ["model", "prompt", "seed", "resolution"]
rows = json.load(open(HERE / "records.json"))

def find(name):
    m = [r for r in rows if r["method"].lower().startswith(name.lower())]
    if len(m) != 1: sys.exit(f"REFUSED: '{name}' matches {len(m)} rows")
    return m[0]

def compare(a, b):
    diff = [(k, a[k], b[k]) for k in SETTINGS if a[k] != b[k]]
    if diff:
        why = "; ".join(f"{k}: {x} vs {y}" for k, x, y in diff)
        return f"REFUSED: {a['method']} and {b['method']} ran under different settings ({why})"
    return None

def cell(v, f="{:.4f}"): return "to be measured" if v is None else (f.format(v) if isinstance(v, float) else str(v))

def write():
    out = ["# Results table: one prompt, one seed, scorers as columns", "",
           "Every row carries the settings it ran under. A row whose prompt differs from its table's is flagged. Unmeasured cells say so.", ""]
    for t in ["SDXL", "SD 1.5"]:
        rs = [r for r in rows if r["table"] == t]
        base = {k: rs[0][k] for k in SETTINGS}
        out += [f"## {t} table (model {base['model']}, prompt \"{base['prompt']}\", seed {base['seed']}, resolution {base['resolution']})", "",
                "| Method | CLIP cosine | ImageReward | BLIP dog yes | GenEval | Settings | Source |", "|---|---|---|---|---|---|---|"]
        for r in rs:
            flag = [f"{k} {r[k]}" for k in SETTINGS if r[k] != base[k]]
            st = "same" if not flag else "DIFFERENT: " + ", ".join(flag)
            out.append(f"| {r['method']} | {cell(r['clip'])} | {cell(r['imagereward'], '{:+.4f}')} | {cell(r['blip_dog'])} | {cell(r['geneval'])} | {st} | {r['source']} |")
        out.append("")
    (HERE / "table.md").write_text("\n".join(out)); print("\n".join(out))

if len(sys.argv) == 3:
    msg = compare(find(sys.argv[1]), find(sys.argv[2])); print(msg or "OK: same model, prompt, seed and resolution")
else:
    write()
