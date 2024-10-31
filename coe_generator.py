import numpy as np

# Define the function parameters
bitwidth = 11  # Total resolution: 10 bits for amplitude, 1 bit for sign
number_of_samples = 2**(bitwidth-1)  # Number of sine wave samples to generate (1024 samples)
Max_value = 2**(bitwidth-1) -1  # Maximum positive value for the sine wave (1024), since 10 bits are used for magnitude

# Generate an array of x values ranging from 0 to 1024 (sample indices)
x_values = np.arange(0, number_of_samples, 1)  # 1024 sample points over one sine wave period

# Calculate the corresponding y values as sine wave coefficients
# The sine wave is scaled to the max amplitude and floored to an integer value
y_values = np.floor(Max_value * np.sin(2 * np.pi / number_of_samples * x_values))  

# Save the generated sine wave coefficients into a text file
# The file 'sine_values.coe' will store the integer coefficients in a single column
np.savetxt('sine_values.coe', y_values, fmt='%d')  # Save as integers