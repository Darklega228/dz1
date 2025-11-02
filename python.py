# 1
def count_digits(number: int) -> int:
    return len(str(abs(number)))

# 2
def word_count(text: str):
    import string
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    for word, count in counts.items():
        print(f"{word}: {count}")

# 3
def even_squares(numbers: list[int]) -> list[int]:
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    squares = list(map(lambda x: x ** 2, even_numbers))
    return squares

# 4
def student_grades():
    students = {
        "Іван": [12, 10, 11, 9],
        "Марія": [10, 8, 9, 10],
        "Олег": [7, 9, 8, 6],
        "Анна": [12, 12, 11, 10]
    }

    print("\nСередні бали студентів:")
    averages = {}
    for student, grades in students.items():
        avg = sum(grades) / len(grades)
        averages[student] = avg
        print(f"{student}: {avg:.2f}")

    top_student = max(averages, key=averages.get)
    print(f"\nНайвищий середній бал у студента: {top_student} ({averages[top_student]:.2f})")

# 5
def char_count(text: str) -> dict:
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

# 6
def extract_numbers(data: tuple) -> tuple:
    return tuple(item for item in data if isinstance(item, (int, float)))

# 7
def sort_by_length(strings: list[str]) -> list[str]:
    return sorted(strings, key=len)

# 8
def sort_employees():
    employees = [
        {"ім’я": "Іван", "посада": "Менеджер", "зарплата": 25000},
        {"ім’я": "Марія", "посада": "Розробник", "зарплата": 40000},
        {"ім’я": "Олег", "посада": "Тестувальник", "зарплата": 30000},
        {"ім’я": "Анна", "посада": "Дизайнер", "зарплата": 35000},
    ]

    sorted_list = sorted(employees, key=lambda e: e["зарплата"], reverse=True)
    print("\nСпівробітники за спаданням зарплати:")
    for emp in sorted_list:
        print(f"{emp['ім’я']} - {emp['посада']}: {emp['зарплата']}")
    return sorted_list

# 9
max_of_two = lambda a, b: a if a > b else b

# 10
def unique_elements(lst: list) -> set:
    return set(lst)


if __name__ == "__main__":
    print("1.", count_digits(-12345))
    print("\n2.")
    word_count("Привіт, привіт! Це тестовий рядок, рядок.")
    print("\n3.", even_squares([1, 2, 3, 4, 5, 6]))
    print("\n4.")
    student_grades()
    print("\n5.", char_count("hello world"))
    print("\n6.", extract_numbers(("слово", 42, 3.14, "123", 7)))
    print("\n7.", sort_by_length(["Python", "C", "JavaScript", "Go"]))
    print("\n8.")
    sort_employees()
    print("\n9.", max_of_two(12, 7))
    print("\n10.", unique_elements([1, 2, 2, 3, 4, 4, 5]))