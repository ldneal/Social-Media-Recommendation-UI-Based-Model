import pandas as pd
import numpy as np

# Load data from CSV files
posts_df = pd.read_csv("posts_challenge.csv")
users_df = pd.read_csv("users_challenge.csv")
likes_df = pd.read_csv("likes_challenge.csv")
testing_df = pd.read_csv("testing_user.csv")

# Merging datasets if necessary
likes_with_usernames_df = pd.merge(likes_df, users_df, on='user_id', how='left')

# Assuming 'user_name' is entered by the system
user_name = input("Enter user name: ")

# Assuming the system provides radio button values for filtering
already_liked_post = input("Filter already liked posts? (yes/no): ").lower() == 'yes'
created_by_user_post = input("Filter posts created by user? (yes/no): ").lower() == 'yes'

# Filter posts based on selected criteria
filtered_posts = posts_df.copy()

if already_liked_post:
    liked_post_ids = likes_df[likes_df['user_name'] == user_name]['post_id']
    filtered_posts = filtered_posts[~filtered_posts['post_id'].isin(liked_post_ids)]

if created_by_user_post:
    filtered_posts = filtered_posts[filtered_posts['created_by'] == user_name]

# Calculate matching probabilities
filtered_posts['matching_probability'] = np.random.rand(len(filtered_posts))

# Sort posts based on matching probabilities and select top 10
top_posts = filtered_posts.sort_values(by='matching_probability', ascending=False).head(10)

# Output the list of post IDs along with their matching probabilities
print("Top 10 Posts:")
print(top_posts[['post_id', 'matching_probability']])

# Save the top posts recommendation to a CSV file
top_posts.to_csv("top_posts_recommendation.csv", index=False)

# Check the first few rows of each dataset to understand the structure
print("\nPost Challenge Data:")
print(posts_df.head())

print("\nUsers Challenge Data:")
print(users_df.head())

print("\nLikes Challenges Data:")
print(likes_df.head())

# Merging datasets if necessary
likes_with_usernames_df = pd.merge(likes_df, users_df, on='user_id', how='left')

# Perform further analysis or use this merged dataset for training
# For training, you might need to transform data, extract features, etc.

# For demonstration purposes, let's say we want to count the number of likes per post
likes_per_post = likes_with_usernames_df.groupby('post_id').size().reset_index(name='num_likes_per_post')
print("\nLikes per Post:")
print(likes_per_post.head())

# Assuming 'user_name' is entered by the system
user_name = input("Enter user name: ")

# Assuming the system provides radio button values for filtering
already_liked_post = input("Filter already liked posts? (yes/no): ").lower() == 'yes'
created_by_user_post = input("Filter posts created by user? (yes/no): ").lower() == 'yes'

# Filter posts based on selected criteria
filtered_posts = posts_df.copy()

if already_liked_post:
    # Filter posts that are already liked by the user
    liked_post_ids = likes_df[likes_df['user_name'] == user_name]['post_id']
    filtered_posts = filtered_posts[filtered_posts['post_id'].isin(liked_post_ids)]

if created_by_user_post:
    # Filter posts that are created by the user
    filtered_posts = filtered_posts[filtered_posts['created_by'] == user_name]

# Calculate matching probabilities
# Here, you need to define the logic for calculating matching probabilities based on your specific requirements

# For demonstration purposes, let's assume we calculate probabilities randomly
filtered_posts['matching_probability'] = np.random.rand(len(filtered_posts))

# Sort posts based on matching probabilities and select top 10
top_posts = filtered_posts.sort_values(by='matching_probability', ascending=False).head(10)

# Output the list of post IDs along with their matching probabilities
print("Top 10 Posts:")
print(top_posts[['post_id', 'matching_probability']])

