def main():
    # Open the file in append mode, or create a new one if it doesn't exist
    with open("grades.txt", "a") as file:
        # Continue adding grades until the user enters an empty line
        while True:
            grade_input = input("Enter a grade (or press Enter to finish): ")
            if grade_input == "":
                break
            try:
                grade = float(grade_input)
                # Write the grade to the file
                file.write(str(grade) + "\n")
            except ValueError:
                print("Invalid input. Please enter a valid grade.")

if __name__ == "__main__":
    main()
