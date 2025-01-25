package org.example;

import java.util.ArrayList;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main_Arrays {
    public static void main(String[] args) {

        List<String> names = new ArrayList<String>(); // dynamic data structure
        names.add("Johni");
        names.add("Douglas");
        names.add("Marangon");

        System.out.println(names.size());
        System.out.println(names.get(2));
        names.remove(2);

        for ( String name : names )
            System.out.println(name);

        int[] numbers = new int[10]; // static data structure

        for (int i = 0; i < 10; i++ )
            numbers[i] = i;

        for (int i = 0; i < 10; i++ )
            if (numbers[i] == 4)
                System.out.println("I found the item " + i);
    }
}