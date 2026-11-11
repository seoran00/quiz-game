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


def create_default_quizzes():
    return [
        Quiz(
            "Python의 창시자는?",
            ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],
            1,
        ),
        Quiz(
            "Python에서 화면에 글자를 출력하는 함수는?",
            ["echo()", "print()", "write()", "show()"],
            2,
        ),
        Quiz(
            "Python에서 정수를 나타내는 자료형은?",
            ["str", "bool", "int", "list"],
            3,
        ),
        Quiz(
            "Python에서 여러 값을 순서대로 담는 자료형은?",
            ["list", "int", "bool", "float"],
            1,
        ),
        Quiz(
            "Python에서 함수를 만들 때 사용하는 키워드는?",
            ["function", "func", "make", "def"],
            4,
        ),
    ]


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


def read_number(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()

        if text == "":
            print(f"⚠️ 입력이 비어 있습니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
            continue

        if number < minimum or number > maximum:
            print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
            continue

        return number


def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
        return None

    total = len(quizzes)
    correct_count = 0

    print()
    print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")

    for number, quiz in enumerate(quizzes, start=1):
        print()
        print("-" * 40)
        print(f"[문제 {number}]")
        quiz.display()
        print()

        user_answer = read_number("정답 입력: ", 1, 4)

        if quiz.is_correct(user_answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

    score = correct_count * 100 // total

    print()
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)

    return correct_count


def main():
    quizzes = create_default_quizzes()

    try:
        while True:
            show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                play_quiz(quizzes)
                print()
            elif choice == 5:
                print("👋 프로그램을 종료합니다.")
                break
            else:
                print(f"({choice}번 기능은 아직 준비 중입니다.)")
                print()
    except (KeyboardInterrupt, EOFError):
        print()
        print("👋 입력이 중단되어 안전하게 종료합니다.")


main()