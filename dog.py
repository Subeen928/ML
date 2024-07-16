import cv2
import matplotlib.pyplot as plt

class Dog:
    pass

title = Dog.__name__

# List of image paths
image_paths = [
    'datasets/class3/21.jpg',
    'datasets/class3/22.jpg',
    'datasets/class3/23.webp',
    'datasets/class3/24.jpg',
    'datasets/class3/25.jpg',
    'datasets/class3/26.jpg',
    'datasets/class3/27.jpg',
    'datasets/class3/28.jpeg',
    'datasets/class3/29.jpeg',
    'datasets/class3/30.jpeg'
    
]

# Create a figure with subplots
fig, axes = plt.subplots(2, 5, figsize=(15, 6))  # 2 rows, 5 columns

for i, image_path in enumerate(image_paths):
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Warning: Couldn't open/read file: {image_path}")
        continue
    
    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Get the subplot
    ax = axes[i // 5, i % 5]
    
    # Display the image
    ax.imshow(image)
    
    # Add title
    ax.set_title(f"{title} {i+1}")
    
    # Hide axis
    ax.axis('off')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Close all plots
plt.close('all')
