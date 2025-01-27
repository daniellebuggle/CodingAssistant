exercise_to_badge = {
    "CompareIntegers": "Java If-Else",
    "FactorialCalculator": "Java While-Loop",
    "PowerCalculator": "Java Do-While",
    "SumOfNumbers": "Java For-Loop",
    "VowelCheck": "Java OR Operator",
    "calculate_factorial": "Python While-Loop",
    "calculate_sum": "Python For-Loop",
    "compare_integers": "Python If-Elif",
    "is_vowel": "Python OR Operator"
}


def check_badge(exercise_name):
    return exercise_to_badge.get(exercise_name, "Badge not found")
