# **Customer Service Operations & Device Usage Prediction Project**

## **Project Description**

The goal of this project is to predict high and low call volumes per week at different customer service facilities and analyze device usage patterns (e.g., gates, payment kiosks, exits) per facility and day of the week. Using historical call data, population density, traffic, and other metrics, several machine learning models (Decision Trees, Random Forests) were trained to achieve this.

### **Two Main Objectives:**

1. **Predict Weekly Call Volumes:**  
   Classify whether a week will experience high or low call volume using a variety of operational and temporal features.

2. **Forecast Device Usage Patterns:**  
   Forecast the usage of facility devices (gates, entries, exits, payment kiosks) to aid operational planning.

## **Data Description**

### **Calls Data:**

- Contains information on call operations, including `WaitTime`, `ConversationTime`, `City`, `Facility`, `Device`, `Reason for call`, and several operational flags (e.g., `Flag_BarrierOpened`, `Flag_MissedCall`).
- The `DateTime` column provides timestamps of calls.

### **Mobility Data:**

- Contains `DistanceTravelled` and population metrics per region.

### **Traffic Data:**

- Provides the number of cars per region and per 1000 people.

### **Population Density Data:**

- Provides population density by region.

### **Holiday Data:**

- Data on public holidays for 2022, 2023, and 2024.

## **Exploratory Data Analysis (EDA)**

EDA was performed to identify trends, outliers, and correlations in the dataset:

- **Call Volumes:** Distribution of call volumes over time and across facilities.
- **Device Usage:** How different devices (e.g., gates, exits) are used across facilities.
- **Time Trends:** Patterns in call and device usage by day of the week, hour of the day, and seasonal trends (Summer, Winter, etc.).

### **Key Visualizations:**

- Count of reported issues per city and facility.
- Average wait times per day of the week and per hour of the day.
- Correlation heatmap to identify multicollinearity among features.

## **Feature Engineering**

Several new features were created to improve the predictive power of the models:

- **Lagged Features:** Included lagged call volumes to predict future call volumes.
- **Interaction Terms:** Created interaction terms between device usage (e.g., barrier opened) and temporal variables (e.g., day of the week).
- **Binary Features:** Added flags for busy hours, weekends, and seasonal trends (e.g., summer vs winter).
- **Device Classification:** Classifying devices as `Entry`, `Exit`, `Gate`, `Pay`, and `Door` to analyze usage patterns.

## **Modeling**

### **1. Predicting Weekly Call Volumes**

- **Target:** Classify whether a week will have high or low call volume.
- **Models:**  
  - Decision Tree Classifier  
  - Random Forest Classifier
- **Features:** Operational features (wait time, conversation time), temporal features (hour of the day, day of the week), and device usage metrics.

#### **Performance Metrics:**

- **Accuracy:** 84.2%
- **Precision:** 85.7%
- **Recall:** 81.2%
- **F1-Score:** 83.4%

### **2. Predicting Device Usage**

- **Target:** Forecast the usage of specific devices (gates, entry points, etc.) in each facility.
- **Model:** Random Forest Regressor for multi-output regression.

### **Key Insights:**

- **Conversation Time** and **Wait Time** are critical operational metrics affecting device usage.
-  factors like **Hour of the Day** and **Day of the Week** also  influence usage patterns.

## **Results**

- The Random Forest model accurately predicted high and low call volume weeks with an accuracy of **84%**.
- For device usage prediction, the Random Forest Regressor provided reasonable RMSE values, enabling management to anticipate device usage spikes.
