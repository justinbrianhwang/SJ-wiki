---
title: Linked Data Structures
sidebar_position: 16
---

# Linked Data Structures

Linked data structures store data in nodes connected by pointers. Unlike arrays, the nodes do not need to occupy one contiguous block of memory. This makes linked structures useful when a collection grows, shrinks, or rearranges frequently, but the flexibility comes with pointer management responsibilities.

Savitch's linked-list material builds directly on pointers, dynamic memory, classes, destructors, and copy control. A node allocated with `new` must eventually be released with `delete`, and a class that owns a chain of nodes needs a destructor, copy constructor, and assignment operator if it allows copying.

## Nodes, links, and ownership

A **node** is a small object that stores data plus one or more links to other nodes. A singly linked list node usually has a data field and a pointer to the next node:

```cpp
struct Node {
    int data;
    Node* next;
};
```

The **head pointer** points to the first node in the list. The empty list is represented by `head == nullptr`.

```text
head
 |
 v
+----+------+     +----+------+     +----+------+
| 10 |  *---+---->| 20 |  *---+---->| 30 | null |
+----+------+     +----+------+     +----+------+
```

A **linked list** is a sequence of nodes where each node points to the next. A **stack** can be implemented by inserting and removing at the head. A **queue** can be implemented with both front and back pointers. A **tree** uses nodes with multiple child pointers.

A **traversal** walks through a linked structure by following links:

```cpp
for (Node* p = head; p != nullptr; p = p->next) {
    cout << p->data << endl;
}
```

The arrows express reachability, not physical adjacency. Two neighboring nodes may be far apart in memory, and allocation order need not match list order. A link stores an address; following it requires an extra memory access. That indirection is why the asymptotic benefit of cheap insertion does not automatically translate into faster programs than a contiguous container.

Ownership must be distinguished from navigation. In the elementary representation, the list object owns every node reachable from `head`, while each raw `next` pointer merely records the chain. Client code that retains a node pointer after deletion has a dangling non-owning pointer. A modern implementation can express the one-way ownership chain with `std::unique_ptr<Node>`, though insertion and deletion still require careful link updates.

## Operations and the invariant they preserve

Inserting at the front of a singly linked list is constant time because it changes only two pointers:

```cpp
Node* newNode = new Node;
newNode->data = value;
newNode->next = head;
head = newNode;
```

Searching a linked list is linear time because there is no direct indexing. To find a value, a program may need to inspect every node:

$$
T(n) = O(n)
$$

Deleting a node requires preserving the link to the rest of the list before releasing memory. To delete the head:

```cpp
Node* doomed = head;
head = head->next;
delete doomed;
```

To delete a node after a pointer `before`, update `before->next` to skip the doomed node:

```cpp
Node* doomed = before->next;
before->next = doomed->next;
delete doomed;
```

A class that owns a linked list must obey the same resource-management rule introduced for dynamic arrays: if it defines a destructor, it usually also needs a copy constructor and assignment operator. Otherwise, two list objects may point to the same nodes, causing double deletion or accidental shared mutation.

The central invariant for a well-formed singly linked list is: starting at `head`, following `next` pointers eventually reaches `nullptr` and does not revisit a node. Operations preserve this invariant by connecting new nodes before exposing them through `head`, and by bypassing deleted nodes before freeing them.

Keeping a tail pointer changes which operations are constant time. With only `head`, appending requires a full traversal. With `head` and `tail`, append is constant time, provided every operation maintains two extra conditions: both pointers are null for an empty list, and `tail->next` is null for a nonempty list. Removing the last node of a singly linked list is still linear because there is no link back to its predecessor.

A doubly linked list stores both `next` and `previous`. Given a pointer or iterator to a node, removal can update its two neighbors in constant time. The cost is another pointer per node and more invariant work per mutation. A circular list replaces an end null with a link back to the beginning; traversal then needs an explicit stopping condition to avoid looping forever.

Complexity claims assume the relevant node is already known. “Insert after node $p$” is $O(1)$, but “find the node containing 37 and insert after it” includes an $O(n)$ search. Likewise, deletion by value is linear even though the actual unlink step is constant time.

## Contiguous storage versus linked storage

```mermaid
flowchart LR
  A[Create new node] --> B[Store value]
  B --> C["newNode->next = head"]
  C --> D["head = newNode"]
  D --> E[List has one more first node]
```

| Operation | Array cost | Singly linked list cost | Reason |
|---|---:|---:|---|
| Access item by index | `O(1)` | `O(n)` | Linked list must follow links |
| Insert at front | `O(n)` | `O(1)` | Array shifts; list relinks head |
| Delete after known node | `O(n)` shift | `O(1)` | List changes one link |
| Search by value | `O(n)` | `O(n)` | Both may inspect many elements |
| Extra memory per item | Low | Higher | List stores pointer field |

Arrays and vectors benefit from spatial locality: fetching one element often brings nearby elements into cache. A linked traversal may incur a cache miss at each node. For small values and ordinary sequential work, `std::vector` can outperform a linked list even when the vector occasionally shifts elements. Linked structures earn their cost when stable node addresses, cheap splicing, or frequent insertion at a known position matters.

## Worked example: inserting at the head

Problem: Start with an empty list and insert `30`, then `20`, then `10` at the head. What is the final list?

Method:

1. Begin empty:

   ```text
   head = null
   ```

2. Insert `30`:

   ```cpp
   newNode->data = 30;
   newNode->next = head;  // null
   head = newNode;
   ```

   List:

   ```text
   head -> 30 -> null
   ```

3. Insert `20`:

   ```cpp
   newNode->data = 20;
   newNode->next = head;  // old 30 node
   head = newNode;
   ```

   List:

   ```text
   head -> 20 -> 30 -> null
   ```

4. Insert `10`:

   ```cpp
   newNode->data = 10;
   newNode->next = head;  // old 20 node
   head = newNode;
   ```

Checked answer:

```text
head -> 10 -> 20 -> 30 -> null
```

Head insertion reverses the order of insertion because each new value becomes the first node.

At every step the new node is fully initialized before `head` changes. If allocation fails, `new` throws and the old list is untouched. Once `newNode->next` records the previous head, assigning `head = newNode` cannot lose the old chain. Reversing those two pointer assignments would make `newNode->next` point to itself and orphan the former list.

## Worked example: deleting a middle node

Problem: A list contains `10 -> 20 -> 30 -> 40 -> null`. A pointer `before` points to the node containing `20`. Delete the following node.

Method:

1. Identify the node to delete:

   ```text
   before -> [20 | next] -> [30 | next] -> [40 | null]
   ```

   So `before->next` is the node containing `30`.

2. Save that pointer:

   ```cpp
   Node* doomed = before->next;
   ```

3. Link around it:

   ```cpp
   before->next = doomed->next;
   ```

   Now the logical list is:

   ```text
   10 -> 20 -> 40 -> null
   ```

4. Release the removed node:

   ```cpp
   delete doomed;
   ```

Checked answer: the value `30` is removed, `20` now points to `40`, and no allocated node has been leaked.

The precondition is that `before` and `before->next` are both non-null and belong to this list. If `before` points at the last node, there is no following node to delete. If it comes from another list, relinking can corrupt one structure while freeing storage owned by another. A public container interface normally exposes iterators with documented provenance requirements rather than accepting arbitrary raw node pointers.

## An owning list with deep-copy semantics

```cpp
#include <iostream>
using namespace std;

class IntList {
private:
    struct Node {
        int data;
        Node* next;
    };

public:
    IntList() : head(nullptr) {}

    IntList(const IntList& other) : head(nullptr) {
        try {
            Node* tail = nullptr;
            for (const Node* p = other.head; p != nullptr; p = p->next) {
                Node* copy = new Node{p->data, nullptr};
                if (head == nullptr) {
                    head = copy;
                    tail = copy;
                } else {
                    tail->next = copy;
                    tail = copy;
                }
            }
        } catch (...) {
            clear();
            throw;
        }
    }

    ~IntList() {
        clear();
    }

    IntList& operator=(const IntList& right) {
        if (this == &right) {
            return *this;
        }

        IntList temp(right);
        swapHeads(temp);
        return *this;
    }

    void pushFront(int value) {
        Node* newNode = new Node{value, head};
        head = newNode;
    }

    bool contains(int value) const {
        for (const Node* p = head; p != nullptr; p = p->next) {
            if (p->data == value) {
                return true;
            }
        }
        return false;
    }

    void print() const {
        for (const Node* p = head; p != nullptr; p = p->next) {
            cout << p->data << " ";
        }
        cout << endl;
    }

private:
    Node* head;

    void clear() {
        while (head != nullptr) {
            Node* doomed = head;
            head = head->next;
            delete doomed;
        }
    }

    void swapHeads(IntList& other) {
        Node* temp = head;
        head = other.head;
        other.head = temp;
    }
};

int main() {
    IntList list;
    list.pushFront(30);
    list.pushFront(20);
    list.pushFront(10);

    list.print();
    cout << boolalpha << list.contains(20) << endl;

    IntList copy = list;
    copy.pushFront(5);
    copy.print();
    list.print();
}
```

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

int length(Node* head) {
    int count = 0;
    for (Node* p = head; p != nullptr; p = p->next) {
        ++count;
    }
    return count;
}

int main() {
    Node third = {30, nullptr};
    Node second = {20, &third};
    Node first = {10, &second};

    cout << length(&first) << endl;
}
```

The `try` block in the copy constructor closes a subtle leak. If allocating the fifth copied node throws, the `IntList` object has not completed construction, so its destructor will not run. The handler clears the already built prefix and rethrows. Assignment uses copy-and-swap: if copying fails, the left operand is unchanged; if it succeeds, the temporary takes ownership of the old chain and deletes it on return.

The const member functions traverse with `const Node*`. A const list operation should not mutate node data through an internal pointer. The original pointer representation does not enforce deep constness automatically, so choosing a pointer-to-const during read-only traversal records the intended restriction.

The second program uses stack-allocated nodes and owns no dynamic memory. Its links remain valid only while `first`, `second`, and `third` are alive. Returning `&first` from a function would leave every pointer dangling when those local nodes were destroyed.

## Pointer failures and invalidated positions

- Losing the rest of the list by overwriting `head` before storing the old value in `newNode->next`.
- Deleting a node and then reading `doomed->next`. Save all needed links before `delete`.
- Forgetting to delete dynamically allocated nodes in the destructor.
- Allowing the default copy constructor for a class that owns nodes. The default copy is shallow and makes two list objects share the same chain.
- Treating linked lists as if they had constant-time indexing. To reach item `i`, the program follows `i` links.
- Failing to handle the empty-list and one-node-list cases separately when they need special pointer updates.

While tracing links:

- Draw the list before and after every insertion or deletion. Label `head`, any traversal pointer, and the node that will be deleted. Many linked-list bugs become obvious when the arrows are visible.
- Never overwrite the only pointer to a node unless another pointer already reaches that node. Losing the last pointer to allocated memory creates a leak because the program has no address to pass to `delete`.
- Treat deletion as two separate actions: first remove the node from the chain, then release its memory. Reversing the order makes it tempting to read through a dangling pointer.
- Test operations on the empty list, the first node, a middle node, and the last node. A deletion function that works only for the middle case is incomplete.
- For a class-owned list, decide whether copying is allowed. If copying is not meaningful, disable it; if it is meaningful, implement a deep copy so each list owns its own nodes.
- Keep traversal loops simple. A loop that advances two or three pointers at once should have a clear invariant, such as "`previous` is always the node before `current`."
- Prefer STL containers in application code unless the goal is to study links directly. `list`, `vector`, `queue`, and `stack` already implement ownership and cleanup correctly.

For every pointer variable in a linked-list function, state what it points to before the loop, during one middle iteration, and after the loop. If a pointer's meaning changes from "current node" to "previous node" halfway through the function, rename it or split the logic. Clear pointer roles are more reliable than clever pointer movement.

When debugging, print node addresses as well as data values if the output looks impossible. Seeing two list objects print the same node addresses is strong evidence of a shallow copy. Seeing a cycle of repeated addresses explains an infinite traversal loop.

Every path through the operation must preserve reachability. After insertion, the new node should be reachable from `head`. After deletion, the remaining nodes should still be reachable, and the deleted node should no longer be reachable from the list.

Iterators and pointers to an erased node become invalid immediately. Other node addresses in a typical linked list remain stable across insertion and unrelated erasure, which is one advantage over vector reallocation. Stability does not extend past destruction of the whole list, and an iterator cannot safely reveal whether its node has already been freed.

Cycle detection is useful when corruption or intentionally cyclic input is possible. Floyd's algorithm advances one pointer by one edge and another by two. If they meet, a cycle exists; if the faster pointer reaches null, the chain terminates. Detection prevents an infinite traversal but does not by itself repair ownership or decide which link should be broken.

Recursive destruction that lets each node delete its successor looks compact, but a very long list can exhaust the call stack. The iterative `clear` loop uses constant call-stack space. Each iteration saves the next link, advances the owning head, and only then frees the old node.

A queue implemented with head and tail pointers exposes a useful empty-state edge case. Enqueueing the first node must set both pointers to that node. Dequeueing the final node advances the head to null and must also reset the tail to null; otherwise the tail dangles. Between those cases, enqueue changes the old tail's next link and then advances tail, while dequeue changes only head and deletes the former first node.

<div className="see-also">

See also: [pointers and dynamic memory](/cs/programming/cpp/pointers-and-dynamic-memory) · [constructors and copy semantics](/cs/programming/cpp/constructors-and-copy-semantics) · [recursion](/cs/programming/cpp/recursion) · [stl containers](/cs/programming/cpp/stl-containers) · [classes and encapsulation](/cs/programming/cpp/classes-and-encapsulation)

</div>
