import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn theme
sns.set_theme(style="whitegrid")

# Load dataset
df = pd.read_csv(r"C:\Users\afrid\Desktop\PDS\Assignment_1\Student_Performance\raw_data\StudentsPerformance.csv")

# Display first few rows
print(df.head())

# Check column names
print("Column names:", df.columns)

# Convert categorical values to binary if 'gender' column exists
if 'gender' in df.columns:
    df['gender'] = df['gender'].map({'male': 0, 'female': 1})
    print("Unique values in 'gender' after conversion:", df['gender'].unique())
else:
    print("Error: 'gender' column not found! Available columns:", df.columns)

# Check for blank rows and drop them
print("Rows before dropna:", len(df))
df = df.dropna(how='all')
print("Rows after dropna:", len(df))

# Save cleaned dataset
df.to_csv(r"C:\Users\afrid\Desktop\PDS\Assignment_1\Student_Performance\results\students_cleaned.csv", index=False)
print("Cleaned dataset is saved at C:\\Users\\afrid\\Desktop\\PDS\\Assignment_1\\Student_Performance\\results\\students_cleaned.csv")

# Identify numeric columns for visualization
numeric_df = df.select_dtypes(include=['number'])

# Create 'results' directory if it doesn't exist
output_dir = r"C:\Users\afrid\Desktop\PDS\Assignment_1\Student_Performance\results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. Heatmap for correlation matrix (Only numeric columns)
if not numeric_df.empty:
    plt.figure(figsize=(10, 7))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix of Numeric Features", fontsize=14)
    plt.savefig(os.path.join(output_dir, "heatmap_correlation_matrix.png"))
    plt.close()
else:
    print("Error: No numeric columns available for correlation matrix!")

# 2. Scatter Plot: Math vs Reading Score
if 'math score' in df.columns and 'reading score' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, x='math score', y='reading score', hue=df['gender'] if 'gender' in df.columns else None,
        palette='coolwarm', alpha=0.8, edgecolor='black'
    )
    plt.title("Math Score vs Reading Score (Colored by Gender)", fontsize=14)
    plt.xlabel("Math Score", fontsize=12)
    plt.ylabel("Reading Score", fontsize=12)
    plt.legend(title="Gender (0 = Male, 1 = Female)" if 'gender' in df.columns else None)
    plt.savefig(os.path.join(output_dir, "scatter_math_vs_reading.png"))
    plt.close()

# 3. KDE Plot: Distribution of Writing Scores
if 'writing score' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['writing score'], fill=True, color='royalblue', linewidth=2, alpha=0.7)
    plt.title("Density Distribution of Writing Scores", fontsize=14)
    plt.xlabel("Writing Score", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.savefig(os.path.join(output_dir, "kde_writing_score.png"))
    plt.close()

# 4. Violin Plot: Math Score by Gender
if 'math score' in df.columns and 'gender' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='gender', y='math score', data=df, hue='gender', palette='coolwarm', inner="quartile", legend=False)
    plt.title("Math Score Distribution by Gender", fontsize=14)
    plt.xlabel("Gender (0 = Male, 1 = Female)", fontsize=12)
    plt.ylabel("Math Score", fontsize=12)
    plt.savefig(os.path.join(output_dir, "violin_math_score_by_gender.png"))
    plt.close()

# 5. Box Plot: Reading Score by Gender
if 'reading score' in df.columns and 'gender' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='gender', y='reading score', data=df, hue='gender', palette='Set2', legend=False)
    plt.title("Reading Score by Gender (Box Plot)", fontsize=14)
    plt.xlabel("Gender (0 = Male, 1 = Female)", fontsize=12)
    plt.ylabel("Reading Score", fontsize=12)
    plt.savefig(os.path.join(output_dir, "box_reading_score_by_gender.png"))
    plt.close()

print("All visualizations have been saved in the 'results' folder.")
