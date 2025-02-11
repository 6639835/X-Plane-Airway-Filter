# X-Plane-Airway-Filter
A tool to remove specific rows from dat files, particularly for handling data related to regions within China.

## Features

- Read and parse DAT files
- Remove rows that meet specific conditions
- Support custom China region judgment
- Exception handling for stable program execution
- Efficient processing of large files

## Usage Instructions

### 1. Installation and Configuration

- Ensure Python 3.x is installed on your system
- Download the code to your local directory
- Configure the input and output file paths

### 2. Running the Program

```bash
python main.py
```

### 3. Input and Output

- Input File: The original DAT file
- Output File: The processed DAT file meeting the requirements

### 4. Output Results

After processing, the program will output the following messages:
- If successful: `Processing completed! Rows meeting the conditions have been removed, and the results are saved in output.dat.`
- If file not found: `File not found. Please check if the input file path is correct.`
- If other errors occur: `An error occurred: [Error message]`

### 5. Code Explanation

- `china_areas`: Define the list for judging regions within China
- `input_file`: Set the input file path
- `output_file`: Set the output file path
- Read the input file and process each line
- Remove lines that meet specific conditions
- Write the processed lines to the output file

### 6. Precautions

- Ensure the input file path is correct
- Ensure the output file path has write permissions
- Ensure sufficient memory for processing large files
- Verify the output file is correct after processing

### 7. Extension and Contribution

- You can modify the `china_areas` list as needed
- You can adjust the input and output file paths
- Welcome to submit Pull Requests to improve the code together
