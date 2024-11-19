# Sentiment Analysis for Tips Data Set

This analysis aims to determine whether the tips provided for venues express a positive or negative sentiment. Based on this sentiment, the tips dataset is sorted accordingly.

## Dataset Source:
The dataset is sourced from Yelp Dataset, specifically using the Tips dataset, which contains 693,021 rows and 5 columns.

<br><br>
---

## Sentiment Analysis Steps

1- **Data Cleaning and Preprocessing**:

  ⇨ Case Normalization: Convert all text to lowercase to eliminate differences between capitalized and non-capitalized words.
  ⇨ Punctuation Removal: Remove punctuation marks to ensure consistent text analysis.
  ⇨ Number Removal: Replace or remove numeric values to focus on textual content.

2- **Stopwords Removal**:

  ⇨ Stopwords (e.g., "the," "is," "and") are removed to reduce noise in the data and focus on meaningful words.

3- **Rare Words Removal**:

  ⇨ Words that appear very infrequently in the dataset are removed as they contribute little to overall sentiment analysis and may introduce noise.

4- **WordNet Integration**:

  ⇨ Incorporate WordNet to standardize word meanings and improve the understanding of word relationships in context.

5- **Lemmatization**:

  ⇨ Lemmatize words to their base or dictionary form (e.g., "running" to "run"), ensuring consistency and reducing variations of the same word.

6- **Sentiment Analysis**:

  ⇨ Perform sentiment analysis on the cleaned and preprocessed text using the following metrics:
  ⇨ Polarity Score: A numerical representation of the text's sentiment ranging from -1 (negative) to +1 (positive).
  ⇨ Sentiment Label: Classify the text as "Positive," "Neutral," or "Negative" based on the polarity score.
  ⇨ Compound Score: An aggregate score that combines all sentiment metrics to provide a comprehensive view of the text's sentiment.




## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)
