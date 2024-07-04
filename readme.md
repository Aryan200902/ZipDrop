# ZipDrop

ZipDrop is a simple web application built using Django Rest Framework (DRF) and Python's shutil module. It allows users to upload files, which are then zipped into a single file for easy downloading.

## Features

- **File Upload**: Users can upload multiple files at once.
- **Zip Generation**: Uploaded files are automatically zipped into a single file.
- **Download Link**: After uploading, users are provided with a link to download the generated zip file.

## Installation

To run ZipDrop locally, follow these steps:

1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/Aryan200902/Zipdrop.git
    cd zipdrop
    ```
2. Install Python (if not already installed).
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    - On Windows: 
        ```bash
        env\Scripts\activate
        ```
    - On macOS and Linux: 
        ```bash
        source env/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
8. Visit `http://localhost:8000` in your web browser to access ZipDrop.

## Usage

1. Visit the ZipDrop web application.
2. Click on the "Upload File" button to select files for upload.
3. Once files are uploaded, a download link will be provided.
4. Click the download link to download the generated zip file.

