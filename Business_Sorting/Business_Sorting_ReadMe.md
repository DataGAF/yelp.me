# Yelp Business Scoring and Ranking System

---

## Objective

This project aims to provide a robust scoring and ranking system for businesses in the Yelp dataset. By combining **Bayesian Average Rating (BAR)** with **Weighted Sorting Scores (WSS)**, the ranking system evaluates businesses based on customer ratings, review counts, and check-in data. The result is a fair and insightful method for identifying standout businesses and improving the user experience on Yelp.

---

## Dataset Source

This project uses the Yelp Dataset, focusing on the following components:

- **Review Dataset**: Provides user ratings and feedback for businesses.
- **Business Dataset**: Contains business metadata, including total review counts and average star ratings.
- **Check-in Dataset**: Tracks customer check-ins at businesses.

---

## Methodology

### 1. Bayesian Average Rating (BAR)

BAR provides a statistically robust method to rank businesses based on customer ratings. By adjusting for the number of ratings and their distribution, this approach prevents small sample sizes from disproportionately influencing rankings.

### 2. Weighted Sorting Score (WSS)

WSS evaluates businesses using three critical metrics:

- **Scaled Review Count**: Reflects the volume of customer feedback.
- **Scaled Check-in Count**: Captures customer visit frequency.
- **Star Ratings**: Indicates overall customer satisfaction.

The weighted combination of these metrics ensures that both popularity and quality are considered.

### 3. Hybrid Sorting Score (HSS)

HSS blends BAR and WSS to balance the qualitative and quantitative aspects of business performance. This approach highlights both highly-rated hidden gems and popular, frequently visited businesses.

---

## Segmentation and Ranking

Using these scores, businesses are categorized into actionable segments, including:

- **Hidden Gems**: Exceptional businesses with untapped popularity.
- **Crowd Pleasers**: Popular spots with high visit frequency and broad appeal.
- **Star Diners**: Prestigious venues with loyal customer bases.

---

## Use Cases

- **Enhanced Recommendations**: Provide personalized business suggestions based on a blend of customer ratings and popularity metrics.
- **Business Insights**: Help business owners understand their strengths and opportunities for improvement.
- **Improved Search Ranking**: Rank search results based on a holistic score that captures both customer sentiment and business activity.

---

## Project Results

A subset of businesses ranked by their Hybrid Sorting Scores demonstrates the value of combining Bayesian methods with real-world metrics. For example:

| **Business Segment** | **Key Insights**                           |
|-----------------------|--------------------------------------------|
| Hidden Gems           | High quality, awaiting discovery.         |
| Crowd Pleasers        | Frequent visits, broad popularity.        |
| Star Diners           | Loyal clientele, exceptional ratings.     |


<img width="537" alt="Ekran Resmi 2024-11-15 21 48 07" src="https://github.com/user-attachments/assets/ed55c6c5-12ec-49dc-b2f9-907bc86a05ed">


---

## Insights

By integrating Bayesian statistics with data-driven metrics, this project offers a comprehensive tool for ranking and evaluating businesses. These insights can help both Yelp users and business owners make informed decisions.

## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)
