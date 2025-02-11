import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import re
from tqdm import tqdm
import os


def search_earth_fix(waypoint, filepath):
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 5 and parts[2] == waypoint and parts[4] in ["ZB", "ZG", "ZS", "ZH", "ZJ", "ZU", "ZY", "ZW",
                                                                        "ZP", "ZL"] and parts[3] == "ENRT":
                return parts[4]
    return None


def search_earth_nav(waypoint, filepath, code_type):
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 10 and parts[7] == waypoint and parts[8] == "ENRT" and parts[9] in ["ZB", "ZG", "ZS", "ZH",
                                                                                                "ZJ", "ZU", "ZY", "ZW",
                                                                                                "ZP", "ZL"]:
                return parts[9]
    return None


def sort_key(line):
    last_part = line.split()[-1]
    match = re.match(r"([A-Z]+)(\d*)$", last_part)
    if match:
        letters, numbers = match.groups()
        numbers = int(numbers) if numbers else 0
        return (letters, numbers)
    return (last_part, float('inf'))


def convert_csv_to_dat(csv_file, earth_fix_path, earth_nav_path, output_file, status_label=None):
    try:
        output_lines = []
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            total_rows = sum(1 for _ in reader)
            csvfile.seek(0)
            next(reader)  # skip header

            for row in tqdm(reader, total=total_rows, desc="Processing Rows"):
                first_part = row['CODE_POINT_START']
                third_part = '11' if row['CODE_TYPE_START'] == 'DESIGNATED_POINT' else '3' if row[
                                                                                                  'CODE_TYPE_START'] == 'VORDME' else '2'

                if third_part == '11':
                    second_part = search_earth_fix(first_part, earth_fix_path)
                else:
                    second_part = search_earth_nav(first_part, earth_nav_path, third_part)

                if not second_part:
                    print(f"Warning: No area code found for {first_part}. Skipping row.")
                    continue

                fourth_part = row['CODE_POINT_END']
                sixth_part = '11' if row['CODE_TYPE_END'] == 'DESIGNATED_POINT' else '3' if row[
                                                                                                'CODE_TYPE_END'] == 'VORDME' else '2'

                if sixth_part == '11':
                    fifth_part = search_earth_fix(fourth_part, earth_fix_path)
                else:
                    fifth_part = search_earth_nav(fourth_part, earth_nav_path, sixth_part)

                if not fifth_part:
                    print(f"Warning: No area code found for {fourth_part}. Skipping row.")
                    continue

                seventh_part = 'N' if row['CODE_DIR'] == 'X' else row['CODE_DIR']
                ninth_part = '0'
                tenth_part = '600'
                eleventh_part = row['TXT_DESIG']

                for i in range(1, 3):  # generate two records (parts 1 and 2)
                    eighth_part = str(i)
                    part1 = f"{first_part:>5}"
                    part2 = f"{second_part:>3}"
                    part3 = f"{third_part:>3}"
                    part4 = f"{fourth_part:>6}"
                    part5 = f"{fifth_part:>3}"
                    part6 = f"{sixth_part:>3}"
                    part7 = f"{seventh_part:>2}"
                    part8 = f"{eighth_part:>2}"
                    part9 = f"{ninth_part:>4}"
                    part10 = f"{tenth_part:>4}"
                    part11 = f" {eleventh_part}"
                    dat_line = f"{part1}{part2}{part3}{part4}{part5}{part6}{part7}{part8}{part9}{part10}{part11}\n"
                    output_lines.append(dat_line)

        output_lines.sort(key=sort_key)
        with open(output_file, 'w') as datfile:
            datfile.writelines(output_lines)

        if status_label:
            status_label.config(text="Processing completed!")
        print("Processing completed!")
    except Exception as e:
        if status_label:
            status_label.config(text=f"Error: {e}")
        print(f"Error: {e}")


def browse_file(entry_field):
    filename = filedialog.askopenfilename()
    if filename:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, filename)


def browse_output_file(entry_field):
    filename = filedialog.asksaveasfilename(defaultextension=".dat")
    if filename:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, filename)


def run_conversion(csv_entry, earth_fix_entry, earth_nav_entry, output_entry, status_label):
    csv_file = csv_entry.get()
    earth_fix_file = earth_fix_entry.get()
    earth_nav_file = earth_nav_entry.get()
    output_file = output_entry.get()

    if not all([csv_file, earth_fix_file, earth_nav_file, output_file]):
        messagebox.showwarning("Warning", "Please select all required files before running the conversion.")
        return

    if not os.path.isfile(csv_file) or not os.path.isfile(earth_fix_file) or not os.path.isfile(earth_nav_file):
        messagebox.showwarning("Warning", "One or more input files are not valid. Please check your selections.")
        return

    status_label.config(text="Processing...")
    convert_csv_to_dat(csv_file, earth_fix_file, earth_nav_file, output_file, status_label)


# Simple Tkinter UI
def main():
    root = tk.Tk()
    root.title("CSV to .dat Converter")

    # CSV File
    tk.Label(root, text="CSV File:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    csv_entry = tk.Entry(root, width=60)
    csv_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(csv_entry)).grid(row=0, column=2, padx=5, pady=5)

    # Earth Fix Path
    tk.Label(root, text="Earth Fix File:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    earth_fix_entry = tk.Entry(root, width=60)
    earth_fix_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(earth_fix_entry)).grid(row=1, column=2, padx=5, pady=5)

    # Earth Nav Path
    tk.Label(root, text="Earth Nav File:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    earth_nav_entry = tk.Entry(root, width=60)
    earth_nav_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(earth_nav_entry)).grid(row=2, column=2, padx=5, pady=5)

    # Output File
    tk.Label(root, text="Output .dat File:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    output_entry = tk.Entry(root, width=60)
    output_entry.grid(row=3, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_output_file(output_entry)).grid(row=3, column=2, padx=5,
                                                                                          pady=5)

    # Status Label
    status_label = tk.Label(root, text="", fg="green")
    status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

    # Convert Button
    convert_button = tk.Button(
        root,
        text="Convert CSV",
        command=lambda: run_conversion(csv_entry, earth_fix_entry, earth_nav_entry, output_entry, status_label)
    )
    convert_button.grid(row=4, column=1, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()