# Segmentation Objective
The objective of segmentation is to create customer profiles and sort customer-business reviews based on these profiles.

![image](https://github.com/user-attachments/assets/977c9636-eb40-47f2-a5aa-a1385551333e)



## Dataset Source:
The dataset is sourced from Yelp Dataset and utilizes the User and Review segments.
https://www.yelp.com/dataset
* **User Dataset**: 1,807,703 rows, 11 columns
* **Review Dataset**: 5,791,201 rows, 9 columns

<br><br>
---

## RFM Methodology:
The RFM (Recency, Frequency, Monetary) methodology was applied as follows:

![image](https://github.com/user-attachments/assets/72943ebb-aea0-4b24-b430-67a879dba213)


* Recency: The difference between the most recent review date and the maximum review date.
* Frequency: Calculated based on the review count to determine activity frequency.
* Monetary (Engagement Score): Instead of monetary value, the usefulness of customer reviews was considered. An **"engagement score"** was calculated by summing the values of **"useful"**, **"funny"**, and **"cool"** in the dataset.

After calculating the RFM values, the results were grouped into categories ranging from 1 to 5 using the qcut function.

<br><br>
---

## Customer Segments
Below are the customer segment names (ranked by importance) and their descriptions:

▶ **Sleeping Flavors**:
Customers who rarely interact and have minimal engagement with businesses.

▶ **Flavor Hunters at Risk**:
Previously active customers who are losing interest and may stop engaging soon.

▶ **Irreplaceable Customers**:
Highly engaged customers who consistently contribute valuable reviews.

▶ **Drowsy Tasters**:
Customers with moderate activity and potential for increased engagement.

▶ **Needs Attention**:
Customers showing low engagement but with untapped potential.

▶ **Loyal Gourmets**:
Highly loyal customers with consistent engagement and positive feedback.

▶ **Promising**:
Customers with rising activity levels and potential to become loyal.

▶ **New Explorers**:
First-time customers exploring the platform, with opportunities for retention.

▶ **Potential Gourmet Customers**:
Active users showing strong signs of becoming highly engaged.

▶ **Gourmet Champions**:
The most valuable and loyal customers, setting examples for others.


### Segment Sorting
The "RF" values were used to prioritize and rank the customer segments.

<br><br>
---

## Sample Output
Below is an example visualization of the segmentation process and results:

![image](https://github.com/user-attachments/assets/3f09f51b-38a2-491e-8736-b4cc33c28e16)


## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)

