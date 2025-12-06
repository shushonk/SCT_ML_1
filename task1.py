import matplotlib.pyplot as plt
import numpy as np

# Create sample housing data
np.random.seed(42)
n = 200

# Generate features
sqft = np.random.normal(2000, 500, n).clip(800, 3500)
bedrooms = np.random.choice([2, 3, 4], n, p=[0.3, 0.5, 0.2])
school_rating = np.random.uniform(5, 10, n)
age = np.random.randint(0, 50, n)

# Calculate price (simple formula)
price = (sqft * 200 + 
         bedrooms * 35000 + 
         school_rating * 20000 - 
         age * 1000 + 
         np.random.normal(0, 50000, n))

# Create figure with 4 plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Price Distribution
axes[0,0].hist(price/1000000, bins=20, color='lightblue', edgecolor='black', alpha=0.8)
axes[0,0].axvline(price.mean()/1000000, color='red', linestyle='--', linewidth=2, 
                 label=f'Mean: ${price.mean()/1000000:.1f}M')
axes[0,0].axvline(np.median(price)/1000000, color='green', linestyle='--', linewidth=2,
                 label=f'Median: ${np.median(price)/1000000:.1f}M')
axes[0,0].set_xlabel('Price (Millions $)')
axes[0,0].set_ylabel('Number of Houses')
axes[0,0].set_title('🏠 Housing Price Distribution')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# 2. Price vs Square Feet
scatter = axes[0,1].scatter(sqft, price/1000, c=bedrooms, cmap='coolwarm', 
                           alpha=0.7, s=50, edgecolor='black')
axes[0,1].set_xlabel('Square Feet')
axes[0,1].set_ylabel('Price (Thousands $)')
axes[0,1].set_title('📐 Price vs Square Feet')
axes[0,1].grid(True, alpha=0.3)

# Add colorbar for bedrooms
cbar = plt.colorbar(scatter, ax=axes[0,1])
cbar.set_label('Bedrooms')

# 3. Price by Bedroom Count
bedroom_groups = []
price_by_bedroom = []
for beds in [2, 3, 4]:
    bedroom_groups.append(beds)
    price_by_bedroom.append(price[bedrooms == beds].mean()/1000000)

bars = axes[1,0].bar(bedroom_groups, price_by_bedroom, color=['lightgreen', 'lightblue', 'lightcoral'])
axes[1,0].set_xlabel('Number of Bedrooms')
axes[1,0].set_ylabel('Average Price (Millions $)')
axes[1,0].set_title('🛏️ Average Price by Bedrooms')
axes[1,0].set_xticks([2, 3, 4])
axes[1,0].grid(True, alpha=0.3)

# Add values on bars
for bar, val in zip(bars, price_by_bedroom):
    axes[1,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                  f'${val:.2f}M', ha='center', fontweight='bold')

# 4. Price vs Property Age
scatter2 = axes[1,1].scatter(age, price/1000, c=school_rating, cmap='viridis',
                            alpha=0.7, s=50, edgecolor='black')
axes[1,1].set_xlabel('Property Age (Years)')
axes[1,1].set_ylabel('Price (Thousands $)')
axes[1,1].set_title('🏚️ Price vs Property Age')
axes[1,1].grid(True, alpha=0.3)

# Add colorbar for school rating
cbar2 = plt.colorbar(scatter2, ax=axes[1,1])
cbar2.set_label('School Rating')

# Add simple statistics text box
stats_text = f"""
Statistics Summary:
• Houses: {n}
• Avg Price: ${price.mean():,.0f}
• Avg SqFt: {sqft.mean():,.0f}
• Avg Bedrooms: {bedrooms.mean():.1f}
• Price Range: ${price.min():,.0f} - ${price.max():,.0f}
"""

plt.figtext(0.02, 0.02, stats_text, fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('Simple Housing Price Analysis', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()