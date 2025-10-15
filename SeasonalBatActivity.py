
plt.figure(figsize=(8,5))
sns.countplot(x='season', hue='risk', data=df1, palette='Set2')
plt.title("Bat Risk-Taking Behaviour by Season")
plt.xlabel("Season")
plt.ylabel("Number of Observations")
plt.legend(title="Risk (1=Risk-taking, 0=Risk-avoidance)")
plt.show()

risk_winter = df1[df1['season']=='Winter']['risk'].mean()
risk_spring = df1[df1['season']=='Spring']['risk'].mean()
print(f"Average Risk-Taking - Winter: {risk_winter:.2f}, Spring: {risk_spring:.2f}\n")


plt.figure(figsize=(8,5))
sns.boxplot(x='season', y='bat_landing_number', data=df2, palette='coolwarm')
plt.title("Bat Landings per Observation by Season")
plt.xlabel("Season")
plt.ylabel("Number of Bat Landings")
plt.show()

print("📘 Interpretation 3:")
print("Bat activity is higher in Spring due to more available food.\n")

winter_land = df2[df2['season']=='Winter']['bat_landing_number']
spring_land = df2[df2['season']=='Spring']['bat_landing_number']
t_stat2, p_val2 = stats.ttest_ind(winter_land, spring_land, equal_var=False)
print(f"T-test: t={t_stat2:.3f}, p={p_val2:.4f}\n")