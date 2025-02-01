package org.example.linkedlist;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class LinkedList<T> implements Iterable<T> {
    private Node<T> head;
    private int length = 0;

    public void reverse() {

        Node<T> current = this.head;
        Node<T> next = null;
        Node<T> privious = null;

        while (current != null) {
            next = current.next;
            current.next = privious;
            privious = current;
            current = next;
        }

        this.head = privious;

    }

    public T getMiddle() {
        Node<T> slow = this.head;
        Node<T> fast = this.head;

        while (( slow.next != null ) && (fast.next != null) && (fast.next.next != null)) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow.value;
    }

    public void insert(T value) {
        /*
         * Insert a new item to the beginning
         * The time complexity is O(1)
         */

        Node<T> item = new Node<>(value);

        item.next = this.head;
        this.head = item;
        this.length += 1;
    }

    public void append(T value) {
        /*
          Insert a new item t the ending
          The time complexity is O(n)
         */

        Node<T> item = new Node<>(value);

        if (this.head == null) {
            this.head = item;
        } else {
            Node<T> current = this.head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = item;
        }
        this.length += 1;
    }

    public T get(int index) {
        /*
        * Return the value corresponding to the index
        * The time complexity is O(n)
        */

        int count = 0;
        
        Node<T> current = this.head;
        while (current != null) {
            if (count == index ) {
                return current.value;
            }
            current = current.next;
            count += 1;
        }
        
        return null;
    }

    public void remove(int index) {
        /*
        * Remove the item corresponding to the index.
        * The time complexity is O(n)
        * */
        if (this.head == null) {
            return;
        }

        if (index == 0 ) {
            this.head = this.head.next;
            this.length -= 1;
            return;
        }

        int count = 1;
        Node<T> current = this.head.next;
        Node<T> prior = this.head;

        while (current != null) {
            if (count == index) {
                prior.next = current.next;
                this.length -= 1;
                return;
            }

            prior = current;
            current = current.next;
            count += 1;
        }
    }

    public int indexOf(T value) {
        /*
        * Return the index corresponding to the value
        * The time complexity is O(n)
        */

        Node<T> current = this.head;
        int count = 0;
        while (current != null) {
            if (current.value == value) {
                return count;
            }
            current = current.next;
            count += 1;
        }

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
            System.out.println( currentNode.value);
            currentNode =  currentNode.next;
        }

    }

    @Override
    public Iterator<T> iterator() {
        return new LinkedListIterator();
    }

    // Inner class implementing the Iterator interface
    private class LinkedListIterator implements Iterator<T> {
        private Node<T> current = head;

        // Check if there is a next element
        @Override
        public boolean hasNext() {
            return current != null;
        }

        // Return the next element
        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T data = current.value;
            current = current.next;
            return data;
        }
    }
}
