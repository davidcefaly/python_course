results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad"]
print(results)

results.append("Bowser")
results.append("Donkey Kong Jr.")
print(results)

results.remove("Bowser")
print(results)

results.insert(0, "Bowser")
print(results)

print(results.count("Bowser"))

results.reverse()
print(results)
