package com.johnidouglas.ai.services;

import java.util.function.Function;

import com.johnidouglas.ai.services.MockWeatherService.Request;
import com.johnidouglas.ai.services.MockWeatherService.Response;

public class MockWeatherService implements Function<Request, Response> {

	public enum Unit { C, F }
	public record Request(String location, Unit unit) {}
	public record Response(double temp, Unit unit) {}

	public Response apply(Request request) {
		System.out.println("Getting weather for " + request.location);
		return new Response(Math.random() * 10, Unit.C);
	}
}