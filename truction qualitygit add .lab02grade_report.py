[1mdiff --git a/lab02/grade_report.py b/lab02/grade_report.py[m
[1mnew file mode 100644[m
[1mindex 0000000..63456fe[m
[1m--- /dev/null[m
[1m+++ b/lab02/grade_report.py[m
[36m@@ -0,0 +1,115 @@[m
[32m+[m[32m# CSE325-2026-L02-M4RB-T1[m
[32m+[m
[32m+[m[32mQUALITY_BASELINE = "grade-report-baseline"[m
[32m+[m
[32m+[m[32mimport os[m
[32m+[m
[32m+[m
[32m+[m[32mdef generate_report():[m
[32m+[m[32m    data = [[m
[32m+[m[32m        {"name": "Ali", "grades": [85, 78, 92]},[m
[32m+[m[32m        {"name": "Sara", "grades": [66, 71, 69]},[m
[32m+[m[32m        {"name": "Hamza", "grades": [91, 95, 89]},[m
[32m+[m[32m        {"name": "Ayesha", "grades": [54, 61, 58]},[m
[32m+[m[32m        {"name": "Usman", "grades": [73, 77, 81]},[m
[32m+[m[32m        {"name": "Zainab", "grades": [42, 49, 45]},[m
[32m+[m[32m    ][m
[32m+[m
[32m+[m[32m    results = [][m
[32m+[m
[32m+[m[32m    for d in data:[m
[32m+[m[32m        total = 0[m
[32m+[m[32m        count = 0[m
[32m+[m
[32m+[m[32m        for grade in d["grades"]:[m
[32m+[m[32m            total = total + grade[m
[32m+[m[32m            count = count + 1[m
[32m+[m
[32m+[m[32m        if count == 0:[m
[32m+[m[32m            average = 0[m
[32m+[m[32m        else:[m
[32m+[m[32m            average = total / count[m
[32m+[m
[32m+[m[32m        if average >= 90:[m
[32m+[m[32m            letter = "A"[m
[32m+[m[32m        elif average >= 80:[m
[32m+[m[32m            letter = "B"[m
[32m+[m[32m        elif average >= 70:[m
[32m+[m[32m            letter = "C"[m
[32m+[m[32m        elif average >= 60:[m
[32m+[m[32m            letter = "D"[m
[32m+[m[32m        else:[m
[32m+[m[32m            letter = "F"[m
[32m+[m
[32m+[m[32m        if average >= 90:[m
[32m+[m[32m            status = "Excellent"[m
[32m+[m[32m        elif average >= 80:[m
[32m+[m[32m            status = "Good"[m
[32m+[m[32m        elif average >= 70:[m
[32m+[m[32m            status = "Average"[m
[32m+[m[32m        elif average >= 60:[m
[32m+[m[32m            status = "Needs Improvement"[m
[32m+[m[32m        else:[m
[32m+[m[32m            status = "Failing"[m
[32m+[m
[32m+[m[32m        results.append({[m
[32m+[m[32m            "name": d["name"],[m
[32m+[m[32m            "average": average,[m
[32m+[m[32m            "letter": letter,[m
[32m+[m[32m            "status": status,[m
[32m+[m[32m        })[m
[32m+[m
[32m+[m[32m    print("STUDENT GRADE REPORT")[m
[32m+[m[32m    print("====================")[m
[32m+[m
[32m+[m[32m    for result in results:[m
[32m+[m[32m        print([m
[32m+[m[32m            f"Student: {result['name']} | "[m
[32m+[m[32m            f"Average: {result['average']:.2f} | "[m
[32m+[m[32m            f"Grade: {result['letter']} | "[m
[32m+[m[32m            f"Status: {result['status']}"[m
[32m+[m[32m        )[m
[32m+[m
[32m+[m[32m    print("====================")[m
[32m+[m[32m    print("Total students:", len(results))[m
[32m+[m
[32m+[m[32m    total_average = 0[m
[32m+[m
[32m+[m[32m    for result in results:[m
[32m+[m[32m        total_average = total_average + result["average"][m
[32m+[m
[32m+[m[32m    if len(results) > 0:[m
[32m+[m[32m        class_average = total_average / len(results)[m
[32m+[m[32m    else:[m
[32m+[m[32m        class_average = 0[m
[32m+[m
[32m+[m[32m    if class_average >= 90:[m
[32m+[m[32m        class_grade = "A"[m
[32m+[m[32m    elif class_average >= 80:[m
[32m+[m[32m        class_grade = "B"[m
[32m+[m[32m    elif class_average >= 70:[m
[32m+[m[32m        class_grade = "C"[m
[32m+[m[32m    elif class_average >= 60:[m
[32m+[m[32m        class_grade = "D"[m
[32m+[m[32m    else:[m
[32m+[m[32m        class_grade = "F"[m
[32m+[m
[32m+[m[32m    print(f"Class Average: {class_average:.2f}")[m
[32m+[m[32m    print(f"Class Grade: {class_grade}")[m
[32m+[m
[32m+[m[32m    if class_average >= 90:[m
[32m+[m[32m        message = "Excellent class performance."[m
[32m+[m[32m    elif class_average >= 80:[m
[32m+[m[32m        message = "Good class performance."[m
[32m+[m[32m    elif class_average >= 70:[m
[32m+[m[32m        message = "Average class performance."[m
[32m+[m[32m    elif class_average >= 60:[m
[32m+[m[32m        message = "The class needs improvement."[m
[32m+[m[32m    else:[m
[32m+[m[32m        message = "The class is performing poorly."[m
[32m+[m
[32m+[m[32m    print(message)[m
[32m+[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    generate_report()[m
\ No newline at end of file[m
