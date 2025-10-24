def scramble_string(s):
    if not s:
        return s
    l = len(s)
    midpoint = (l + 1) // 2
    x = s[:midpoint]
    y = s[midpoint:]
    z = y[::-1]
    return x + z


def sort_courses(cl):
    return sorted(cl, key=lambda course: course[1], reverse=True)


def club_set_operations(rc, ac):
    r = {member.strip() for member in rc}
    a = {member.strip() for member in ac}
    intersection = r & a  
    union = r | a         
    difference = r - a    
    
    student_clubs = {}
    
    for member in r:
        student_clubs[member] = ['Robotics']
    
    for member in a:
        if member in student_clubs:
            student_clubs[member].append('AI')
        else:
            student_clubs[member] = ['AI']
    
    for student in student_clubs:
        student_clubs[student].sort()
    
    return {
        'intersection': intersection,
        'union': union,
        'difference': difference,
        'student_clubs': student_clubs
    }

if __name__ == "__main__":
    import os
    if os.path.exists("results.txt"):
        open("results.txt", "w").close()
        
        
    scrambled_result = scramble_string("AUTOMATION")

    courses = [('CS101', 50), ('MA202', 35), ('EE301', 45), ('PY451', 30)]
    sorted_courses = sort_courses(courses)
    

    robotics_club = [" Kunal ", " Aditi ", " Rohan ", " Priya ", " Vikram "]
    ai_club = [" Priya ", " Sameer ", " Aditi ", " Neha ", " Rohan "]
    club_results = club_set_operations(robotics_club, ai_club)
    

    with open("results.txt", "w") as file:
        file.write("--- SCRABBLED STRING ---\n")
        file.write(f"{scrambled_result}\n")
        
        file.write("--- SORTED COURSES ---\n")
        file.write(f"{sorted_courses}\n")
        
        file.write("--- SET OPERATIONS ---\n")
        file.write(f"Intersection: {sorted(list(club_results['intersection']))}\n")
        file.write(f"Union: {sorted(list(club_results['union']))}\n")
        file.write(f"Difference: {sorted(list(club_results['difference']))}\n")
        
        file.write("--- STUDENT DICTIONARY ---\n")
        file.write(f"{dict(sorted(club_results['student_clubs'].items()))}\n")
        
        
    print("--- SCRABBLED STRING ---")
    print(scrambled_result)
    print("--- SORTED COURSES ---")
    print(sorted_courses)
    print("--- SET OPERATIONS ---")
    print(f"Intersection: {sorted(list(club_results['intersection']))}")
    print(f"Union: {sorted(list(club_results['union']))}")
    print(f"Difference: {sorted(list(club_results['difference']))}")
    print("--- STUDENT DICTIONARY ---")
    print(dict(sorted(club_results['student_clubs'].items())))
