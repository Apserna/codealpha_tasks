# 📚 CodeAlpha Book Analytics

A Python-based data analytics project developed as part of the **CodeAlpha Internship**.  
The project focuses on collecting book data from the **Books to Scrape** website, cleaning and exploring the dataset, and generating meaningful insights through data analysis and visualization.

## 📌 Project Overview

This project follows a complete data analytics workflow:

**Web Scraping → Data Cleaning → Exploratory Data Analysis → Data Visualization → Insights**

The dataset contains information about books, including details such as titles, prices, ratings, and availability-related information.

## 🎯 Objectives

- Collect book information using web scraping.
- Clean and prepare the scraped dataset for analysis.
- Perform Exploratory Data Analysis (EDA).
- Analyze book prices and ratings.
- Identify patterns and relationships in the dataset.
- Create meaningful visualizations.
- Extract useful insights from the data.

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **BeautifulSoup** – Web scraping
- **Requests** – HTTP requests
- **Jupyter Notebook** – Analysis and experimentation
- **VS Code** – Development environment

## 📂 Project Structure

```text
codealpha_tasks/
│
├── README.md
├── books_data.csv
├── books_data_cleaned.csv
├── scraper.py
├── eda.py
├── eda.ipynb
└── visualization.ipynb
```

### File Description

| File | Description |
|------|-------------|
| `scraper.py` | Python script used to scrape book information |
| `books_data.csv` | Raw scraped book dataset |
| `books_data_cleaned.csv` | Cleaned dataset prepared for analysis |
| `eda.py` | Python script for Exploratory Data Analysis |
| `eda.ipynb` | Jupyter Notebook containing EDA |
| `visualization.ipynb` | Notebook containing data visualizations |

## 🔎 Project Workflow

### 1. Web Scraping

Book information was collected from the **Books to Scrape** website using Python with:

- Requests
- BeautifulSoup
- HTML parsing

The extracted information was stored in CSV format for further analysis.

### 2. Data Cleaning

The raw dataset was processed using **Pandas**.

The cleaning process included:

- Checking for missing values
- Removing unnecessary data
- Converting data into suitable formats
- Preparing the dataset for analysis
- Saving the cleaned dataset as `books_data_cleaned.csv`

### 3. Exploratory Data Analysis

EDA was performed to understand the structure and characteristics of the dataset.

The analysis includes:

- Dataset shape
- Data types
- Summary statistics
- Price analysis
- Rating distribution
- Book-level analysis
- Correlation analysis
- Identification of patterns and trends

### 4. Data Visualization

Visualizations were created using **Matplotlib** and **Seaborn** to make the findings easier to understand.

Examples include:

- 📊 Rating distribution
- 💰 Book price distribution
- 📈 Price and rating relationship
- 📚 Distribution of books across ratings
- 🔗 Correlation analysis

## 📊 Key Analysis

One of the analyses examined the relationship between **book price and rating**.

The calculated correlation value was approximately:

```text
0.028
```

This indicates a **very weak linear relationship** between book price and rating in the analyzed dataset.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Apserna/codealpha_tasks.git
```

### 2. Navigate to the project folder

```bash
cd codealpha_tasks
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 jupyter
```

### 4. Run the web scraper

```bash
python scraper.py
```

### 5. Run the EDA script

```bash
python eda.py
```

### 6. Open the Jupyter notebooks

```bash
jupyter notebook
```

Then open:

```text
eda.ipynb
visualization.ipynb
```

## 💡 Insights

The analysis provides an understanding of:

- Book pricing patterns
- Rating distribution
- Relationships between numerical variables
- Distribution of books across different ratings
- Overall characteristics of the scraped book dataset

The project demonstrates how raw web data can be transformed into structured information and meaningful analytical insights.

## 🎓 Internship

This project was completed as part of my **Data Analytics Internship at CodeAlpha**.

The project provided practical experience in:

- Web scraping
- Data preprocessing
- Exploratory Data Analysis
- Data visualization
- Python-based analytics
- Working with real-world datasets

## 👩‍💻 Author

**Apserna**

GitHub: https://github.com/Apserna

## 🙏 Acknowledgements

- **CodeAlpha** – Internship opportunity and project guidance
- **Books to Scrape** – Source website used for the book dataset

## 📜 License

This project is created for **educational and internship purposes**.
