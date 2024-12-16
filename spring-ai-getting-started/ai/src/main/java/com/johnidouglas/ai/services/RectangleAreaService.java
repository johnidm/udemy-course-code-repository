package com.johnidouglas.ai.services;

import java.util.function.Function;

import com.johnidouglas.ai.services.RectangleAreaService.Request;
import com.johnidouglas.ai.services.RectangleAreaService.Response;

public class RectangleAreaService implements Function<Request, Response> {

    public record Request(double base, double height) {
    }

    public record Response(double area) {
    }

    @Override
    public Response apply(Request r) {
        System.out.println("Calculating area of rectangle with base " + r.base() + " and height " + r.height());
        return new Response(r.base() * r.height());
    }

}