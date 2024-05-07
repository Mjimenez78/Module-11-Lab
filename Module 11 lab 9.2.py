def main():
    # Read grades from the file
    with open("grades.txt", "r") as file:
        grades = [float(line.strip()) for line in file.readlines()]

    # Display individual grades
    print("Individual Grades:")
    for grade in grades:
        print(grade)

    # Calculate total, count, and average
    total = sum(grades)
    count = len(grades)
    average = total / count if count > 0 else 0

    # Display total, count, and average
    print("\nTotal:", total)
    print("Count:", count)
    print("Average:", average)

if __name__ == "__main__":
    main()
