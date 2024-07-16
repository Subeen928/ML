import cv2
import matplotlib.pyplot as plt

class House:
    pass

title = House.__name__

# List of image paths
image_paths = [
    'datasets/class1/1.jpg',
    'datasets/class1/2.jpg',
    'datasets/class1/3.jpeg',
    'datasets/class1/4.jpeg',
    'datasets/class1/5.jpeg',
    'datasets/class1/6.jpeg',
    'datasets/class1/7.jpeg',
    'datasets/class1/8.jpg',
    'datasets/class1/9.jpg',
    'datasets/class1/10.jpg'
    
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
