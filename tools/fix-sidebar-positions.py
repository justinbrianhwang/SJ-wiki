"""Rewrite _category_.json positions so hub index.md (position 0) stays on top.

Sidebars autogenerate from sidebar_position (for files) and position (for
_category_.json). When a hub index.md is at 0 and a subtopic _category_.json is
also at 0, ties resolve alphabetically and the hub drops below the subtopic.
This script bumps subtopic positions to start at 1+, preserving a sensible order
per subject.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs"

orderings = {
    "math": [
        "calculus",
        "linear-algebra",
        "engineering-math",
        "statistics",
        "probability",
        "discrete",
        "numerical-analysis",
        "graph-theory",
    ],
    "cs": [
        "programming",
        "algorithms",
        "data-structures",
        "theory",
        "operating-systems",
        "databases",
        "computer-architecture",
        "embedded",
        "data-mining",
        "nlp",
        "cryptography",
        "software-engineering",
    ],
    "physics": [
        "general",
        "mechanics",
        "signals-systems",
        "quantum-mechanics",
        "quantum-field-theory",
        "simulation",
    ],
    "chemistry": [
        "general",
    ],
}


def main() -> None:
    for subject, order in orderings.items():
        for idx, sub in enumerate(order, start=1):
            cat_path = ROOT / subject / sub / "_category_.json"
            if not cat_path.exists():
                print(f"  missing: {cat_path}")
                continue
            data = json.loads(cat_path.read_text(encoding="utf-8"))
            old_pos = data.get("position")
            if old_pos == idx:
                continue
            data["position"] = idx
            cat_path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            print(f"  {subject}/{sub}: {old_pos} -> {idx}")


if __name__ == "__main__":
    main()
