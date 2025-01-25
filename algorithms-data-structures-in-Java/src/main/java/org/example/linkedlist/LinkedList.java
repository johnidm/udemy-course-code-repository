package org.example.linkedlist;

public class LinkedList<T> {
    private Node<T> head;
    private int length = 0;

    public LinkedList() {
        this.head = null;
    }

    public void insert(T value) {
        Node<T> item = new Node<>(value);

        item.setNext(this.head);
        this.head = item;
        this.length += 1;
    }

    public T get(int index) {
        if (this.head == null) {
            return null;
        }

        int count = 0;
        Node<T> currentNode = this.head;

        do {
            if (count == index) {
                return currentNode.getValue();
            }
            count += 1;
            currentNode = currentNode.getNext();
        } while (currentNode != null);


        return null;
    }

    public void append(T value) {
        Node<T> item = new Node<>(value);

        if (this.head == null) {
            this.head = item;
            this.length += 1;
        } else { // Convert to a recursive function
            Node<T> currentNode = this.head;
            do {
                Node<T> nextNode = currentNode.getNext();
                if (nextNode == null) {
                    currentNode.setNext( item );
                    this.length += 1;
                    break;
                }
                currentNode = nextNode;
            } while (true);
        }
    }

    public T remove(T value) {
        return null;
    }

    public int indexOf(T value) {
        return -1;
    }

    public boolean isEmpty() {
        return this.size() == 0;
    }

    public int size() {
        return this.length;
    }

    public void traverse() {
        Node<T> currentNode = this.head;

        while (currentNode != null) {
            System.out.println( currentNode.getValue() );
            currentNode =  currentNode.getNext();
        }

    }
}
