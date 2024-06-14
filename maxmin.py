def mini(a):
    min_val=None
    for val in a:

        if min_val==None or min_val >val:
            min_val=val
        return min_val

def maximum(a):
    max_val = None
    for val in a:

        if max_val == None or max_val < val:
            max_val = val
        return max_val

def main():
    a = input("Enter the elements separated by commas: ").split(",")
    print("maximum element is",max(a))
    print("minimum element is", min(a))
main()