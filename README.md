# X-Plane Airway Filter: Declutter Your Navigation Data! 🗺️ ✂️

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) [![X-Plane](https://img.shields.io/badge/X--Plane-Ready-green.svg)](https://www.x-plane.com/) [![Data Filtering](https://img.shields.io/badge/Data-Filtering-yellow.svg)](https://en.wikipedia.org/wiki/Data_cleansing) [![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE) [![GitHub Stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/X-Plane-Airway-Filter?style=social)](https://github.com/YOUR_GITHUB_USERNAME/X-Plane-Airway-Filter)

Clean up your X-Plane navigation data with this handy Python tool!  Designed to remove specific rows from DAT files, particularly for filtering data related to specific regions (e.g., within China). Improve your X-Plane experience by focusing on the areas you fly in most!

**Eliminate Unwanted Navigation Data and Simplify Your X-Plane World!**

**Important:** Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username in the GitHub Stars badge link.

---

## ✨ Key Features

*   **DAT File Parsing:** Reads and efficiently parses large DAT files.
*   **Selective Row Removal:** Removes rows that meet your specified conditions.
*   **Customizable Region Filtering:** Supports custom region judgment, ideal for tailoring your data to specific geographic areas.
*   **Robust Error Handling:** Includes exception handling to ensure stable program execution.
*   **Efficient Processing:** Designed for efficient processing of large navigation data files.
*   **Simplified Navigation:** Focus on the regions you fly in the most!

---

## 🚀 Usage Instructions

### 1. Installation and Configuration

*   Ensure Python 3.x is installed on your system. Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   Download the code to your local directory.
*   Configure the input and output file paths within the script.

### 2. Running the Program

Open your terminal or command prompt, navigate to the directory containing the script, and run:

```bash
python main.py
```

### 3. Input and Output Files

*   **Input File:** The original DAT file you want to filter.
*   **Output File:** The processed DAT file with the unwanted rows removed.

### 4. Understanding the Output

After processing, the program will display one of the following messages:

*   **Success:** `Processing completed! Rows meeting the conditions have been removed, and the results are saved in output.dat.`
*   **File Not Found:** `File not found. Please check if the input file path is correct.`
*   **Error:** `An error occurred: [Error message]`

### 5. Code Overview

*   `china_areas`: This list defines the regions within China that will be used for filtering.  Customize this list to match your specific needs.
*   `input_file`:  Set the path to your input DAT file here.
*   `output_file`:  Set the path where the filtered DAT file will be saved.

The script reads the input file line by line, checks if each line meets the specified filtering conditions (based on `china_areas`), and writes the lines that *do not* meet the conditions to the output file.

### 6. Important Precautions

*   **Verify Input Path:** Double-check that the input file path is correct.
*   **Write Permissions:** Ensure the output file path has write permissions.
*   **Memory Considerations:** Ensure you have sufficient memory available for processing large files.
*   **Validate Output:** Always verify that the output file is correct after processing.

### 7. Extending and Contributing

*   **Customize Filtering:** Modify the `china_areas` list to filter data based on other regions or criteria.
*   **Adjust File Paths:** Easily change the input and output file paths within the script.
*   **Contribute to the Project:** Submit Pull Requests to improve the code and add new features!

---

## 🤝 Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request.

[![RepoBeats](https://repobeats.axiom.co/api/embed/56889020667fd946242b9730dbc85c6fabbd9516.svg)](https://repobeats.axiom.co/)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Simplify Your X-Plane Navigation Data Today!  Happy Flying!**
