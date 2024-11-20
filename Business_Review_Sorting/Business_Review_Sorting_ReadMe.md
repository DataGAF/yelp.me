# Yelp Business Review Sorting

---

## Objective

This project focuses on building a comprehensive review sorting system for businesses in the Yelp dataset. By incorporating **customer engagement**, **user segmentation**, and **review frequency**, this system identifies and prioritizes impactful reviews, creating actionable insights for businesses and enhancing the user experience.

---

## Dataset Source

This project leverages the following components from the Yelp dataset:

- **Review Dataset**: Provides customer feedback, including ratings, review text, and engagement metrics.
- **Customer Segmentation Dataset**: Contains segmentation attributes like RF_SCORE, customer segment categories, recency, and frequency.

![how-to-get-google-reviews](https://github.com/user-attachments/assets/1870a007-632d-4329-b40d-130b7ebaf2aa)


---

## Methodology

### 1. Engagement Calculation
Customer engagement is calculated by combining key interaction metrics into a single score:
- **Engagement**: The sum of `useful + funny + cool` votes for each review, highlighting how impactful a review is.

### 2. Merging Customer Segmentation with Reviews
The Review Dataset is enriched by merging it with the Customer Segmentation Dataset using `user_id`, enabling insights based on customer segments (e.g., Loyal Gourmets, Gourmet Champions).

### 3. Review Sorting Criteria
Reviews are sorted based on:
- **Date**: Recent reviews are prioritized.
- **Engagement**: High interaction scores indicate impactful reviews.
- **Customer Segment**: Reviews from valuable customer segments are ranked higher.
- **Star Ratings**: High-rated reviews are given priority.

### 4. Frequency Analysis
Additional metrics include:
- **User Review Frequency**: Tracks how often a user leaves reviews.
- **Business Review Frequency**: Tracks how often a business receives reviews.

---

## Project Results

The review sorting process generated a dataset that offers detailed insights into customer behaviors and business performance. Key results include:

### Final Metrics in the Dataset:
| **Review ID** | **User Segment**       | **Engagement** | **Stars** | **Date**       | **Review Count (User)** | **Review Count (Business)** |
|---------------|-------------------------|----------------|-----------|----------------|-------------------------|-----------------------------|
| 12345         | Gourmet Champions      | 45             | 5         | 2024-11-10     | 12                      | 30                          |
| 67890         | Loyal Gourmets         | 35             | 4         | 2024-11-09     | 8                       | 25                          |
| 11223         | Potential Gourmet Customers | 30         | 4         | 2024-11-08     | 6                       | 20                          |

<img width="1160" alt="Ekran Resmi 2024-11-15 22 32 17" src="https://github.com/user-attachments/assets/31388505-b6f0-489e-823b-8b56cd343fb8">



### Key Outcomes:
1. **Enhanced Review Sorting**: The system effectively identifies and prioritizes reviews based on engagement, recency, and customer importance.
2. **Segment-Focused Insights**: Reviews from high-value segments, such as "Gourmet Champions" and "Loyal Gourmets," are emphasized, providing actionable insights for businesses.
3. **Comprehensive Metrics**: By including user and business review frequencies, businesses gain a deeper understanding of customer activity patterns.

---

## Insights

This review sorting system empowers businesses with data-driven insights, enabling them to:
- Understand customer behavior across different segments.
- Focus on actionable feedback from high-value customers.
- Enhance customer satisfaction by addressing key pain points highlighted in impactful reviews.

By prioritizing reviews with high engagement and segment importance, this framework ensures that businesses can identify and act on the feedback that matters most.

## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)

