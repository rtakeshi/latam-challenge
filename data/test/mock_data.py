import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Create a list of dictionaries to store the data
data = []

# Generate 20 unique dates
fake = Faker()
unique_dates = [fake.date_between(start_date='-1y', end_date='today') for _ in range(10)]

# Generate 20 different usernames
usernames = [fake.user_name() for _ in range(12)]

# Generate 20 tweets with emojis
emojis = ["😀", "😍", "🚀", "🐱", "🌟", "🌍", "❤️", "🎉"]
for i in range(10):
    for j in range(12):
        random_date = random.choice(unique_dates)
        random_tweet = fake.text() + " " + random.choice(emojis) + "@"+random.choice(usernames)
        data.append({'id': i * 20 + j + 1, 'username': usernames[i], 'content': random_tweet, 'date': random_date})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('test_data.csv', index=False)