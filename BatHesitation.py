
print("Dataset1 season counts:")
print(df1['season'].value_counts(), "\n")
print("Dataset2 season counts:")
print(df2['season'].value_counts(), "\n")


plt.figure(figsize=(8,5))
sns.boxplot(x='season', y='bat_landing_to_food', data=df1, palette='viridis')
plt.title("Bat Hesitation Time by Season")
plt.xlabel("Season")
plt.ylabel("Time from landing to food (seconds)")
plt.show()

print("📘 Interpretation 1:")
print("Boxplot shows bat hesitation time across Winter and Spring.")
print("Higher hesitation in Winter → bats are cautious when food is scarce.")
print("Lower hesitation in Spring → bats act faster when food is abundant.\n")

winter_hes = df1[df1['season']=='Winter']['bat_landing_to_food']
spring_hes = df1[df1['season']=='Spring']['bat_landing_to_food']
t_stat, p_val = stats.ttest_ind(winter_hes, spring_hes, equal_var=False)
print(f"T-test: t={t_stat:.3f}, p={p_val:.4f}\n")