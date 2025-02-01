package org.example.exercicies;

import javax.lang.model.type.IntersectionType;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class ArraysExercices {


    public void reverseArrayInPlace(int[] numbers) {
        /*
        * Reversing an array in-place exercise.
        *
        * In this exercise, you have to reverse a T[] array in
        * O(N) linear time complexity and we want the algorithm
        * to be in-place as well - so the algorithm can not use
        * additional memory!
        * For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
        *
        * Hint: define 2 pointers (pointing to the last and first item of the array)
        * and make a single iteration
        */

        // This is a two pointers solution.
        int i = 0;
        int j = numbers.length - 1;
        while (i < j) {
            int numI = numbers[i];

            numbers[i] = numbers[j];
            numbers[j] = numI;
            i++;
            j--;
        }

        // Single pointer approach
//        for (int start = 0; start < numbers.length / 2; start++) {
//            int temp = numbers[start];
//            int end = numbers.length - start -1;
//            System.out.println(  Integer.toString(start) + Integer.toString(end));
//            numbers[start] = numbers[end];
//            numbers[end] = temp;
//        }

//        int[] n = new int[ numbers.length ];
//        for (int i = n.length - 1; i >= 0; --i)
//            n[numbers.length - i - 1] = numbers[i];
//
//        for (int i = 0; i < numbers.length; i++)
//            numbers[i] = n[i];
    }


    public boolean anagram(String s1, String s2) {
        /*
         * Anagram problem exercise
         *
         * Your task is to construct an algorithm to check whether
         * two words (or phrases) are anagrams or not!
         *
         * An anagram is a word or phrase formed by rearranging the letters of a
         * different word or phrase, typically using all the original letters
         * exactly once
         *
         * For example: restful and fluster are anagrams.
         *
         * Hint: you get the s1 and s2 strings (char sequences) and you have to
         * return true (if they are anagram) or false otherwise
         */
// Loop and contains
//        for ( char c : s1.toCharArray() ) {
//            if ( !s2.contains(String.valueOf(c)) ) {
//                return false;
//            }
//        }
//        return true;
        // Counting frequency maps

//        return false;
        // Sorting and compare
        char[] c1 =  s1.toCharArray();
        char[] c2 =  s2.toCharArray();
        Arrays.sort( c1 );
        Arrays.sort( c2 );

        return Arrays.equals(c1, c2);


    }

    public boolean isPalindrome(String s) {
        /*
        * Palindrome problem exercise
        *
        * A palindrome is a string that reads the same forward and backward
        * Your task is to design an optimal algorithm for checking whether a
        * given string is palindrome or not!
        *
        * For example: radar or madam.
        *
        * Hint:  define 2 pointers (forward pointer and backward pointer
        * and compare characters accordingly)
        */
//        int len = s.length();
//        char[] c = s.toCharArray();
//        for (int i = 0; i < len; i++) {
//            int index = len - i - 1;
//            if (c[i] != c[index]) {
//                return false;
//            }
//            // System.out.println( Integer.toString(i) + " " + Integer.toString(index) );
//        }
//
//        return true;

        int forward = 0;
        int backward = s.length() - 1;

        while (forward < backward) {
            if ( s.charAt(forward) != s.charAt(backward) )
                return false;

            forward++;
            backward--;
        }
        return true;
    }


    public int reverseInt(int n) {
        /*
        * Integer reversion exercise
        *
        * Your task is to design an efficient algorithm to reverse a given integer.
        * For example if the input of the algorithm is 1234 then the output should be 4321.
        * NOTE: the input is an integer (and not a string).
        *
        */

        int reversed = 0;
        int remainder = 0;
        int division = n;

        while (division != 0) {
            remainder = division % 10;
            division = division / 10;
            reversed =   reversed * 10 + remainder;
        }

        return reversed;
    }

}





