from student_manager import StudentManager
from models import create_student_record
from analytics import compute_summation, find_maximum_score, find_kth_smallest
from reports import reverse_list, display_leaderboard
from validators import validate_score

def main():
    manager = StudentManager()
    
    while True:
        print("\n--- Student Performance & Ranking Analyzer ---")
        print("1. Add Student Record")
        print("2. Calculate Totals & Display Leaderboard")
        print("3. Find Top Scorer (Max Algorithm)")
        print("4. Find K-th Smallest Score")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            m_score = validate_score(input("Enter Math Score: "))
            p_score = validate_score(input("Enter Python Score: "))
            e_score = validate_score(input("Enter English Score: "))
            
            if m_score != -1.0 and p_score != -1.0 and e_score != -1.0:
                scores = {"Math": m_score, "Python": p_score, "English": e_score}
                rec = create_student_record(sid, name, scores)
                rec["total"] = compute_summation([m_score, p_score, e_score])
                rec["average"] = rec["total"] / 3
                
                if manager.add_student(rec):
                    print("Student added successfully")
                    
        elif choice == "2":
            display_leaderboard(manager.students)
            
        elif choice == "3":
            top_student = find_maximum_score(manager.students)
            if top_student:
                print(f"\nTop Student: {top_student['name']} with {top_student['total']} marks.")
            else:
                print("No records available.")
                
        elif choice == "4":
            k = int(input("Enter K value: "))
            kth = find_kth_smallest(manager.students, k)
            if kth:
                print(f"The {k}-th lowest performing student is {kth['name']} with {kth['total']} marks.")
                
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()