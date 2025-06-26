import itertools

def leetspeak(word):
    replacements = {
        'a': ['a', '@', '4'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        's': ['s', '$', '5'],
        't': ['t', '7']
    }
    
    def recursive_leet(w, i=0):
        if i == len(w):
            return ['']
        chars = replacements.get(w[i].lower(), [w[i]])
        rest = recursive_leet(w, i+1)
        return [c + r for c in chars for r in rest]
    
    return list(set(recursive_leet(word)))

def generate_variations(inputs):
    base = list(filter(None, inputs))  # remove empty inputs
    combos = []

    # Generate direct combos
    for i in range(1, len(base)+1):
        for item in itertools.permutations(base, i):
            combined = ''.join(item)
            combos.append(combined)
            combos.append(combined + '123')
            combos.append(combined + '@2024')

    # Add leetspeak variants
    for word in base:
        combos.extend(leetspeak(word))

    return list(set(combos))  # remove duplicates

def main():
    print("🔧 Custom Wordlist Generator\n")
    name = input("Enter your name: ").strip()
    pet = input("Enter your pet's name: ").strip()
    birth_year = input("Enter your birth year: ").strip()
    fav_word = input("Enter your favorite word: ").strip()

    inputs = [name, pet, birth_year, fav_word]
    wordlist = generate_variations(inputs)

    filename = "custom_wordlist.txt"
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"\n✅ Wordlist generated with {len(wordlist)} entries.")
    print(f"📁 Saved to: {filename}")

if __name__ == "__main__":
    main()
