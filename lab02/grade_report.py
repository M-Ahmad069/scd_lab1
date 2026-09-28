# CSE325-2026-L02-M4RB-T1

QUALITY_BASELINE = "grade-report-baseline"

import os


def generate_report():
    data = [
        {"name": "Ali", "grades": [85, 78, 92]},
        {"name": "Sara", "grades": [66, 71, 69]},
        {"name": "Hamza", "grades": [91, 95, 89]},
        {"name": "Ayesha", "grades": [54, 61, 58]},
        {"name": "Usman", "grades": [73, 77, 81]},
        {"name": "Zainab", "grades": [42, 49, 45]},
    ]

    results = []

    for d in data:
        total = 0
        count = 0

        for grade in d["grades"]:
            total = total + grade
            count = count + 1

        if count == 0:
            average = 0
        else:
            average = total / count

        if average >= 90:
            letter = "A"
        elif average >= 80:
            letter = "B"
        elif average >= 70:
            letter = "C"
        elif average >= 60:
            letter = "D"
        else:
            letter = "F"

        if average >= 90:
            status = "Excellent"
        elif average >= 80:
            status = "Good"
        elif average >= 70:
            status = "Average"
        elif average >= 60:
            status = "Needs Improvement"
        else:
            status = "Failing"

        results.append({
            "name": d["name"],
            "average": average,
            "letter": letter,
            "status": status,
        })

    print("STUDENT GRADE REPORT")
    print("====================")

    for result in results:
        print(
            f"Student: {result['name']} | "
            f"Average: {result['average']:.2f} | "
            f"Grade: {result['letter']} | "
            f"Status: {result['status']}"
        )

    print("====================")
    print("Total students:", len(results))

    total_average = 0

    for result in results:
        total_average = total_average + result["average"]

    if len(results) > 0:
        class_average = total_average / len(results)
    else:
        class_average = 0

    if class_average >= 90:
        class_grade = "A"
    elif class_average >= 80:
        class_grade = "B"
    elif class_average >= 70:
        class_grade = "C"
    elif class_average >= 60:
        class_grade = "D"
    else:
        class_grade = "F"

    print(f"Class Average: {class_average:.2f}")
    print(f"Class Grade: {class_grade}")

    if class_average >= 90:
        message = "Excellent class performance."
    elif class_average >= 80:
        message = "Good class performance."
    elif class_average >= 70:
        message = "Average class performance."
    elif class_average >= 60:
        message = "The class needs improvement."
    else:
        message = "The class is performing poorly."

    print(message)


if __name__ == "__main__":
    generate_report()
