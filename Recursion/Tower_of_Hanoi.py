def tower_of_hanoi(n, source, helper, destination):
    """
    Parameters:
    n (int): Number of disks
    source (str): The source rod
    helper (str): The auxiliary rod
    destination (str): The target rod
    """
    # Base Case: If only one disk, move it directly
    if n == 1:
        print(f"Move disk 1 from {source} -> {destination}")
        return
    # Step 1: Move n-1 disks from source to helper using destination
    tower_of_hanoi(n - 1, source, destination, helper)
    # Step 2: Move the nth (largest) disk from source to destination
    print(f"Move disk {n} from {source} -> {destination}")
    # Step 3: Move n-1 disks from helper to destination using source
    tower_of_hanoi(n - 1, helper, source, destination)
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
 

'''
Time Complexity (TC)
    Recurrence relation:
        T(n) = 2T(n-1) + 1
    Final Complexity:
        T(n) = O(2^n)  Reason: Each disk doubles the number of operations.
        
Space Complexity (SC)
   Due to recursion stack:O(n)
👉 Maximum depth of recursive calls = number of disks'''