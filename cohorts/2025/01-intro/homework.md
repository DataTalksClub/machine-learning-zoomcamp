# Homework

## Set up the environment

You need to install Python, NumPy, Pandas, Matplotlib, and Seaborn. For that, you can use the instructions from
[06-environment.md](../../../01-intro/06-environment.md).

## Q1. Pandas version

What version of Pandas did you install?

You can get the version information using the `__version__` field:

```python
pd.__version__
```

## Getting the data 

For this homework, we'll use the Car Fuel Efficiency dataset. Download it from <a href='https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv'>here</a>.

You can do it with wget:
```bash
wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv
```

Or just open it with your browser and click "Save as...".

Now read it with Pandas.

## Q2. Records count

How many records are in the dataset?

- 4704
- 8704
- 9704
- 17704

## Q3. Fuel types

How many fuel types are presented in the dataset?

- 1
- 2
- 3
- 4

## Q4. Missing values

How many columns in the dataset have missing values?

- 0
- 1
- 2
- 3
- 4

## Q5. Max fuel efficiency

What's the maximum fuel efficiency of cars from Asia?

- 13.75
- 23.75
- 33.75
- 43.75

## Q6. Median value of horsepower

1. Find the median value of the `horsepower` column in the dataset.
2. Next, calculate the most frequent value of the same `horsepower` column.
3. Use the `fillna` method to fill the missing values in the `horsepower` column with the most frequent value from the previous step.
4. Now, calculate the median value of `horsepower` once again.

Has it changed?


- Yes, it increased
- Yes, it decreased
- No


## Q7. Sum of weights

1. Select all the cars from Asia
2. Select only columns `vehicle_weight` and `model_year`
3. Select the first 7 values
4. Get the underlying NumPy array. Let's call it `X`.
5. Compute matrix-matrix multiplication between the transpose of `X` and `X`. To get the transpose, use `X.T`. Let's call the result `XTX`.
6. Invert `XTX`.
7. Create an array `y` with values `[1100, 1300, 800, 900, 1000, 1100, 1200]`.
8. Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y`. Call the result `w`.
9. What's the sum of all the elements of the result?

> **Note**: You just implemented linear regression. We'll talk about it in the next lesson.

- 0.051
- 0.51
- 5.1
- 51

## Learning in Public

As part of this course, we encourage you to learn in public. Sharing your progress helps you reflect, stay accountable, and connect with others.

Write posts on your social media about Module 1 of this course.

How to do it
- Pick one platform (or more!) and post using the templates below
- Don't forget to tag Alexey Grigorev and use #mlzoomcamp hashtag

Alexey on social media: [LinkedIn](https://www.linkedin.com/in/agrigorev/), [Twitter/X](https://x.com/Al_Grigor)
DTC on social media: [LinkedIn](https://www.linkedin.com/company/datatalks-club/), [Twitter/X](https://x.com/DataTalksClub)

---

### LinkedIn Template (storytelling style)

[Hook — e.g., “I always thought machine learning started with algorithms. Module 1 showed me it actually starts with asking the right questions.”]

I just completed Module 1: Introduction to Machine Learning from ML Zoomcamp 2025 🎉

This module covered:

🔹 Difference between ML and rule-based systems

🔹 What supervised machine learning is

🔹 CRISP-DM: a framework for structuring ML projects

🔹 The model selection step

🔹 Setting up the environment (Python, Jupyter, etc.)

🔹 Quick refreshers on NumPy, linear algebra, and Pandas

✨ My key takeaway: [insert your personal insight]

🤔 Something I struggled with or found interesting: [insert challenge, surprise, or aha-moment]

➡️ Next step → Module 2: [your personal goal or excitement]

#mlzoomcamp #machinelearning #learninginpublic
Tag: @Alexey Grigorev

---

### Twitter / X Template

#### Single tweet version
Just wrapped up Module 1 of #mlzoomcamp 🚀

Learned about:

🔹 ML vs. rule-based systems

🔹 Supervised ML basics

🔹 CRISP-DM framework

🔹 Setting up environment + NumPy/Pandas/Linear Algebra refreshers

✨ Key takeaway: [insert insight]

➡️ Next up: Module 2!

#learninginpublic @alexeygrigorev

#### Thread starter
Day 1 of #mlzoomcamp ✅

Module 1: Intro to ML

Here’s what I learned 👇

(then add 2–3 tweets: 💡 takeaway, 🤔 challenge, 🚀 goal for Module 2)

---

### Telegram / Slack Community Template

✅ Finished Module 1 of ML Zoomcamp!

This module covered:

🔹 ML vs. rule-based systems

🔹 Supervised learning

🔹 CRISP-DM framework

🔹 Model selection

🔹 Environment setup (Python, Jupyter)

🔹 NumPy, Linear Algebra, Pandas refreshers

✨ Key takeaway: [insert insight]

🤔 Interesting or challenging part: [insert reflection]

➡️ Next step (Module 2): [your goal/excitement] 🚀


## Submit the results

* Submit your results here: https://courses.datatalks.club/ml-zoomcamp-2025/homework/hw01
* If your answer doesn't match options exactly, select the closest one
