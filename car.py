import cv2
import matplotlib.pyplot as plt

class Car:
    pass

title = Car.__name__

# List of image paths
image_paths = [
    'datasets/class2/11.jpg',
    'datasets/class2/12.jpg',
    'datasets/class2/13.jpg',
    'datasets/class2/14.jpg',
    'datasets/class2/15.jpg',
    'datasets/class2/16.jpeg',
    'datasets/class2/17.jpeg',
    'datasets/class2/18.jpeg',
    'datasets/class2/19.jpeg',
    'datasets/class2/20.jpeg'
    
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
