class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        print()
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


def show_menu():
    print("=" * 40)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def read_menu_choice():
    while True:
        text = input("선택: ").strip()

        if text == "":
            print("⚠️ 입력이 비어 있습니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        if number < 1 or number > 5:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        return number


def main():
    try:
        while True:
            show_menu()
            choice = read_menu_choice()

            if choice == 5:
                print("👋 프로그램을 종료합니다.")
                break

            print(f"({choice}번 기능은 아직 준비 중입니다.)")
            print()
    except (KeyboardInterrupt, EOFError):
        print()
        print("👋 입력이 중단되어 안전하게 종료합니다.")


main()