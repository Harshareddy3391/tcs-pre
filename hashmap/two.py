words = ["eat","tea","tan","ate","nat"]

map_a = {}

for word in words:
    key = "".join(sorted(word))
    map_a.setdefault(key, []).append(word)

print(map_a.values())