package main

type Node struct {
	Value int
	Next  *Node
}

type List struct {
	Head *Node
}

func NewNode(v int) *Node {
	return &Node{Value: v}
}

func NewList() *List {
	return &List{}
}

func InitList(sl []int) *List {
	l := NewList()
	for _, v := range sl {
		l.append(v)
	}
	return l
}

func (l *List) Get(idx int) int {
	cur := l.Head

	for i := 0; i < idx; i++ {
		if cur.Next == nil {
			panic("index out of range")
		}
		cur = cur.Next
	}

	return cur.Value
}

func (l *List) Len() int {
	cur := l.Head
	count := 0
	for cur != nil {
		count++
		cur = cur.Next
	}
	return count
}

func (l *List) append(n int) {
	newNode := NewNode(n)
	if l.Head == nil {
		l.Head = newNode
		return
	}

	cur := l.Head
	for cur.Next != nil {
		cur = cur.Next
	}
	cur.Next = newNode
}

func (l *List) prepend(n int) {
	newNode := NewNode(n)
	newNode.Next = l.Head
	l.Head = newNode
}

func (l *List) Insert(idx, n int) {
	if idx == 0 {
		l.prepend(n)
		return
	}

	cur := l.Head
	for i := 0; i < idx-1; i++ {
		if cur.Next == nil {
			panic("index out of range")
		}
		cur = cur.Next
	}

	newNode := NewNode(n)
	newNode.Next = cur.Next
	cur.Next = newNode
}

func (l *List) Delete(idx int) {
	if idx == 0 {
		l.Head = l.Head.Next
		return
	}

	cur := l.Head
	for i := 0; i < idx-1; i++ {
		if cur.Next == nil {
			panic("index out of range")
		}
		cur = cur.Next
	}

	cur.Next = cur.Next.Next
}

func (l *List) Reverse() {
	var prev, next *Node
	cur := l.Head

	for cur != nil {
		next = cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}

	l.Head = prev
}
