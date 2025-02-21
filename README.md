# BHCT Prediction - SPE ML Challenge 2025 by Fervo

## 1. Introduction

- **Problem Statement**
- **Objectives and Goals**
- **Importance and Real-World Applications**

## 2. Data Understanding

**2.1: Data Sources**

- **2.2: Data Description** (features, target variable)
- **2.3: Data Exploration** (visualizations, summary statistics)
- **2.4: Missing Data Analysis:**
  I used the missingno package to study the missing data (coded as -999.25) and found out some of the columns are up to 100% missing. Below is a summary of the column and missing percentage and a visualization to show a comparative view.

| Column                                 | Missing Percentage |
| -------------------------------------- | ------------------ |
| Annular Velocity (ft/min)              | 2.32%              |
| Bit MSE (psi)                          | 0.23%              |
| Depth of Cut (ft)                      | 0.01%              |
| East West Horizontal (ft)              | 95.56%             |
| G/L Rate - 5 Min (bbl/min)             | 0.03%              |
| Gamma Depth (ft)                       | 1.14%              |
| Gamma Ray (offset) (API)               | 63.24%             |
| MSE Downhole (psi)                     | 5.98%              |
| MSE Total (psi)                        | 5.98%              |
| North South Horizontal (ft)            | 95.56%             |
| Surface MSE wMotor (psi)               | 0.23%              |
| Total Gas (ML) (lagged) (1%=100 Units) | 100.00%            |

![missing matrix](images/missing_matrix.png)
I decided to discard columns of missing data more than 20%, nothing special about the percentage, this is a pure personal preference. The imputation approach of the remaining colums is by using the KNN imputer in the sklearn package. This approach involves learning from data and more efficient than mean or median imputation. Below how the data looks like after using backfill operation. That means following columns will be dropped.

| Column                                 | Missing Percentage |
| -------------------------------------- | ------------------ |
| East West Horizontal (ft)              | 95.56%             |
| Gamma Ray (offset) (API)               | 63.24%             |
| North South Horizontal (ft)            | 95.56%             |
| Total Gas (ML) (lagged) (1%=100 Units) | 100.00%            |


![missing matrix](images/missing_imputation.png)

- **2.5: Outliers Analysis:**

Local Outlier Factor (LOF) method was used analyze the outliers. I decided to remove the top 1% of the outliers scores. Here is the before and after values for the outlier removal from the 3 datasets.

| DataFrame | Original Length| New Length | Removed Points |
|-----------|----------------|------------|----------------|
| df1       | 7879           | 7800       | 79             |
| df2       | 8259           | 8176       | 83             |
| df3       | 6925           | 6855       | 70             |

## 3. Data Preprocessing
- **Correlation Matrix**
Since we have large number of columns, I kept only correlations above 0.5, checking the correlation matirx below.
![](images/corr.png)
below is correlations that are above 0.5
![](images/high_corr.png)
Some of these columns are prone to high covariance, this can be noticed from looking at the correlations values and can also be concluded from field experience, below is an example.

| Column                  | Correlation |
|-------------------------|-------------|
| Bttm Pipe Temp (°F)     | 1.000000    |
| Pipe Length (ft)        | 0.991367    |
| Depth(ft)               | 0.990280    |
| Bit Position (ft)       | 0.990280    |
| Hole Depth (ft)         | 0.990280    |
| Svy Depth (ft)          | 0.990214    |
| Gamma Depth (ft)        | 0.990206    |
| Bit Time (hr)           | 0.954932    |
| Time On Bottom (hr)     | 0.954932    |
| Circulating Hrs (hr)    | 0.928182    |

- **Feature Selection and Engineering**
- **Data Transformation** (scaling, encoding, normalization)
- **Handling Class Imbalance**
- **Splitting Data** (train-test-validation split)

## 4. Model Selection and Training

- **Overview of Algorithms Considered**
- **Justification for Chosen Model(s)**
- **Hyperparameter Tuning**
- **Model Training Details**

## 5. Model Evaluation

- **Performance Metrics** (accuracy, precision, recall, F1-score, etc.)
- **Confusion Matrix, ROC Curve, and AUC**
- **Cross-Validation Results**
- **Error Analysis**

## 6. Results and Discussion

- **Key Findings from Model Evaluation**
- **Comparison of Different Models**
- **Insights from Feature Importance Analysis**
- **Challenges Encountered**

## 7. Deployment (if applicable)

- **Model Saving and Loading**
- **API Development** (Flask, FastAPI, etc.)
- **Integration with Web Applications or Cloud Services**

## 8. Conclusion and Future Work

- **Summary of Findings**
- **Limitations of the Current Approach**
- **Recommendations for Improvement**
- **Future Research Directions**

## 9. References

- **Cite Books, Research Papers, Datasets, and Other Sources**

## 10. Appendices (if needed)

- **Additional Charts, Code Snippets, or Experiment Details**
