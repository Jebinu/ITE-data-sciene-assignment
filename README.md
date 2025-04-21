# Visitor-Exhibitor Matching & Insights (ITE Data Science Assignment)

## 🎯 Objective
Analyze visitor and exhibitor registration data from a corporate event, extract insights, and build a smart matching system to recommend relevant exhibitors to visitors and vice versa.

---

## 📁 Project Structure

- `source_datasets/` – Contains **all raw CSV files** (visitors, exhibitors, questions, answers, etc.)  
  as well as **cleaned datasets** like `final_analysis_data_visitors.csv`, `exhibitor_final.csv`, etc.
- `code/` – Jupyter Notebook(s) with full data processing, analysis, and recommendation logic
- `Visitor_Exhibitor_Matching_Presentation.pptx` – Final presentation summarizing insights and model
- `requirements.txt` – Python libraries used in the project
- `README.md` – Project documentation (this file)

---

## 🔧 Work Summary

### ✅ 1. Data Cleaning & Processing
- Parsed nested JSON structure from visitor responses
- Merged `visitor`, `question`, and `answer` datasets to build a rich visitor profile
- Cleaned and merged exhibitor categories 
- Removed duplicates, handled missing values
- Cleaned and standardized email formats

### ✅ 2. Visitor Profile Analysis
- **Gender distribution** analysis: Majority of visitors are male – insight for inclusive planning
- **Top questions and answers** highlight visitor engagement and reveal their key interests

### ✅ 3. Exhibitor Profile Analysis
- Cleaned and categorized exhibitor data
- Frequency analysis of exhibitor categories
- Detected over-generic exhibitors selecting too many broad categories
- Shows how different categories are spread across exhibitors to spot common areas

### ✅ 4. Visitor-Exhibitor Matching Model

- **TF-IDF + Cosine Similarity** used for intelligent matching
- **Three Recommendation Functions**:
  - Match by **visitor email** (interest-based)
  - Match by **visitor answers**
  - Match by **exhibitor ID**
- Matching is based on **highest similarity scores**
- Sample output: Top 7 recommendations for each query
- Validated logic using visitor data
- Edge cases (e.g., missing info or overly generic exhibitors) handled carefully

### ✅ 5. Data Visualization
- Gender distribution, answer frequency, and category spread
- Category popularity and frequency
- Visitor Engagement & Interests:
  - Top questions and common answers reveal engagement patterns

### ✅ 6. Unit Testing
- **Testing performed inside each of the three recommendation notebooks and separate notebooks "Tests"**
- Reusable and scalable for future development
- Validated logic and handled exceptions

### ✅ 7. Advanced Insights
- **Predictive Analysis**:
  - Topic Modeling using NMF to uncover emerging visitor themes
- **Cluster Analysis**:
  - Identified **4 distinct visitor segments**
  - Supports targeted recommendations and smarter category planning

---

## 🚀 How to Run
1. Clone the repo or download the files
2. Open the Jupyter Notebooks inside the `code/` folder
3. Run all cells in order to see processing, analysis, and recommendations

> **Note**: Install dependencies using  
> `pip install -r requirements.txt`

---

## 📽️ Presentation
The `Visitor_Exhibitor_Matching_Presentation.pptx` contains:
- Project overview
- Key findings and insights
- Recommendation model breakdown
- Business impact & suggested next steps

---

## ✅ Status
- [x] Visitor Profile Analysis  
- [x] Exhibitor Profile Analysis  
- [x] Matching System (Visitors ↔ Exhibitors)  
- [x] Visualizations  
- [x] Inline Unit Testing (3 recommendation notebooks)  
- [x] `requirements.txt`  
- [x] Clustering & Prediction Analysis  

---

## ✍️ Author
**Jebinu**  
Data Science Assignment – ITE
