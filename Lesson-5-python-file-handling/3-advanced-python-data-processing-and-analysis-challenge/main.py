import re
import os

class TravelBlogSentimentAnalyzer:
    def __init__(self, blog_file_path):
        self.blog_file_path = blog_file_path
        self.positive_words = ['amazing', 'enjoy', 'beautiful', 'wonderful', 'fantastic', 'memorable', 'enlightening']
        self.negative_words = ['disappointing', 'poor', 'lackluster', 'scarce', 'overcrowded']

    def analyze_sentiments(self):
        positive_count = 0
        negative_count = 0
        try:
            with open(self.blog_file_path, 'r') as file:
                for line in file:
                    for word in self.positive_words:
                        positive_count += len(re.findall(word, line, re.IGNORECASE))
                    for word in self.negative_words:
                        negative_count += len(re.findall(word, line, re.IGNORECASE))
            print("Task 1: Travel Blog Sentiment Analysis")
            print(f"Positive words count: {positive_count}")
            print(f"Negative words count: {negative_count}")
        except FileNotFoundError:
            print("Blog file not found.")

class WeatherDataCompiler:
    def __init__(self, file_paths):
        self.file_paths = file_paths

    def compile_and_analyze(self):
        year_avg_temps = {}
        for file_path in self.file_paths:
            total_temp = 0
            count = 0
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        match = re.search(r"(\d{4})-\d{2}-\d{2},(\d+)", line)
                        if match:
                            total_temp += int(match.group(2))
                            count += 1
                year = os.path.splitext(os.path.basename(file_path))[0].split('_')[-1]
                year_avg_temps[year] = total_temp / count if count else 0
            except FileNotFoundError:
                print(f"Weather file {file_path} not found.")

        if year_avg_temps:
            max_avg_temp_year = max(year_avg_temps, key=year_avg_temps.get)
            print("\nTask 2: Historical Weather Data Compiler")
            print("Yearly Average Temperatures:")
            for year, avg_temp in year_avg_temps.items():
                print(f"{year}: {avg_temp:.2f}°C")
            print(f"Year with the highest average temperature: {max_avg_temp_year} ({year_avg_temps[max_avg_temp_year]:.2f}°C)")

# Example usage
# Ensure to replace 'path/to/...' with the actual paths to the text files you've downloaded
blog_analyzer = TravelBlogSentimentAnalyzer('travel_blogs.txt')
blog_analyzer.analyze_sentiments()

weather_compiler = WeatherDataCompiler(['weather_2020.txt', 'weather_2021.txt'])
weather_compiler.compile_and_analyze()
