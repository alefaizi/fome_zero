# Fome Zero - Food Marketplace Dashboard

## 1. Business Problem
**Fome Zero** is a restaurant marketplace. Its core business is to connect customers and restaurants, facilitating discovery and transactions.

Restaurants register on the platform and provide information such as:
- address and location
- cuisine type
- reservation availability
- delivery options
- online ordering
- customer ratings and reviews

A newly hired CEO needs a clear view of the business to support strategic decision-making and scale the platform.  
To do that, the CEO requested a data analysis to answer a set of business questions across:

- overall platform metrics
- countries
- cities
- restaurants
- cuisine types

In addition, the CEO requested an interactive dashboard to make these insights easy to explore.

---

## 2. Assumptions and Data Cleaning
- The business model considered for the analysis is a **marketplace** (as defined in the problem statement).
- Removed **585 duplicate records** and **13 rows with missing values** from the original dataset. The cleaned dataset contains **6,929 records**.
- To standardize the *average cost for two*, all prices were converted to **USD**, using exchange rates from **Aug 24, 2024**.
- Identified **one outlier** in the *average cost for two* column and replaced it.
- For restaurants with multiple cuisine types, only the **first cuisine** was considered as the primary one; the remaining cuisines were dropped.

---

## 3. Solution Strategy
The strategic dashboard was built around the main findings extracted from answering **45+ business questions**, organized into key views:

### Home Page
- Project summary, main assumptions, and tech stack

### Main Page
- KPI cards: total restaurants, countries, cities, total reviews, cuisine types  
- Interactive map showing restaurant locations and details (name, city, rating)  
  - Marker color changes based on the restaurant rating

### Countries Page
- Restaurants by country  
- Cities by country  
- Average number of reviews per country  
- Average cost for two (USD) by country  

### Cities Page
- Top 10 cities by number of restaurants  
- Cities with the most restaurants rated **above 4.0**  
- Cities with the most restaurants rated **below 2.5**  
- Top 10 cities by number of distinct cuisine types  

### Cuisines Page
- Highlight cards with top-rated restaurants for Italian, American, Arabian, Japanese, and more  
- Table with the top 10 highest-rated restaurants  
- Top 10 best cuisines (by rating)  
- Top 10 worst cuisines (by rating)

---

## 4. Tech Stack
- **Python**
- **Pandas** – data manipulation and analysis
- **NumPy** – numerical operations
- **Inflection** – string normalization and feature standardization
- **Plotly Express** – interactive data visualizations
- **Folium** – geospatial visualization and interactive maps
- **Streamlit** – dashboard development and deployment
- **Pillow (PIL)** – image handling

---

## 5. Top 3 Data Insights
1. The average cost for two varies significantly across countries. **South Africa** (most expensive) has an average cost **~50x higher** than **Turkey** (least expensive).
2. Restaurants that accept **online orders** have **~2x more reviews** than those that do not. The average rating difference is only **0.04**, suggesting online ordering is beneficial due to higher engagement with minimal impact on ratings.
3. Restaurants that accept **reservations** have an average cost for two only **$0.06 lower** than restaurants that do not, indicating this feature has little to no influence on pricing.

---

## 6. Final Product
A live, cloud-hosted dashboard built with Streamlit and accessible from any internet-connected device:

Dashboard link: https://acsf-fomezero.streamlit.app/

---

## 7. Conclusion
This project aimed to create a set of charts, tables, and visualizations that help the CEO monitor key business metrics and make data-informed decisions.

Using Python for data analysis, I was able to answer all proposed questions (and additional questions that emerged during exploration). The dashboard focuses on the most actionable insights.

A sidebar filter was implemented to allow country selection (single or multiple). Once selected, the entire dashboard updates dynamically based on the chosen criteria.

---

## 8. Next Steps
- Add more filters
- Create additional business views
- Improve the Python scripts and modularize the codebase
- Explore the dataset further and answer new business questions
