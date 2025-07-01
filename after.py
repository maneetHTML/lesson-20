import requests
import time
import pyperclip

def get_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["text"]
    except requests.RequestException as e:
        return f"⚠️ Error fetching fun fact: {e}"

def main_menu():
    print("\n" + "="*50)
    print("        🤓 FUN FACT TERMINAL APP 🤓")
    print("="*50)
    print("1. Get a new fun fact")
    print("2. Copy the last fact to clipboard")
    print("3. About this app")
    print("4. Exit")
    print("="*50)

def about():
    print("\n📘 This app fetches random fun facts using the public Useless Facts API.")
    print("🔗 API Source: https://uselessfacts.jsph.pl")
    print("🛠 Built with Python and ♥️ by OpenAI ChatGPT")

def run_app():
    last_fact = ""
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\nFetching a fun fact... 🤔")
            fact = get_fun_fact()
            print(f"\n💡 FUN FACT:\n{fact}")
            last_fact = fact

        elif choice == "2":
            if last_fact:
                try:
                    pyperclip.copy(last_fact)
                    print("✅ Fun fact copied to clipboard!")
                except Exception:
                    print("❌ Couldn't copy to clipboard. Make sure pyperclip is installed and working.")
            else:
                print("⚠️ No fact available to copy. Get one first!")

        elif choice == "3":
            about()

        elif choice == "4":
            print("\n👋 Goodbye! Stay curious!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

        time.sleep(1.5)

if __name__ == "__main__":
    run_app()
