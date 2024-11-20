# Yelp User-Based Recommendation System

---

## Objective

This project aims to develop a user-based recommendation system to predict businesses that Yelp users are likely to enjoy. By analyzing users' past interactions with businesses and identifying similarities between users, the system provides personalized business recommendations tailored to individual preferences.

![image](https://github.com/user-attachments/assets/c7e1a91f-4218-40c3-ad89-76cdf458eea5)

---

## Dataset Source

The project utilizes the following components from the Yelp dataset:

- **Review Dataset**: Contains user ratings, review text, and interaction details for businesses.
- **Bayesian Average Score Dataset**: Includes hybrid ranking scores for businesses based on quality, popularity, and customer engagement.

---

## Methodology

1. **Data Preparation**  
Rare businesses (with fewer than 300 reviews) and inactive users (with fewer than 30 reviews) are filtered out. The resulting data is transformed into a pivot table, creating a user-business matrix where each cell represents the rating a user gave to a business.

2. **User Similarity Analysis**  
For each user:
   - Businesses they have interacted with are identified.
   - Other users who visited the same businesses are retrieved.
   - Correlation scores between users are calculated, and users with a similarity score of 0.8 or higher are selected.

3. **Weighted Ratings**  
The ratings given by similar users are weighted by their similarity scores. A weighted average is calculated to determine the recommendation score for each business.

4. **Business Recommendation**  
Businesses with a recommendation score above a threshold (e.g., 4) are selected. These businesses are:
   - Ranked by category.
   - Enhanced using Bayesian hybrid ranking scores.
   - Deduplicated to ensure unique recommendations.

---

## Use Cases

- **Personalized Recommendations**: Suggest businesses users haven’t visited but are likely to enjoy based on similar users' preferences.  
- **Peer Group Analysis**: Identify similar user groups and recommend businesses popular among these groups.  
- **High-Quality Business Suggestions**: Prioritize businesses with high hybrid scores for quality and popularity.

---

## Project Results

The final output is a personalized recommendation list of the top 100 businesses for each user. For example:

| **User ID**               | **Recommended Businesses**                         |
|---------------------------|----------------------------------------------------|
| Xw7ZjaGfr0WNVt6s_5KZfA    | [Business A, Business B, Business C, ...]         |
| Y1NkcZlPogXZ2r4sHblTpA    | [Business D, Business E, Business F, ...]         |
| 3XYUtZbd2HSqjzBsleA0cA    | [Business G, Business H, Business I, ...]         |

<img width="1075" alt="Ekran Resmi 2024-11-16 12 07 23" src="https://github.com/user-attachments/assets/0b77ff38-d1b1-40da-be1d-d0d851df4d5b">

### Key Results:
1. **User-Centric Approach**: The system analyzes individual user behavior to generate tailored recommendations.  
2. **Comprehensive Business Analysis**: Recommended businesses are evaluated for both popularity and quality.  
3. **Scalable and Dynamic Model**: The system is designed to handle growth in the number of users and businesses efficiently.

---

## Insights

This user-based recommendation system enhances the Yelp user experience by providing personalized suggestions. By recommending businesses based on quality and customer feedback, the system enables users to make more informed decisions.


<br><br>
---

## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)
