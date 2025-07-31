# Python Pandas Application

This project is a simple Python application that uses the pandas library to load and visualize a dataset.

## Project Structure

```
python-pandas-app
├── src
│   └── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Requirements

Make sure you have Docker installed on your machine.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-pandas-app
   ```

2. Build the Docker image:
   ```
   docker build -t python-pandas-app .
   ```

## Running the Application

To run the application, use the following command:
```
docker run python-pandas-app
```

This will execute the main script and display the output. Make sure that the dataset file (`diabetes.csv`) is available in the appropriate directory as specified in the code.