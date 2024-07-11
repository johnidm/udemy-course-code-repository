local char = 'a'

print(type(char))


local text = [[Hi,

How are you doing?


Tell me about your day

]]

print(text)


local value = 30

print("The amount of time are: " .. value .. " seconds")


print(string.upper("How long have you been living here?"))
print(string.lower("How ARE You Doing?"))
print(string.reverse("Is there a game running?"))


print(string.len(text))
print(#text)

local found = string.find(text, "doing")
print(found)


local start, finish = 10, 15
print(string.sub(text, start, finish))
