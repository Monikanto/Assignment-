import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import stats

# 1. Create 1D and 2D NumPy arrays
arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Perform slicing and indexing on arrays
slice_val = arr1d[1:4]
index_val = arr2d[1, 2]

# 3. Add and multiply two matrices
mat_a = np.array([[1, 2], [3, 4]])
mat_b = np.array([[5, 6], [7, 8]])
addition = mat_a + mat_b
multiplication = np.dot(mat_a, mat_b)

# 4. Find transpose and inverse of a matrix
transpose_a = mat_a.T
inverse_a = np.linalg.inv(mat_a)

# 5. Compute mean, median, variance, and standard deviation
data_points = np.array([10, 20, 30, 40, 50])
mean_val = np.mean(data_points)
median_val = np.median(data_points)
variance_val = np.var(data_points)
std_dev_val = np.std(data_points)

# 6. Generate random numbers using NumPy and compute basic stats
random_data = np.random.randn(100)
rand_mean = np.mean(random_data)
rand_std = np.std(random_data)

# 7. Solve linear equations using numpy.linalg.solve()
# 3x + y = 9, x + 2y = 8
coeffs = np.array([[3, 1], [1, 2]])
consts = np.array([9, 8])
solution = np.linalg.solve(coeffs, consts)

# 8. Compute dot product and cross product of vectors
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
dot_res = np.dot(v1, v2)
cross_res = np.cross(v1, v2)

# 9. Reshape a matrix and flatten it
orig = np.array([1, 2, 3, 4, 5, 6])
reshaped = orig.reshape(2, 3)
flattened = reshaped.flatten()

# 10. Compare execution time of Python list vs NumPy array for sum operation
size = 1000000
p_list = list(range(size))
n_array = np.arange(size)
start = time.time()
sum(p_list)
list_time = time.time() - start
start = time.time()
np.sum(n_array)
numpy_time = time.time() - start

# 11. Calculate mean, median, and mode manually and using libraries
vals = [1, 2, 2, 3, 4]
man_mean = sum(vals) / len(vals)
man_median = sorted(vals)[len(vals)//2]
man_mode = max(set(vals), key=vals.count)
lib_mean = np.mean(vals)
lib_median = np.median(vals)
lib_mode = stats.mode(vals, keepdims=True).mode[0]

# 12. Create a frequency distribution table for a numeric column
data_col = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique, counts = np.unique(data_col, return_counts=True)
freq_dist = dict(zip(unique, counts))

# 13. Plot histogram for a given dataset and interpret the distribution
plt.hist(random_data, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Random Data")
plt.show()

# 14. Simulate coin toss probability experiment for N trials
n_trials = 1000
tosses = np.random.randint(0, 2, n_trials)
prob_heads = np.mean(tosses)

# 15. Implement binomial distribution simulation and plot PMF
n, p = 10, 0.5
binom_data = np.random.binomial(n, p, 1000)
plt.hist(binom_data, bins=10, density=True, alpha=0.6, color='g')
plt.title("Binomial Distribution PMF")
plt.show()

# 16. Generate and plot a normal distribution curve with different μ and σ
x_axis = np.linspace(-5, 5, 100)
plt.plot(x_axis, stats.norm.pdf(x_axis, 0, 1), label='mu=0, sigma=1')
plt.plot(x_axis, stats.norm.pdf(x_axis, 0, 2), label='mu=0, sigma=2')
plt.legend()
plt.show()

# 17. Compute correlation and covariance between two variables
x_var = np.array([1, 2, 3, 4, 5])
y_var = np.array([2, 4, 6, 8, 10])
covariance = np.cov(x_var, y_var)[0, 1]
correlation = np.corrcoef(x_var, y_var)[0, 1]

# 18. Perform simple random sampling from a dataset and compare summaries
population = np.random.normal(100, 15, 1000)
sample = np.random.choice(population, size=50)
pop_mean, sample_mean = np.mean(population), np.mean(sample)

# 19. Conduct a one-sample t-test on a sample and interpret p-value
t_stat, p_value = stats.ttest_1samp(sample, 100)

# 20. Perform chi-square test for independence on a contingency table
table = [[10, 20], [20, 30]]
chi2, p_chi, dof, expected = stats.chi2_contingency(table)