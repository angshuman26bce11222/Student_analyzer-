def reverse_list(arr: list) -> list:
    
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def display_leaderboard(students: list):
    
    print("\n" + "="*40)
    print(f"{'ID':<10}{'Name':<15}{'Total Marks':<15}")
    print("="*40)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<15}{s['total']:<15.2f}")
    print("="*40)