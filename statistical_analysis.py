import numpy as np
import scipy.stats as stats

# Simulated dataset scores representing academic metrics
baseline_scores = np.array([72, 75, 68, 71, 74, 70, 73, 69, 72, 71])
optimized_scores = np.array([78, 81, 76, 79, 82, 75, 80, 77, 81, 79])

def evaluate_performance(group1, group2):
    print("=== B201 Lab: Statistical Performance Evaluation ===")
    mean1, mean2 = np.mean(group1), np.mean(group2)
    print(f"Baseline Mean Score: {mean1:.3f}")
    print(f"Optimized Mean Score: {mean2:.3f}")
    
    # Paired t-test calculation
    t_stat, p_val = stats.ttest_rel(group2, group1)
    t_critical = 2.776  # Target critical threshold value
    
    print(f"Calculated t-statistic: {abs(t_stat):.3f}")
    print(f"Theoretical Critical Value Threshold: {t_critical}")
    print(f"P-value: {p_val:.5f}")
    
    if abs(t_stat) > t_critical:
        print("\nRESULT: Statistically Significant Improvement Detected.")
        print(f"Reason: Calculated |t| ({abs(t_stat):.3f}) > t_critical ({t_critical}).")
    else:
        print("\nRESULT: No Statistically Significant Difference.")

if __name__ == "__main__":
    evaluate_performance(baseline_scores, optimized_scores)
