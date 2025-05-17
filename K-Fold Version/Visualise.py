import matplotlib.pyplot as plt
import numpy as np

# Data for Traditional Features
traditional_data = {
    'Full (55.9GB)': [0.591, 0.606, 0.708, 0.438, 0.678],
    '47.9GB': [0.510, 0.530, 0.651, 0.386, 0.623],
    '34.4GB': [0.527, 0.578, 0.692, 0.375, 0.616],
    '30.3GB': [0.520, 0.579, 0.661, 0.383, 0.601],
    '14.8GB': [0.412, 0.516, 0.563, 0.442, 0.472]
}

# Data for Whisper Features
whisper_data = {
    'Full (55.9GB)': [0.606, 0.571, 0.798, 0.322, 0.709],
    '47.9GB': [0.655, 0.603, 0.869, 0.296, 0.758],
    '34.4GB': [0.555, 0.549, 0.746, 0.340, 0.658],
    '30.3GB': [0.536, 0.502, 0.687, 0.342, 0.627],
    '14.8GB': [0.388, 0.516, 0.445, 0.587, 0.388]
}

metrics = ['Accuracy', 'ROC AUC', 'Sensitivity', 'Specificity', 'F1-Score']
datasets = ['Full (55.9GB)', '47.9GB' , '34.4GB' , '30.3GB', '14.8GB']
labels = ['Accuracy', 'ROC AUC', 'Sensitivity', 'Specificity', 'F1-Score']
x = np.arange(len(datasets))  # X-axis positions for datasets
width = 0.15  # Width of each bar

# Function to plot grouped bars
def plot_metrics(data, title):
    fig, ax = plt.subplots(figsize=(14, 6))
    for i, metric in enumerate(labels):
        # Extract metric values across all datasets
        values = [data[dataset][i] for dataset in datasets]
        ax.bar(x + i * width, values, width, label=metric)
    
    ax.set_xlabel('Dataset Size')
    ax.set_ylabel('Score')
    ax.set_title(title)
    ax.set_xticks(x + width * 2)
    ax.set_xticklabels(datasets)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Generate charts
plot_metrics(traditional_data, 'RandomForest with Traditional Features')
plot_metrics(whisper_data, 'RandomForest with Whisper Small Features')