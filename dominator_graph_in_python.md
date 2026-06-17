# Dominator Graph for Compiler Optimization in Python

## Core Concept

Node **A dominates** node **B** if every path from the entry node to B passes through A.
The **dominator tree** encodes these relationships compactly — each node's parent is its immediate dominator.

Used in: loop detection, SSA construction, code motion optimizations.

---

## Step 1: Represent the CFG

```python
# Adjacency list: node -> set of successors
cfg = {0: {1, 2}, 1: {3}, 2: {3}, 3: {4}}

# Also build predecessor map
from collections import defaultdict

def build_preds(cfg):
    preds = defaultdict(set)
    for node, succs in cfg.items():
        for s in succs:
            preds[s].add(node)
    return preds
```

---

## Step 2: Choose Your Algorithm

| Algorithm              | Complexity     | When to use                              |
|------------------------|----------------|------------------------------------------|
| Naive dataflow         | O(n²) worst    | Simple to implement, fine for small CFGs |
| Cooper et al. (2001)   | O(n²) typical  | Sweet spot — ~30 lines, production-ready |
| Lengauer-Tarjan        | O(n α(n))      | Large CFGs, maximum performance          |

**Cooper's "Simple, Fast Dominance Algorithm"** is the recommended starting point.

---

## Step 3: Compute Reverse Postorder (RPO)

RPO is critical — it ensures the dataflow converges quickly.

```python
def reverse_postorder(cfg, entry):
    visited = set()
    postorder = []

    def dfs(node):
        visited.add(node)
        for succ in cfg.get(node, []):
            if succ not in visited:
                dfs(succ)
        postorder.append(node)

    dfs(entry)
    return list(reversed(postorder))
```

---

## Step 4: Cooper's Dominator Algorithm

```python
def intersect(doms, rank, b1, b2):
    # Walk up the partial dominator tree to find common ancestor
    while b1 != b2:
        while rank[b1] > rank[b2]:
            b1 = doms[b1]
        while rank[b2] > rank[b1]:
            b2 = doms[b2]
    return b1

def build_dominators(cfg, entry, preds):
    rpo = reverse_postorder(cfg, entry)
    rank = {n: i for i, n in enumerate(rpo)}

    doms = {entry: entry}
    changed = True

    while changed:
        changed = False
        for b in rpo:
            if b == entry:
                continue
            processed_preds = [p for p in preds[b] if p in doms]
            if not processed_preds:
                continue
            new_idom = processed_preds[0]
            for p in processed_preds[1:]:
                new_idom = intersect(doms, rank, new_idom, p)
            if doms.get(b) != new_idom:
                doms[b] = new_idom
                changed = True

    return doms  # maps node -> immediate dominator
```

---

## Step 5: Build the Dominator Tree

```python
def build_dom_tree(doms, entry):
    dom_tree = defaultdict(set)
    for node, idom in doms.items():
        if node != entry:
            dom_tree[idom].add(node)
    return dom_tree
```

---

## Step 6: Dominance Frontier (for SSA Construction)

The dominance frontier of node X is the set of nodes where X's dominance ends —
these are exactly where φ-functions (phi nodes) must be placed in SSA form.

```python
def build_dominance_frontier(cfg, preds, doms):
    df = defaultdict(set)
    for b in cfg:
        if len(preds[b]) >= 2:
            for p in preds[b]:
                runner = p
                while runner != doms[b]:
                    df[runner].add(b)
                    runner = doms[runner]
    return df
```

---

## Full Example

```python
from collections import defaultdict

cfg = {0: {1, 2}, 1: {3}, 2: {3}, 3: {4}, 4: set()}
entry = 0

preds = build_preds(cfg)
doms = build_dominators(cfg, entry, preds)
dom_tree = build_dom_tree(doms, entry)
df = build_dominance_frontier(cfg, preds, doms)

print("Immediate dominators:", doms)
print("Dominator tree:", dict(dom_tree))
print("Dominance frontiers:", dict(df))
```

---

## Runnable Script

Save as `dominator.py` and run with `python dominator.py`.

```python
from collections import defaultdict


def build_preds(cfg):
    preds = defaultdict(set)
    for node, succs in cfg.items():
        for s in succs:
            preds[s].add(node)
    return preds


def reverse_postorder(cfg, entry):
    visited = set()
    postorder = []

    def dfs(node):
        visited.add(node)
        for succ in sorted(cfg.get(node, [])):  # sorted for determinism
            if succ not in visited:
                dfs(succ)
        postorder.append(node)

    dfs(entry)
    return list(reversed(postorder))


def intersect(doms, rank, b1, b2):
    while b1 != b2:
        while rank[b1] > rank[b2]:
            b1 = doms[b1]
        while rank[b2] > rank[b1]:
            b2 = doms[b2]
    return b1


def build_dominators(cfg, entry, preds):
    rpo = reverse_postorder(cfg, entry)
    rank = {n: i for i, n in enumerate(rpo)}

    doms = {entry: entry}
    changed = True

    while changed:
        changed = False
        for b in rpo:
            if b == entry:
                continue
            processed_preds = [p for p in preds[b] if p in doms]
            if not processed_preds:
                continue
            new_idom = processed_preds[0]
            for p in processed_preds[1:]:
                new_idom = intersect(doms, rank, new_idom, p)
            if doms.get(b) != new_idom:
                doms[b] = new_idom
                changed = True

    return doms


def build_dom_tree(doms, entry):
    dom_tree = defaultdict(set)
    for node, idom in doms.items():
        if node != entry:
            dom_tree[idom].add(node)
    return dom_tree


def build_dominance_frontier(cfg, preds, doms):
    df = defaultdict(set)
    for b in cfg:
        if len(preds[b]) >= 2:
            for p in preds[b]:
                runner = p
                while runner != doms[b]:
                    df[runner].add(b)
                    runner = doms[runner]
    return df


def print_dom_tree(dom_tree, node, doms, entry, indent=0):
    label = f"{node} (idom: {doms[node]})" if node != entry else f"{node} (entry)"
    print("  " * indent + f"[{label}]")
    for child in sorted(dom_tree[node]):
        print_dom_tree(dom_tree, child, doms, entry, indent + 1)


def find_back_edges(cfg, doms):
    back_edges = []
    for src, succs in cfg.items():
        for dst in succs:
            # dst dominates src => back edge (loop)
            runner = src
            while runner != doms[runner]:  # walk to entry
                if runner == dst:
                    back_edges.append((src, dst))
                    break
                runner = doms[runner]
            else:
                if runner == dst:
                    back_edges.append((src, dst))
    return back_edges


if __name__ == "__main__":
    # CFG representing:
    #
    #       0
    #      / \
    #     1   2
    #      \ /
    #       3 <---\
    #       |     |
    #       4 ----/   (4 -> 3 is a back edge, forming a loop)
    #       |
    #       5
    #
    cfg = {
        0: {1, 2},
        1: {3},
        2: {3},
        3: {4},
        4: {3, 5},  # back edge 4->3 creates a loop
        5: set(),
    }
    entry = 0

    preds = build_preds(cfg)
    doms = build_dominators(cfg, entry, preds)
    dom_tree = build_dom_tree(doms, entry)
    df = build_dominance_frontier(cfg, preds, doms)
    back_edges = find_back_edges(cfg, doms)

    print("=== Immediate Dominators ===")
    for node in sorted(doms):
        print(f"  idom({node}) = {doms[node]}")

    print("\n=== Dominator Tree ===")
    print_dom_tree(dom_tree, entry, doms, entry)

    print("\n=== Dominance Frontiers ===")
    for node in sorted(cfg):
        frontier = df.get(node, set())
        print(f"  DF({node}) = {sorted(frontier)}")

    print("\n=== Back Edges (loops) ===")
    if back_edges:
        for src, dst in back_edges:
            print(f"  {src} -> {dst}  (loop header: {dst})")
    else:
        print("  None")
```

**Expected output:**
```
=== Immediate Dominators ===
  idom(0) = 0
  idom(1) = 0
  idom(2) = 0
  idom(3) = 0
  idom(4) = 3
  idom(5) = 4

=== Dominator Tree ===
[0 (entry)]
  [1 (idom: 0)]
  [2 (idom: 0)]
  [3 (idom: 0)]
    [4 (idom: 3)]
      [5 (idom: 4)]

=== Dominance Frontiers ===
  DF(0) = []
  DF(1) = [3]
  DF(2) = [3]
  DF(3) = [3]
  DF(4) = [3, 5]
  DF(5) = []

=== Back Edges (loops) ===
  4 -> 3  (loop header: 3)
```

---

## What You Can Do With It

- **Loop detection** — a back edge exists when the target node dominates the source node
- **Natural loops** — the loop body is all nodes dominated by the loop header that can reach the back edge
- **SSA construction** — place φ-functions at dominance frontiers of definition sites
- **Code motion / LICM** — hoist loop-invariant code to the immediate dominator of the loop

---

## References

- Cooper, Harvey, Kennedy — *"A Simple, Fast Dominance Algorithm"* (2001) — 4 pages, maps directly to code
- LLVM source: `llvm/lib/Analysis/DominatorTree.cpp`
- Appel — *"Modern Compiler Implementation in ML/Java/C"* (chapters on SSA)
