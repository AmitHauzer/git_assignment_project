from datetime import datetime

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Welcome to Git Assignment!!")
    print(f"The current date and time: {current_time}")


if __name__ == "__main__":
    main()
