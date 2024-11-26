import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class TitanicEDA:
    def __init__(self, file_path):
        """
        Initialize the TitanicEDA class with the path to the dataset.
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load the Titanic dataset from the specified file path.
        """
        self.df = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def generate_summary_statistics(self):
        """
        Generate and print summary statistics of the dataset.
        """
        if self.df is not None:
            print("Summary Statistics:")
            print(self.df.describe(include='all'))
        else:
            print("Data not loaded. Please load data first.")

    def plot_survival_rates(self, feature):
        """
        Plot survival rates based on the specified feature and save the plot as an image file.
        """
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=feature, y='Survived', data=self.df, estimator=lambda x: sum(x) / len(x))
            plt.title(f'Survival Rate by {feature}')
            plt.xlabel(feature)
            plt.ylabel('Survival Rate')
            plt.savefig(f'survival_rate_by_{feature}.png')
            plt.close()
            print(f'Plot saved as survival_rate_by_{feature}.png')
        else:
            print("Data not loaded. Please load data first.")

    def plot_age_distribution(self):
        """
        Plot the distribution of ages and save the plot as an image file.
        """
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df['Age'].dropna(), kde=True, bins=30)
            plt.title('Age Distribution')
            plt.xlabel('Age')
            plt.ylabel('Frequency')
            plt.savefig('age_distribution.png')
            plt.close()
            print('Plot saved as age_distribution.png')
        else:
            print("Data not loaded. Please load data first.")

    def plot_class_distribution(self):
        """
        Plot the distribution of passengers based on their Pclass and save the plot as an image file.
        """
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            sns.countplot(x='Pclass', data=self.df)
            plt.title('Passenger Class Distribution')
            plt.xlabel('Pclass')
            plt.ylabel('Count')
            plt.savefig('class_distribution.png')
            plt.close()
            print('Plot saved as class_distribution.png')
        else:
            print("Data not loaded. Please load data first.")

    def plot_sex_distribution(self):
        """
        Plot the distribution of survival rates based on Sex and save the plot as an image file.
        """
        if self.df is not None:
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Sex', y='Survived', data=self.df, estimator=lambda x: sum(x) / len(x))
            plt.title('Survival Rate by Sex')
            plt.xlabel('Sex')
            plt.ylabel('Survival Rate')
            plt.savefig('survival_rate_by_sex.png')
            plt.close()
            print('Plot saved as survival_rate_by_sex.png')
        else:
            print("Data not loaded. Please load data first.")
# Create an instance of TitanicEDA
eda = TitanicEDA("Titanic-Dataset.csv")

# Load the Titanic dataset
eda.load_data()
# Generate summary statistics
eda.generate_summary_statistics()
# Plot survival rates by Pclass
eda.plot_survival_rates('Pclass')
# Plot survival rates by Sex
eda.plot_sex_distribution()
# Plot age distribution
eda.plot_age_distribution()
# Plot passenger class distribution
eda.plot_class_distribution()