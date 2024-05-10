from src.generator import gen_password
from gui import create_window
def main() -> int:
    try:
        password = gen_password()
        create_window(password)
    except Exception as e:
        print(f"errro is compiller{str(e)[:50]}")
    return 0

if __name__ == '__main__':
    main()
