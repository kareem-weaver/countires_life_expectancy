import requests
from bs4 import BeautifulSoup

def get_salary_data():
    url = 'https://www.glassdoor.com/Salaries/data-scientist-salary-SRCH_KO0,14.htm'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    salary_elements = soup.find_all('div', class_='common__RangeBarStyle__rangeBarStyle')

    salaries = []
    for salary_element in salary_elements:
        salary_range = salary_element.text.strip()
        salaries.append(salary_range)

    return salaries

# Example usage
salary_data = get_salary_data()
for salary_range in salary_data:
    print(salary_range)
