def evaluate_result(got_score,total_score=100):
    pctg=round((got_score/total_score)*100,2)
    if pctg >=90 : grade ="A+"
    elif pctg >= 80: grade = "A"
    elif pctg >= 70: grade = "B"
    elif pctg >= 60: grade = "C"
    elif pctg >= 40: grade = "D"
    else:  grade = "F"

    status="Pass" if pctg>=40 else "Fail"
    return pctg,grade,status


percentage,grade,status=evaluate_result(92,100)

print(f"Marks: 82/100 | {percentage}% | Grade: {grade} | {status}")

if status == "Pass" and grade in ("A+", "A"):
    print("🏅 Eligible for merit scholarship!")

