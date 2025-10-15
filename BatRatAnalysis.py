
plt.figure(figsize=(8,5))
sns.boxplot(x='season', y='rat_minutes', data=df2, palette='mako')
plt.title("Rat Activity (Minutes Present) by Season")
plt.xlabel("Season")
plt.ylabel("Rat Minutes per Observation")
plt.show()

print("📘 Interpretation 4:")
print("Rats are more active in Spring, less in Winter due to resource scarcity.\n")

# T-test for rat activity
winter_rat = df2[df2['season']=='Winter']['rat_minutes']
spring_rat = df2[df2['season']=='Spring']['rat_minutes']
t_stat3, p_val3 = stats.ttest_ind(winter_rat, spring_rat, equal_var=False)
print(f"T-test: t={t_stat3:.3f}, p={p_val3:.4f}\n")

plt.figure(figsize=(7,5))
sns.scatterplot(x='rat_minutes', y='bat_landing_number', hue='season', data=df2, palette='magma')
plt.title("Relationship Between Rat and Bat Activity by Season")
plt.xlabel("Rat Minutes (Rat Activity)")
plt.ylabel("Bat Landings (Bat Activity)")
plt.show()

for season in ['Winter','Spring']:
    subset = df2[df2['season']==season].dropna(subset=['rat_minutes','bat_landing_number'])
    if len(subset) >= 2:
        corr, p = stats.pearsonr(subset['rat_minutes'], subset['bat_landing_number'])
        print(f"Correlation ({season}): {corr:.3f}, p={p:.4f}")
    else:
        print(f" Not enough data to calculate correlation for {season}.")