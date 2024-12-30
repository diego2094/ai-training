import random
import csv

# List of example names, partners, technologies, and industries
names = ["Carlos Fernandez", "Maria Lopez", "Javier Ramirez", "Ana Gomez", "Ricardo Martinez", "Sofia Rodriguez", "Juan Perez"]
partners = ["TechNova Solutions", "GreenLeaf Organics", "BlueWave Logistics", "QuantumMed Innovations", "EcoFusion Energy", "Stellar Financial", "AeroSpace Dynamics"]
technologies = ["React", "Node.js", "PostgreSQL", "Vue.js", "Django", "MySQL", "Angular", "Java", "MongoDB", "Python", "SQLite", "C++", "Spring Boot", "Express"]
industries = ["Technology", "Agriculture", "Food Industry", "Transportation & Logistics", "Automotive", "Healthcare", "Renewable Energy", "Finance", "Venture Capital", "Aerospace"]

# Possible skill sets for each role
cv_skills = {
    "Web Development": ['Fullstack Web Development', 'Frontend Development', 'Backend Development', 'Database Management'],
    "React": ['React Framework', 'Frontend Development', 'State Management', 'JavaScript Libraries'],
    "Node.js": ['Backend Development', 'Express.js', 'API Development', 'Database Management'],
    "Java": ['Java Programming', 'Backend Development', 'Object-Oriented Programming', 'Web Development'],
    "MongoDB": ['Database Management', 'NoSQL Databases', 'Backend Development', 'Data Modeling'],
    "Python": ['Backend Development', 'Machine Learning', 'Data Science', 'API Development'],
}

# Randomly generate rows
def generate_row():
    name = random.choice(names)
    partner = random.choice(partners)
    tech = random.sample(technologies, k=random.randint(2, 4))  # Select 2 to 4 random technologies
    industry = random.choice(industries)
    salary = random.randint(1500, 8000)  # Random salary between 1500 and 8000
    
    # Randomly choose skills from one of the technology-based CVs
    cv_skill_set = random.choice(list(cv_skills.values()))
    
    # Convert skill set into a formatted string for the CV
    processed_cv = "\n".join([f"{i+1}. {skill}" for i, skill in enumerate(cv_skill_set)])
    processed_cv_list = str(cv_skill_set)

    return [name, partner, ", ".join(tech), industry, salary, processed_cv, processed_cv_list]

# Create 500 rows of data
rows = []
for _ in range(500):
    rows.append(generate_row())

# Write data to CSV (without ID column)
with open('experts_profile_large.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Partner", "Technologies", "Industry", "Salary", "Processed_CV", "Processed_CV_list"])  # Header row
    for idx, row in enumerate(rows, start=0):
        writer.writerow([idx] + row)  # Add row number at the beginning

print("CSV file 'experts_profile_large.csv' created with 500 rows.")