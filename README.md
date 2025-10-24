# Python Lab 11 Solution

This repository contains solutions for Python Lab 11, demonstrating various string manipulation, data sorting, and set operations.

## 📁 Project Structure

```
2025204005/
├── lab11_solution.py    # Main solution file
├── results.txt          # Output file (generated when script runs)
└── README.md           # This file
```

## 🎯 Overview

This Python script implements three main functions that demonstrate fundamental programming concepts:

1. **String Scrambling**: Manipulates strings by splitting and reversing parts
2. **Course Sorting**: Sorts course data by enrollment numbers
3. **Set Operations**: Performs mathematical set operations on club memberships

## 🔧 Functions

### 1. `scramble_string(s)`
**Purpose**: Scrambles a string by finding the midpoint, keeping the first half unchanged, and reversing the second half.

**Algorithm**:
- If string is empty, return as-is
- Find midpoint using `(length + 1) // 2`
- Split string into two parts at midpoint
- Reverse the second part
- Concatenate first part + reversed second part

**Example**:
```python
scramble_string("AUTOMATION")  # Returns: "AUTOMNOITA"
```

### 2. `sort_courses(cl)`
**Purpose**: Sorts a list of course tuples by enrollment numbers in descending order.

**Input**: List of tuples `(course_code, enrollment_count)`
**Output**: Sorted list by enrollment count (highest first)

**Example**:
```python
courses = [('CS101', 50), ('MA202', 35), ('EE301', 45), ('PY451', 30)]
sort_courses(courses)  # Returns: [('CS101', 50), ('EE301', 45), ('MA202', 35), ('PY451', 30)]
```

### 3. `club_set_operations(rc, ac)`
**Purpose**: Performs set operations on two club membership lists and creates a student-club mapping.

**Operations Performed**:
- **Intersection**: Students in both clubs
- **Union**: Students in either club
- **Difference**: Students only in robotics club
- **Student Dictionary**: Maps each student to their club memberships

**Input**: Two lists of club members (with potential whitespace)
**Output**: Dictionary containing all set operations and student mappings

## 📊 Output

The script generates both console output and a `results.txt` file containing:

```
--- SCRABBLED STRING ---
AUTOMNOITA

--- SORTED COURSES ---
[('CS101', 50), ('EE301', 45), ('MA202', 35), ('PY451', 30)]

--- SET OPERATIONS ---
Intersection: ['Aditi', 'Priya', 'Rohan']
Union: ['Aditi', 'Kunal', 'Neha', 'Priya', 'Rohan', 'Sameer', 'Vikram']
Difference: ['Kunal', 'Vikram']

--- STUDENT DICTIONARY ---
{'Aditi': ['AI', 'Robotics'], 'Kunal': ['Robotics'], 'Neha': ['AI'], 'Priya': ['AI', 'Robotics'], 'Rohan': ['AI', 'Robotics'], 'Sameer': ['AI'], 'Vikram': ['Robotics']}
```

## 🚀 Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Script

1. **Navigate to the project directory**:
   ```bash
   cd /path/to/2025204005/
   ```

2. **Run the script**:
   ```bash
   python lab11_solution.py
   ```

3. **Check the output**:
   - Results will be displayed in the console
   - A `results.txt` file will be created in the same directory

### Running from Any Directory

The script uses absolute paths, so you can run it from any location:

```bash
python /path/to/2025204005/lab11_solution.py
```

The `results.txt` file will always be created in the same directory as the script.

## 🔍 Key Features

- **Robust File Handling**: Uses absolute paths to ensure `results.txt` is created in the correct location
- **Data Sanitization**: Strips whitespace from club member names
- **Sorted Output**: All set operations and dictionaries are sorted for consistent results
- **Dual Output**: Results displayed both in console and saved to file

## 🧪 Test Data

The script uses the following test data:

- **String**: "AUTOMATION"
- **Courses**: CS101 (50), MA202 (35), EE301 (45), PY451 (30)
- **Robotics Club**: Kunal, Aditi, Rohan, Priya, Vikram
- **AI Club**: Priya, Sameer, Aditi, Neha, Rohan

## 📝 Notes

- The script automatically handles whitespace in member names
- Set operations maintain alphabetical order in output
- The student dictionary shows club memberships in alphabetical order
- File paths are resolved relative to the script location for portability

## 🤝 Contributing

This is a lab assignment solution. Feel free to study the code and adapt it for educational purposes.

## 📄 License

This project is for educational purposes as part of Python Lab coursework.
