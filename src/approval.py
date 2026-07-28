def get_confirmation(prompt_text):
    while True:
        response = input(f"\n{prompt_text} (y/n/exit): ").lower().strip()

        if response in ["y", "yes"]:
            return "y"

        if response in ["n", "no"]:
            return "n"

        if response in ["exit", "quit", "q"]:
            return "exit"

        print("Please enter y, n, or exit.")