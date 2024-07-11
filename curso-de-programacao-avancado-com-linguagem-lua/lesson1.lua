-- The local keyword makes the variable locally scoped
-- which can be used in the block where they are defined

local str = "Hello world"
local bool = false
local number = 23.6

print(str, bool, number)

print(3 % 2)  -- division remainder
print(3 ^ 2)  -- exponential


local s = "10"
local n = 10

print(type(s), type(n))
print(type(tonumber(s)), type(tostring(n)))


print(math.ceil(2.1))
print(math.floor(2.9))

print(math.fmod(12, 9))
print(math.modf(12.9))

print(math.max(3, 7, 2, 0, 3, 6, 9, 2))
print(math.min(3, 7, 2, 1, 3, 6, 9, 2))


print(math.random(2, 6))

print(math.pi, math.huge)







