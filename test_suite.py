from analytics import compute_summation, find_maximum_score
from models import create_student_record

def run_tests():
    print("Running verification tests...")
    
    # Test 1: Summation
    assert compute_summation([10.0, 20.0, 30.0]) == 60.0, "Summation Test Failed"
    
    # Test 2: Maximum finding
    s1 = create_student_record("1", "Rahul", {})
    s1["total"] = 80.0
    s2 = create_student_record("2", "Mohan", {})
    s2["total"] = 95.0
    
    assert find_maximum_score([s1, s2])["name"] == "Mohan", "Max Score Test Failed"
    
    print("All unit validation tests passed successfully!")

if __name__ == "__main__":
    run_tests()