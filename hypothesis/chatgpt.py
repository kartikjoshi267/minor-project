import pandas as pd
from scipy.stats import spearmanr, pearsonr

# Read the data
data = pd.read_csv("https://gist.githubusercontent.com/kartikjoshi267/afdbd38f1842037f4845237cba184e5d/raw/819a506fcb683f89d8584c3b170f45e04e5056a4/student_dropout_analysis.csv")

print(data.isna().sum())

# Filter data for females only
# female_data = data[data['Gender'] == 0]
female_data = data
# female_data.loc[female_data["Marital status"] != 2, "Marital status"] = 0

# Calculate Spearman's rank correlation
correlation, p_value = pearsonr(female_data['Gender'], female_data["Target"])

print("Spearman's Rank Correlation Coefficient:", correlation)
print("p-value:", p_value)

alpha = 0.05
if p_value <= alpha:
    print("Reject Null Hypothesis: There is evidence of a significant correlation between marital status and dropout rates.")
else:
    print("Fail to reject Null Hypothesis: There is no evidence of a significant correlation between marital status and dropout rates.")
