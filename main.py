import argparse
from zxcvbn import zxcvbn
import itertools

# --------------------- Password Strength Analyzer ---------------------
def analyze_password_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    print("\n🔐 Password Strength Report")
    print("-" * 30)
    print(f"Password: {password}")
    print(f"Strength Score (0-4): {score}")

    if feedback['warning']:
        print(f"⚠️ Warning: {feedback['warning']}")

    if feedback['suggestions']:
        print("💡 Suggestions:")
        for suggestion in feedback['suggestions']:
            print(f"  - {suggestion}")
    print("-" * 30)

    # Optional: Save to log
    with open("password_log.txt", "a") as f:
        f.write(f"Password: {password}\n")
        f.write(f"Score: {score}\n")
        if feedback['warning']:
            f.write(f"Warning: {feedback['warning']}\n")
        if feedback['suggestions']:
            f.write("Suggestions:\n")
            for s in feedback['suggestions']:
                f.write(f"  - {s}\n")
        f.write("-" * 30 + "\n")

# --------------------- Wordlist Generator ---------------------
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

def generate_wordlist(inputs):
    base = list(filter(None, inputs))
    combos = []

    for i in range(1, len(base)+1):
        for item in itertools.permutations(base, i):
            combined = ''.join(item)
            combos.append(combined)
            combos.append(combined + '123')
            combos.append(combined + '@2024')

    for word in base:
        combos.extend(leetspeak(word))

    return list(set(combos))

def wordlist_mode(name, pet, year, fav):
    print("\n📦 Generating Custom Wordlist...\n")
    inputs = [name, pet, year, fav]
    wordlist = generate_wordlist(inputs)
    filename = "custom_wordlist.txt"
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    print(f"✅ Wordlist created with {len(wordlist)} entries.")
    print(f"📁 Saved to: {filename}")

# --------------------- Main CLI Logic ---------------------
def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer + Wordlist Generator Tool")
    parser.add_argument("--analyze", help="Analyze password strength", action="store_true")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--wordlist", help="Generate custom wordlist", action="store_true")
    parser.add_argument("--name", help="Your name")
    parser.add_argument("--pet", help="Your pet's name")
    parser.add_argument("--year", help="Birth year")
    parser.add_argument("--fav", help="Favorite word")

    args = parser.parse_args()

    if args.analyze and args.password:
        analyze_password_strength(args.password)
    elif args.wordlist:
        wordlist_mode(args.name, args.pet, args.year, args.fav)
    else:
        print("❌ Invalid usage. Use --help to see options.")

if __name__ == "__main__":
    main()
