# Yelp Business Segmentation 

## Segmentation Objective
The goal of segmentation is to categorize businesses in the Yelp dataset accurately to enhance customer experience and ensure the right match between customers and venues.

## Dataset Source:
The dataset is sourced from Yelp Dataset and utilizes the Business and Check-in JSON files.
(https://www.yelp.com/dataset)
* Business Dataset: 1,196,983 rows, 13 columns
* Check-in Dataset: 103,160 rows, 2 columns
* Review Dataset: 5,791,201 rows, 9 columns

<br><br>
---
## RFM Methodology:
The RFM (Recency, Frequency, Monetary) methodology was applied as follows:
![image](https://github.com/user-attachments/assets/2f9a167e-4d12-4942-b7e4-6c5c8e04be19)



* **Recency**: Derived from the most recent business usage based on the date field in the Check-in dataset.
* **Frequency**: Calculated as the number of times a customer visited a particular restaurant using the Check-in dataset.
* **Monetary**: Instead of monetary value, the number of reviews per business was used to represent customer interest.

After calculating the RFM values, the results were distributed into groups ranging from 1 to 5 using the qcut function.

<br><br>
---

## Business Segments
Below are the segment names and their descriptions:

* **Hidden Gems**: Rarely visited but high-quality restaurants waiting to be discovered.
* **Comeback Cuisine** : Restaurants losing visitor interest but with strong potential for recovery.
* **Local Legends**: Highly loyal local customer favorites.
* **Slow Burners**: Low visit frequency but with growth potential for a loyal customer base.
* **On the Rise**: Restaurants gaining traction and building a loyal customer base.
* **Taste Trendsetters**: Innovative restaurants attracting new customers and starting to build loyalty.
* **Must-Try Spots**: Ideal for first-time visitors seeking unique dining experiences.
* **Loyalty Builders**: Restaurants with high potential for customer loyalty, requiring targeted strategies.
* **Crowd Pleasers**: Popular spots with high visitor traffic and broad appeal.
* **Star Diners**: Highly prestigious restaurants, exemplary in building loyal clientele.

### Segment Sorting
The "RF" values were used to prioritize and rank the restaurant segments.

<br><br>
---

## Sample Output
Below is an example visualization of the segmentation process and results:

![image](https://github.com/user-attachments/assets/36a4c707-19a2-4dd6-ba41-0e3a63533d14)

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


