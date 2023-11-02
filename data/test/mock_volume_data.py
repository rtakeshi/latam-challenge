import pandas as pd
import random
from faker import Faker

data = []

# Increase the number of dates
fake = Faker()
unique_dates = [fake.date_between(start_date='-1y', end_date='today') for _ in range(20000)]

# Increase the number of usernames
usernames = [fake.user_name() for _ in range(2000)]

# Increase the number of emojis
emojis = ["😀", "😍", "🚀", "🐱", "🌟", "🌍", "❤️", "🎉", "🌞", "🌸", "🌼", "🎈", "🎂", "🔥", "🍔", "🎳", "🌈", "🎸", "🍁", "⛱️", "🎺", "🍟", "🍦", "🌵", "🏆", "🏖️", "🎨", "🌮", "🍓", "🎆", "🚁", "🎵"]

# Increase the number of iterations
for i in range(100000):  # Adjust the number of outer iterations
    for j in range(1200):  # Adjust the number of inner iterations
        random_date = random.choice(unique_dates)
        random_tweet = fake.text() + " " + random.choice(emojis) + " @" + random.choice(usernames)
        data.append({'id': i * 1200 + j + 1, 'username': random.choice(usernames), 'content': random_tweet, 'date': random_date})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('test_volume_data20gb.csv', index=False, sep="~")





