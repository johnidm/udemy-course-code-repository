package org.example;

import org.example.exercicies.ArraysExercices;

import java.util.Arrays;

public class MainArraysExercicies {
    public static void main(String[] args) {
        System.out.println("My Main Class");

        ArraysExercices arr = new ArraysExercices();

//        int[] numbers = {6, 5, 4, 3, 2, 1}; // int[] n = new[3]{3, 2, 1};
//        arr.reverseArrayInPlace(numbers);
//        System.out.println(Arrays.toString(numbers));
//        String[][] anagramTestCase = {
//                {"restful", "fultser"},
//                {"hello", "world"},
//                {"cat", "bull"},
//        };
//
//        for (String[] item: anagramTestCase) {
//            String s1 = item[0];
//            String s2 = item[1];
//            boolean isAnagram = arr.anagram(s1, s2);
//            System.out.println( String.format("%s/%s is anagram: " + isAnagram, s1, s2) );
//        }

//
//        int[] nums = new int[] {1, 2, 3};
//        System.out.println( Arrays.toString( nums ) );
//
//        boolean isPalindrome = arr.isPalindrome("radar");
//        System.out.println( "radar  is palindrome: " + isPalindrome );
//
        int reversed = arr.reverseInt(1234);
        System.out.println( "reversed integer: " + reversed );

    }
}
