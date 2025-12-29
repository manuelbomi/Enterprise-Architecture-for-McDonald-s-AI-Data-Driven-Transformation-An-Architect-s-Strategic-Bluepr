# McDonald's AI Capability Maturity Assessment
import pandas as pd
import matplotlib.pyplot as plt

mcd_capabilities = {
    'Capability': ['Customer Personalization', 'Kitchen Automation', 
                   'Supply Chain Prediction', 'Drive-thru AI', 
                   'Equipment Maintenance', 'Franchisee AI Enablement'],
    'Current_Score': [3.8, 2.2, 3.0, 2.5, 2.8, 1.8],  # From public disclosures
    'Target_Score': [4.8, 4.5, 4.2, 4.5, 4.0, 4.2],
    'Business_Impact': [9.5, 8.5, 8.0, 9.0, 7.5, 8.0]  # 1-10 scale
}

df = pd.DataFrame(mcd_capabilities)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gap analysis
axes[0].barh(df['Capability'], df['Current_Score'], height=0.6, label='Current', color='#FFC72C')
axes[0].barh(df['Capability'], df['Target_Score'], height=0.3, label='Target', color='#DA291C', alpha=0.7)
axes[0].set_xlabel('Maturity Level (1-5 Scale)')
axes[0].set_title('McDonald\'s AI Capability Gap Analysis')
axes[0].legend()

# Business impact vs current maturity scatter
axes[1].scatter(df['Current_Score'], df['Business_Impact'], s=df['Target_Score']*200, alpha=0.6)
for i, row in df.iterrows():
    axes[1].annotate(row['Capability'][:15], (row['Current_Score'], row['Business_Impact']), 
                     fontsize=9, ha='center')
axes[1].set_xlabel('Current Maturity')
axes[1].set_ylabel('Business Impact')
axes[1].set_title('Investment Priority Matrix')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('mcdonalds_ai_capability_analysis.png', dpi=300)
plt.show()