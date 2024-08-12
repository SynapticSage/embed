import sys
import re
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_distances
from sklearn.cluster import AgglomerativeClustering
from sentence_transformers import SentenceTransformer

def extract_bullets(text):
    # Extract bullet points (lines starting with '*')
    bullets = re.findall(r'\*.*', text)
    return [bullet.strip('*').strip() for bullet in bullets]

def get_embeddings(sentences, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    return model.encode(sentences)

def create_distance_matrix(embeddings, sentences):
    # Create a distance matrix using cosine distances
    distance_matrix = cosine_distances(embeddings)
    return pd.DataFrame(distance_matrix, index=sentences, columns=sentences)

def cluster_and_plot(distance_matrix_df, output_plot=None):
    # Perform agglomerative clustering to reorder the distance matrix
    clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0, affinity='precomputed', linkage='average')
    clustering.fit(distance_matrix_df)
    ordered_indices = clustering.labels_.argsort()

    # Reorder the distance matrix
    ordered_df = distance_matrix_df.iloc[ordered_indices, ordered_indices]

    # Plot the clustered distance matrix using Seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(ordered_df, cmap='viridis', square=True, cbar=True)
    plt.title('Clustered Distance Matrix')
    plt.tight_layout()

    if output_plot:
        plt.savefig(output_plot)
        print(f"Clustered distance matrix plot saved to {output_plot}")
    else:
        plt.show()

def main():
    # Set up argparse to handle input file and model name
    parser = argparse.ArgumentParser(description='Process bullet points, generate embeddings, and create a distance matrix with clustering.')
    parser.add_argument('input_file', type=str, help='Path to the input file containing bullet points')
    parser.add_argument('--model', type=str, default='all-MiniLM-L6-v2', help='SentenceTransformers model to use for embeddings (default: all-MiniLM-L6-v2)')
    parser.add_argument('--output_matrix', type=str, default=None, help='Path to save the output distance matrix as CSV (optional)')
    parser.add_argument('--output_plot', type=str, default=None, help='Path to save the clustered distance matrix plot (optional)')

    args = parser.parse_args()

    # Read the input file
    with open(args.input_file, 'r') as file:
        input_text = file.read().strip()

    # Extract bullets
    sentences = extract_bullets(input_text)
    
    # Generate embeddings
    embeddings = get_embeddings(sentences, model_name=args.model)
    
    # Create distance matrix
    distance_matrix_df = create_distance_matrix(embeddings, sentences)
    
    # Output the distance matrix
    if args.output_matrix:
        distance_matrix_df.to_csv(args.output_matrix)
        print(f"Distance matrix saved to {args.output_matrix}")

    # Cluster and plot the distance matrix
    cluster_and_plot(distance_matrix_df, output_plot=args.output_plot)

if __name__ == "__main__":
    main()

