package org.example;

import org.example.linkedlist.LinkedList;
import org.example.linkedlist.LinkedListExercicies;

public class MainLinkedListExercicies {
    public static void main(String[] args) {
        LinkedListExercicies exer = new LinkedListExercicies();

        LinkedList<Integer> nums1 = new LinkedList<>();
        nums1.append(1);
        nums1.append(2);
        nums1.append(3);
        nums1.append(4);
        nums1.append(5);
        nums1.append(6);
        nums1.append(7);
        nums1.append(8);
        nums1.append(9);
        nums1.traverse();
        nums1.reverse();
        nums1.traverse();

//        int middle = exer.findMiddleNode(nums1);
//        System.out.println(middle);
//        System.out.println( nums1.getMiddle() );

    }
}
