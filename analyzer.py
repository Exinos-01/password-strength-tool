from zxcvbn import zxcvbn

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
    
if __name__ == "__main__":
    user_input = input("Enter a password to analyze: ")
    analyze_password_strength(user_input)

