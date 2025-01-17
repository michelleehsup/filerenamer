# FileRenamer

FileRenamer is a Python program designed to provide batch renaming capabilities for files and folders on Windows, enhancing organization and management efficiency.

## Features

- Batch rename files with a specified prefix and sequence number.
- Optionally include folders in the renaming process.
- Define the starting number for the renaming sequence.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository or download the `FileRenamer.py` file.

## Usage

Navigate to the directory where `FileRenamer.py` is located and run the following command in the terminal:

```bash
python FileRenamer.py <directory> <prefix> [-s START] [-f]
```

- `<directory>`: The directory containing files to rename.
- `<prefix>`: The prefix for the renamed files.
- `-s, --start`: (Optional) The starting number for the renaming sequence (default is 1).
- `-f, --folders`: (Optional) Include folders in the renaming process.

### Example

To rename files in the `C:\Documents` directory with a prefix of `Document` starting from number 10, and including folders:

```bash
python FileRenamer.py "C:\Documents" Document -s 10 -f
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.