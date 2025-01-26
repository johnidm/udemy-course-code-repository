package org.example;

import org.example.linkedlist.LinkedList;

public class Main {
    public static void assertEx(boolean value) {
        if (!value) {
            throw new AssertionError("Assert error!");
        }
    }
    public static void main(String[] args) {
        // Remove single item from a list containing only one element.
        LinkedList<String> l1 = new LinkedList<>();
        l1.remove(3);
        l1.append("Johni");
        l1.remove(4);
        l1.remove(0);
        assertEx (l1.isEmpty());

        // Remove first item from a list of two elements.
        LinkedList<String> l2 = new LinkedList<>();
        l2.append("Johni");
        l2.append("Douglas");
        l2.remove(0);
        assertEx( l2.size() == 1);

        // Remove middle item frmo a list of three elements.
        LinkedList<String> l3 = new LinkedList<>();
        l3.append("Johni");
        l3.append("Douglas");
        l3.append("Lara");
        l3.remove(1);
        assertEx( l3.size() == 2);

        LinkedList<String> l4 = new LinkedList<>();
        l4.append("Johni");
        l4.append("Douglas");
        l4.append("Marti");
        l4.append("Lara");
        l4.insert( "Adam" );
        l4.insert( "Yas" );
        l4.remove(5);
        assertEx( l4.size() == 5);

        LinkedList<String> l5 = new LinkedList<>();
        l5.append("Johni");
        l5.append("Douglas");
        l5.append("Marti");

        assertEx( l5.get(0).equals("Johni"));
        assertEx( l5.get(3) == null);

        assertEx( l5.indexOf("") == -1);
        assertEx( l5.indexOf("Douglas") == 1);


        LinkedList<String> l6 = new LinkedList<>();
        l6.append("Johni");
        l6.append("Douglas");
        l6.append("Marti");

        for (String i : l6) {
            System.out.println(i);
        }

    }
}
