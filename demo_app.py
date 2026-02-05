import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set page title
st.title("Normal Distribution Plotter")
st.write("Enter the mean and standard deviation to visualize a normal distribution.")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    mean = st.number_input("Mean (μ)", value=0.0, step=0.1)

with col2:
    std_dev = st.number_input("Standard Deviation (σ)", value=1.0, min_value=0.01, step=0.1)

# Generate x values for the distribution
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Calculate the probability density function
y = stats.norm.pdf(x, mean, std_dev)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', linewidth=2, label=f'μ={mean}, σ={std_dev}')
ax.fill_between(x, y, alpha=0.3)
ax.axvline(mean, color='r', linestyle='--', linewidth=1.5, label=f'Mean = {mean}')
ax.grid(True, alpha=0.3)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title('Normal Distribution', fontsize=14, fontweight='bold')
ax.legend()

# Display the plot
st.pyplot(fig)

# Display distribution statistics
st.subheader("Distribution Statistics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Mean (μ)", f"{mean:.2f}")

with col2:
    st.metric("Std Dev (σ)", f"{std_dev:.2f}")

with col3:
    st.metric("Variance (σ²)", f"{std_dev**2:.2f}")

# Add information about the normal distribution
with st.expander("ℹ️ About the Normal Distribution"):
    st.write("""
    The normal distribution (also called Gaussian distribution) is a bell-shaped probability distribution.
    
    Key properties:
    - **Mean (μ)**: The center of the distribution
    - **Standard Deviation (σ)**: Measures the spread of the distribution
    - Approximately 68% of values fall within ±1σ of the mean
    - Approximately 95% of values fall within ±2σ of the mean
    - Approximately 99.7% of values fall within ±3σ of the mean
    """)