#
# showStats
#
# showStats
#
# Description: Find bounds by Z-Score, Chebyshev's inequality and Law of Large Number, Central Limit Theorem, etc
# Version: 1.0.2
# Author: Tomio Kobayashi
# Last Update: 2024/9/4


import numpy as np
import scipy.stats as stats

def showStats(samples, confidence_level = 0.95, population_percentile=0.6):


    # Find the z-scores for the two tails
    alpha = 1 - confidence_level
    k = stats.norm.ppf(1 - alpha / 2)
    
    means = []
    variances = []
    for sample in samples:


        # Calculate mean and variance of the sample
        sample_mean = np.mean(sample)
        sample_variance = np.var(sample, ddof=1)


        # Store the mean and variance
        means.append(sample_mean)
        variances.append(sample_variance)

    if num_sampling > 1:
        sample_mean = np.mean(means)
        sample_variance = np.var(means)

    print("*******")
    print("PREDICTION AFTER", num_sampling,  "SAMPLINGS")
#     print(f"k: {k} for confidence_level: {confidence_level}")
    print("Sample Mean:", sample_mean)
    print("Sample Variance:", sample_variance)
    if num_sampling == 1:
#         variance_of_sample = sample_variance/sample_picks
        variance_of_sample = sample_variance*sample_picks/(sample_picks-1)**2
    else:
#         variance_of_sample = sample_variance/num_sampling
        variance_of_sample = sample_variance*num_sampling/(num_sampling-1)**2
    print("Sample Variance of Sample Mean", variance_of_sample)

    # By Z score
    # Calculate the interval bounds
    lower_bound = sample_mean - k * np.sqrt(variance_of_sample) 
    upper_bound = sample_mean + k * np.sqrt(variance_of_sample)
    print(f"Interval Bounds of Mean by Z score: [{lower_bound}, {upper_bound}]")

    mean_of_variances = np.mean(variances)
    print("Mean of Variance", mean_of_variances)

    if num_sampling > 1:
        variance_of_variances = np.var(variances, ddof=1)
        variance_of_sample = variance_of_variances*num_sampling/(num_sampling-1)**2

        print("variance_of_variances", variance_of_variances)
        print("variance_of_sample", variance_of_sample)

        # By Z score
        # Calculate the interval bounds
        ci_mean_lower = mean_of_variances - k * np.sqrt(variance_of_sample) 
        ci_mean_upper = mean_of_variances + k * np.sqrt(variance_of_sample)

        # Display the results
        print(f"Interval Bounds of Variance by Z score Lower Bound: [{ci_mean_lower:.4f}, {ci_mean_upper:.4f}]")
    
    # By Chebyshev
    k2 = np.sqrt(1 / (1 - population_percentile))
    # Calculate the interval bounds
    lower_bound = sample_mean - k2 * np.sqrt(mean_of_variances) 
    upper_bound = sample_mean + k2 * np.sqrt(mean_of_variances)
    print(f"Middle {int(population_percentile*100)} percentile Bounds of Expected Population by Chebyshev: [{lower_bound}, {upper_bound}]")




# Execution Sample

import numpy as np

# Define the parameters
mean = 60
variance = 100
std_dev = np.sqrt(variance)  # Standard deviation
pop_size = 100000

# Generate the normally distributed vector
normal_vector = np.random.normal(loc=mean, scale=std_dev, size=pop_size)
# n = pop_size # Number of trials
# num_occured = pop_size*0.82 # Number of trials
# normal_vector = np.array([1 if i < num_occured else 0 for i in range(pop_size)])
# normal_vector = np.random.randint(1, 200, size=pop_size) + 300

# Print the first 10 elements to check
print("First 10 elements of the normally distributed vector:")
print(normal_vector[:10])

# Optional: Verify the mean and variance of the generated vector
mean = np.mean(normal_vector)
variance = np.var(normal_vector)
print("Population Mean:", mean)
print("Population Variance:", variance)

sample_picks =100
print("Sample Size", sample_picks)
num_sampling = 1
# Pick 5 random elements from the vector
sample = np.random.choice(normal_vector, size=sample_picks, replace=False)

confidence_level = 0.95
print(f"Confidence Level: {confidence_level}")

# Number of Sampling
for num_sampling in [1, 5, 10, 100]:
#     samples = []
#     for _ in range(num_sampling):
#         # Pick 5 random elements from the vector
#         sample = np.random.choice(normal_vector, size=sample_picks, replace=False)
#         samples.append(sample)
    samples = np.empty((0, sample_picks))
    for _ in range(num_sampling):
        # Pick 5 random elements from the vector
        sample = np.random.choice(normal_vector, size=sample_picks, replace=False)
        samples = np.vstack([samples, sample])
    showStats(samples, confidence_level, 0.7)