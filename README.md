
# PDF Text Extraction Application

Access the application here: [PDF Text Extraction](https://pdf-data-extraction.onrender.com)

This project aims to streamline the process of extracting text from PDF documents using Python. It leverages Streamlit for the web interface and PDFMiner for parsing PDF files.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/vallirajasekar/PDF-Data-Extraction-.git
cd PDF-Data-Extraction-
```

### Step 2: Create the Conda Environment

Create a new Conda environment with Python 3.10.

```bash
conda create -p venv python==3.10 -y
```

### Step 3: Activate the Environment

Activate the Conda environment.

```bash
conda activate "/Users/vallirajasekar/Desktop/gemini/Pdf_Information/venv"
```

### Step 4: Install Dependencies

Install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

### Set Up API Key

Make sure to set up your Google Generative AI API key. You can store it in a `.env` file in the root directory of your project:

```plaintext
GOOGLE_API_KEY=your_google_api_key
```

### Run the Streamlit Application

Start the Streamlit application by running:

```bash
streamlit run app.py
```

### Extract Text from PDF

1. Open the Streamlit app in your web browser.
2. Upload a PDF file containing text.
3. Click on the "Submit" button to extract the text from the PDF.

## Description

The PDF Text Extraction application is designed to simplify the process of extracting text from PDF documents. It eliminates the manual effort required for extracting information and enhances accuracy using Python libraries like PDFMiner.

### Key Features:

- **Streamlit Web Interface:** Provides a user-friendly interface for uploading and processing PDF documents.
- **Python PDFMiner Library:** Utilizes PDFMiner for parsing and extracting text content from PDF files.
- **Efficient Text Extraction:** Enables quick extraction of text from PDFs, suitable for various use cases such as data extraction and document processing.

### How It Works:

- **Upload PDF:** Users upload a PDF file through the Streamlit web interface.
- **Text Extraction:** The application processes the uploaded PDF using PDFMiner and displays the extracted text.

## Acknowledgements

This project utilizes the following technologies:

- **Streamlit:** An open-source app framework for building ML and data science applications.
- **PDFMiner:** A Python library for extracting information from PDF documents.

### Notes

- Ensure your environment is configured with the necessary API key from Google Cloud for accessing services.
- This project is intended for educational and experimental purposes.

## Project Structure

```
PDF-Data-Extraction-/
│
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── venv/                 # Conda virtual environment directory
├── .env                  # Environment variables file
├── data/                 # Directory for input PDF files
├── models/               # Directory for storing models (if applicable)
└── .git/                 # Git version control directory
```

## Version Control with Git

This project uses Git for version control. Below are some basic commands to get you started:

1. Initialize a new Git repository:

   ```bash
   git init
   ```

2. Add files to the staging area:

   ```bash
   git add .
   ```

3. Commit changes:

   ```bash
   git commit -m "Initial commit"
   ```

4. Add a remote repository:

   ```bash
   git remote add origin <remote_repository_URL>
   ```

5. Push changes to the remote repository:

   ```bash
   git push -u origin master
   ```

## !!! Thank You !!! Visit Us Again :)

---

