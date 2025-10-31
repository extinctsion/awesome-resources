class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const reverseLinkedList = head => {
  let prev = null;
  let current = head;
  while (current) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
};

// Example 
const a = new Node(1);
const b = new Node(2);
const c = new Node(3);
a.next = b; b.next = c;
console.log(reverseLinkedList(a)); // returns reversed list