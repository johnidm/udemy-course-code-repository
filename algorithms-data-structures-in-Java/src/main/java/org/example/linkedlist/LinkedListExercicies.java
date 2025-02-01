package org.example.linkedlist;

public class LinkedListExercicies {

    public void reverse(LinkedList<Integer> l) {
        /*
        * Reverse a linked list in-place exercise
        * Construct an in-place algorithm (without the need for extra memory)
        * to reverse a linked list!
        *
        * For example: 1 -> 2 -> 3 -> 4 should be transformed into 4 -> 3 -> 2 -> 1
        */
    }

    public int findMiddleNode(LinkedList<Integer> l) {
        /*
        * Finding the middle node in a linked list exercise.
        *
        * Suppose we have a standard linked list.
        * Construct an in-place (without extra memory) algorithm
        * that is able to find the middle node!
        * Note: you should construct an O(N) linear running time algorithm
        *
        * For example: [1, 2, 3, 4] --> middle node is: 3,   [1, 2, 3, 4, 5] --> middle node is: 3
        *
        * WE ASSUME THAT WE STORE INTEGERS IN THE LINKED LIST
        * NO NEED TO USE GENERIC IMPLEMENTATION !!!
        */

        int middle = l.size() / 2;
        int count =0;

        for (Integer i : l) {
            if (count >= middle)
                return i;

            count++;
        }

        return 0;
    }
}
