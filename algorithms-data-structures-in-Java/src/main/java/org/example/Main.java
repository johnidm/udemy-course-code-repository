package org.example;

import org.example.linkedlist.LinkedList;

public class Main {
    public static void assertEx(boolean value) {
        if (!value) {
            throw new AssertionError("Assert error!");
        }
    }
    public static void main(String[] args) {

        LinkedList<String> list = new LinkedList<>();

        assertEx (list.isEmpty());
        assertEx (list.get(1) == null);

        list.append("Johni");
        list.append("Douglas");
        list.append("Marti");
        list.append("Lara");

        list.insert( "Adam" );
        list.insert( "Yas" );

        assertEx( !list.isEmpty());
        assertEx( list.size() == 6);

        list.traverse();

        assertEx( list.get(0).equals("Yas"));
        assertEx( list.get(3).equals("Douglas"));
        assertEx( list.get(5).equals("Lara"));

    }
}
