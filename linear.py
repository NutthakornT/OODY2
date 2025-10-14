import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import matplotlib.pyplot as plt
import csv

# -------------------------
# 1. Sample Dataset
# -------------------------

def read_csv_to_flattened_list(filepath):
    data_list = []
    
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Skip the header row
            try:
                header = next(reader)
            except StopIteration:
                # empty file
                return data_list 

            # Find the indices for 'value1' and 'value2'
            try:
                value1_index = header.index('text1')
                value2_index = header.index('text2')
            except ValueError:
                print("Error: 'text1' or 'text2' column not found in the header.")
                return data_list
            
            row_count = 0
            for row in reader:
                # capped at 5 data rows
                if row_count >= 5:
                    break
                
                # Check if the row has enough columns
                if len(row) > max(value1_index, value2_index):
                    data_list.append(row[value1_index])
                    data_list.append(row[value2_index])
                    row_count += 1
                else:
                    print(f"Warning: Row {row_count+2} (1-based index) is too short and was skipped.")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return data_list

filename = 'full_sample.csv'
docs = read_csv_to_flattened_list(filename)

print(docs)

doc_ids = [f"Doc {i+1}" for i in range(len(docs))]

# -------------------------
# 2. Convert Text → TF-IDF
# -------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs).toarray()
D = X  # document-term matrix

# -------------------------
# 3. Vector and Matrix operation
# -------------------------

# Cosine similarity (doc-doc)
cos_sim = cosine_similarity(D)

# Euclidean distance (doc-doc)
eu_dist = euclidean_distances(D)

# Pearson similarity (doc-doc)
pearson_sim = np.corrcoef(D)

# Covariance similarity (doc-doc)
# Compute covariance between documents using D @ D^T
cov_matrix = D @ D.T

# -------------------------
# 4. Normalize metrics
# -------------------------

# Normalize metrics to 0→1

# Cosine similarity is already 0→1

eu_sim = 1 - eu_dist / eu_dist.max()
# Normalize from [-1, 1] to [0, 1]
pearson_sim_norm = (pearson_sim + 1) / 2 
# Normalize the covariance matrix to the range [0, 1] for fair comparison
cov_sim = (cov_matrix - cov_matrix.min()) / (cov_matrix.max() - cov_matrix.min())

# -------------------------
# 5. Combine all Similarity
# -------------------------

# Equal weights
combined_sim = (cos_sim + eu_sim + pearson_sim_norm + cov_sim) / 4

# -------------------------
# 6. Build and Print Table
# -------------------------

# Build table
rows = []
N = len(docs)
for i in range(N):
    for j in range(i + 1, N):
        rows.append({
            "Document A": doc_ids[i],
            "Document B": doc_ids[j],
            "Cosine": round(cos_sim[i, j], 3),
            "Euclidean": round(eu_sim[i, j], 3),
            "Pearson": round(pearson_sim_norm[i, j], 3),
            "Covariance": round(cov_sim[i, j], 3),
            "Combined": round(combined_sim[i, j], 3)
        })

df_results = pd.DataFrame(rows)

def sort_similarity(df, metric="Combined", ascending=False):
    """Sorts the DataFrame by a specified similarity metric."""
    df_sorted = df.sort_values(by=metric, ascending=ascending)
    return df_sorted

# Sort by Combined similarity in descending order (Top 5)
df_sorted_combined = sort_similarity(df_results, metric="Combined", ascending=False)
print("\n=== Top 5 Most Similar Pairs (Sorted by Combined) ===")
print(df_sorted_combined.head(5).to_string(index=False))


# -------------------------
# 7. Visualization
# -------------------------
plt.figure(figsize=(8, 6))
plt.imshow(combined_sim, cmap="viridis")
plt.colorbar(label='Combined Similarity (0-1)')
plt.title("Combined Similarity Heatmap")
plt.xticks(range(N), doc_ids, rotation=45, ha='right')
plt.yticks(range(N), doc_ids)
plt.tight_layout()
plt.show()