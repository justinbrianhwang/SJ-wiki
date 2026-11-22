---
title: Linked Lists
sidebar_position: 5
---

# Linked Lists

Linked lists (연결 리스트) replace the array's contiguous storage with nodes connected by pointers. This single change alters the tradeoffs: insertion and deletion near a known node can be constant time, but random access by index is no longer constant because the list must be traversed link by link. In C, linked lists also force careful handling of allocation, pointer updates, and ownership.

The source textbook introduces lists after stacks and queues, then uses them to implement linked stacks, linked queues, polynomial lists, sparse matrices, circular lists, and doubly linked lists. That order is natural. Once a node can point to another node, the same idea can represent many structures: a chain, a ring, a two-way sequence, a sparse row, or an adjacency list in a graph.

## Definitions

A **node** is a record containing a data field and one or more links. In C:

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

A **singly linked list** stores one link per node, usually named `next`. The list is reached through a head pointer. Traversal is one-way.

A **doubly linked list** stores `prev` and `next`, allowing traversal in both directions and $O(1)$ deletion when a pointer to the node is known.

A **circular linked list** makes the last node point back to the first, or uses a header node whose link eventually returns to the header. Circular lists are useful when operations repeatedly cycle through items or when a sentinel header simplifies edge cases.

The **list ADT** commonly includes:

- **`insert_front(L, x)`**: insert at the beginning.
- **`insert_after(p, x)`**: insert after a known node `p`.
- **`delete_after(p)`**: remove the node after `p`.
- **`find(L, key)`**: return a pointer to the first matching node.
- **`traverse(L, visit)`**: apply a function or action to each element in order.
- **`is_empty(L)`**: report whether the head is `NULL` or the sentinel points to itself.

The phrase "known node" is important. Linked lists do not make searching free. If you only know an index or a key, you must first traverse to the position.

## Key results

For a singly linked list with only a head pointer, inserting at the front is $O(1)$, deleting the front is $O(1)$, searching is $O(n)$, and accessing the $i$th element is $O(i)$. If a tail pointer is also maintained, appending at the rear is $O(1)$; otherwise appending requires traversal and costs $O(n)$.

Deleting a specific node from a singly linked list requires access to the previous node, because the previous node's `next` field must be redirected. Doubly linked lists store that previous link explicitly, trading memory for simpler deletion.

Pointer update order is a correctness issue. To insert a new node after `p`, set the new node's link first:

$$
\begin{aligned}
\text{new->next} &= \text{p->next} \\
\text{p->next} &= \text{new}
\end{aligned}
$$

If `p->next` is overwritten before being saved, the suffix of the list can be lost.

| Operation | Singly list with head | Singly list with head+tail | Doubly linked list |
|---|---:|---:|---:|
| Insert at front | $O(1)$ | $O(1)$ | $O(1)$ |
| Delete at front | $O(1)$ | $O(1)$ | $O(1)$ |
| Append at rear | $O(n)$ | $O(1)$ | $O(1)$ with tail |
| Search by key | $O(n)$ | $O(n)$ | $O(n)$ |
| Delete known node | needs previous node | needs previous node | $O(1)$ |
| Access by index | $O(n)$ | $O(n)$ | $O(n)$ |

Many list implementations use a **header** or **sentinel** node. A sentinel does not store a real user value; it marks the boundary of the list. With a sentinel, insertion and deletion near the front can avoid special cases because there is always a node before the first real element. Circular lists often use a sentinel whose `next` points to itself when the list is empty. The invariant becomes "starting at the sentinel and following `next` eventually returns to the sentinel."

Another important C technique is passing a pointer to the head pointer, written as `Node **head`. This lets a function update the caller's head when insertion or deletion changes the first node. Without that, deleting the first node would only change a local copy of the head pointer. This is not a linked-list concept mathematically, but it is a central implementation detail in C.

Linked lists are not automatically better than arrays. They use extra memory for pointers, scatter nodes across the heap, and have poor cache locality. Their advantage appears when pointer splicing avoids large shifts or when the structure naturally grows and shrinks in many small pieces.

A useful performance rule is to count both traversal and update. Inserting after a pointer you already have is $O(1)$, but inserting at sorted position is $O(n)$ because finding that position dominates. Many incorrect comparisons between arrays and lists forget this search cost.

This distinction is why list questions often state whether the node pointer is already available.

## Visual

```mermaid
flowchart LR
  H[head] --> A["node: 10"]
  A --> B["node: 20"]
  B --> C["node: 30"]
  C --> N[NULL]
```

Doubly linked nodes carry links in both directions:

```text
NULL <- [prev|10|next] <-> [prev|20|next] <-> [prev|30|next] -> NULL
```

## Worked example 1: inserting after a node in a singly linked list

Problem: A list contains `10 -> 30 -> 40 -> NULL`. A pointer `p` points to the node containing `10`. Insert `20` after `p`.

Method: allocate a new node, connect it to the old successor, then connect `p` to the new node.

1. Initial state:

```text
p
|
10 -> 30 -> 40 -> NULL
```

2. Allocate `new` with `new->value = 20`.
3. Save the suffix by setting `new->next = p->next`. Since `p->next` points to `30`, the new node now points to `30`.
4. Link `p` to the new node by setting `p->next = new`.

Final state:

```text
10 -> 20 -> 30 -> 40 -> NULL
```

Checked answer: no node was lost. Starting from head and following `next` fields visits `10`, then `20`, then `30`, then `40`, then `NULL`. The two pointer assignments were enough because insertion happened after a known node.

## Worked example 2: deleting a node from a doubly linked list

Problem: A doubly linked list contains `A <-> B <-> C <-> D`. A pointer `p` points to `C`. Delete `C`.

Method: redirect the neighboring links around `C`, then free `C`.

1. Identify neighbors:
   - `p->prev` is `B`.
   - `p->next` is `D`.
2. Since `p->prev` exists, set `p->prev->next = p->next`. Now `B->next` points to `D`.
3. Since `p->next` exists, set `p->next->prev = p->prev`. Now `D->prev` points to `B`.
4. Free `p`.

Final state:

```text
A <-> B <-> D
```

Checked answer: forward traversal gives `A, B, D`, and backward traversal from `D` gives `D, B, A`. Both directions agree that `C` has been removed. If `C` had been the head or tail, one of the neighbor checks would update the external head or tail pointer instead.

## Code

This program implements a sorted singly linked list. Insertions allocate nodes and maintain ascending order; deletion removes the first matching value.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

static Node *make_node(int value) {
    Node *node = malloc(sizeof(*node));
    if (node == NULL) {
        fprintf(stderr, "malloc failed\n");
        exit(EXIT_FAILURE);
    }
    node->value = value;
    node->next = NULL;
    return node;
}

static void sorted_insert(Node **head, int value) {
    Node *node = make_node(value);
    if (*head == NULL || value < (*head)->value) {
        node->next = *head;
        *head = node;
        return;
    }

    Node *cur = *head;
    while (cur->next != NULL && cur->next->value < value) {
        cur = cur->next;
    }
    node->next = cur->next;
    cur->next = node;
}

static int delete_value(Node **head, int value) {
    Node *cur = *head;
    Node *prev = NULL;
    while (cur != NULL && cur->value != value) {
        prev = cur;
        cur = cur->next;
    }
    if (cur == NULL) return 0;
    if (prev == NULL) {
        *head = cur->next;
    } else {
        prev->next = cur->next;
    }
    free(cur);
    return 1;
}

static void print_list(const Node *head) {
    for (const Node *cur = head; cur != NULL; cur = cur->next) {
        printf("%d%s", cur->value, cur->next == NULL ? "\n" : " -> ");
    }
}

static void destroy(Node *head) {
    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}

int main(void) {
    Node *list = NULL;
    sorted_insert(&list, 30);
    sorted_insert(&list, 10);
    sorted_insert(&list, 20);
    sorted_insert(&list, 40);
    delete_value(&list, 30);
    print_list(list);
    destroy(list);
    return EXIT_SUCCESS;
}
```

## Common pitfalls

- Losing the rest of the list by overwriting `p->next` before saving it during insertion.
- Deleting from a singly linked list without tracking the previous node.
- Forgetting to update the head pointer when inserting or deleting at the front.
- Forgetting to update the tail pointer when deleting the last node in a list that maintains one.
- Traversing a circular list with `while (p != NULL)`. Circular lists do not end with `NULL`; they need a sentinel or a stop condition based on returning to the start.
- Leaking memory by removing nodes from the chain without calling `free`.
- Freeing a node and then reading its fields. Store needed links before `free`.

## Connections

- [stacks](/cs/data-structures/stacks)
- [queues](/cs/data-structures/queues)
- [hashing](/cs/data-structures/hashing)
- [graph representation](/cs/data-structures/graph-representation)
- [binary trees](/cs/data-structures/binary-trees)
