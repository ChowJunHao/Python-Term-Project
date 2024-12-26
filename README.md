# Interactive Periodic Table

An interactive periodic table application built using Python and Tkinter. This tool provides a visual representation of the periodic table and allows users to view detailed information about each element. It includes features such as search functionality, a pop-up details window, and filtering of element properties.

## Features

1. **Visual Periodic Table**
   - Displays all 118 elements with their symbols and atomic numbers.
   - Elements are color-coded based on their category (e.g., Non-metal, Alkali Metal).

2. **Element Details**
   - Hover over an element to view a tooltip with selected properties.
   - Click on an element to open a pop-up window displaying detailed information in a tabular format.

3. **Search Functionality**
   - Search for elements by name, symbol, or atomic number.
   - Displays search results in a scrollable window for quick navigation.

4. **Property Filtering**
   - Customize which properties are displayed in tooltips by selecting them from a scrollable list.

5. **Superscript Atomic Numbers**
   - Element symbols are displayed with their atomic numbers as superscripts.

6. **Scrollable and Neat Layout**
   - Scrollbars ensure usability even with large amounts of content.
   - Labels and frames organize the layout for better visual clarity.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required libraries (Tkinter is included with Python by default).
3. Download the script files `Interactive Periodic Table.py` and `Data.py`.
4. Run the script:

   ```bash
   python "Interactive Periodic Table.py"
   ```

## Usage

1. Launch the application by running the Python script.
2. Hover over elements to view their selected properties.
3. Click on elements to view detailed information in a pop-up window.
4. Use the search bar to locate specific elements by name, symbol, or atomic number.
5. Customize the properties displayed in the tooltip by selecting them from the scrollable list on the left panel.

## Program Architecture

The project is organized as follows:

```bash
Interactive_Periodic_Table/
├── Data.py            # Contains all element data in dictionary format
├── Interactive_Periodic_Table.py  # Main script to run the application
└── README.md          # Documentation
```

### Core Components

- **Data.py**: Contains the data for all 118 elements in a structured dictionary format.
- **Interactive_Periodic_Table.py**: Main script that handles the UI and interactions.

## Development Process

The development of the Interactive Periodic Table followed these steps:

1. **Data Collection**: Collected detailed information about all 118 elements from reliable sources.
2. **Data Structuring**: Converted the data into a structured dictionary format and saved it in `Data.py`.
3. **UI Development**: Built the user interface using Tkinter, ensuring all elements were displayed correctly.
4. **Feature Development**: Added features like tooltips, search functionality, and popups for element details.
5. **Enhancements**: Improved the layout and made the application more interactive with user inputs.

## Enhancements and Contributions

The following modifications and enhancements were added to the project:

### Reference Features Integrated:

- Search function that allows users to search by symbol, name, or atomic number.
- Color-coded periodic table to visually differentiate element categories.

### Unique Contributions:

- Developed an interactive, scrollable periodic table.
- Implemented a popup window to display detailed element properties.
- Added hover-over tooltips to display quick details about elements.
- Designed an intuitive search function that updates the table dynamically.

## Contribution

Feel free to contribute to this project by suggesting new features, improving the code, or fixing bugs. Fork the repository, make your changes, and submit a pull request.

## References

1. This project was developed with the assistance of ChatGPT, which provided guidance and solutions for implementing various features. You can find the link to the original conversation with ChatGPT below:

   - [Interactive Periodic Table Python](https://chatgpt.com/share/675823de-9fe0-8002-b07e-317248a4817f)
   - [Interactive Periodic Table Python 2](https://chatgpt.com/share/676abdc9-169c-8002-9a78-808ae5e895ef)
   - [Interactive Periodic Table Python 3](https://chatgpt.com/share/676abe00-1d6c-8002-babd-d40e79e299c3)

---

Thank you for using the Interactive Periodic Table!

