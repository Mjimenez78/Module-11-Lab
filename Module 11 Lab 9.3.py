import csv

def main():
    # Open the CSV file in write mode and create a CSV writer
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Continue adding student records until the user chooses to stop
        while True:
            first_name = input("Enter the student's first name (or press Enter to finish): ")
            if first_name == "":
                break
            last_name = input("Enter the student's last name: ")
            exam1 = int(input("Enter the student's exam 1 grade: "))
            exam2 = int(input("Enter the student's exam 2 grade: "))
            exam3 = int(input("Enter the student's exam 3 grade: "))
            
            # Write the student record to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])
            
            print("Record added successfully.")

if __name__ == "__main__":
    main()
