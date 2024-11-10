# List of years and associated colors
years = [2020, 2021]
colors = {
    2020: "linear-gradient(to right, #ff7e5f, #feb47b)",  
    2021: "linear-gradient(to right, #6a11cb, #2575fc)", 
}

# Path to the existing CSS file
css_file_path = 'timeline.css'

# Open and modify the existing CSS file
with open(css_file_path, 'r') as file:
    css_code = file.read()

# Modify the background color for each year in the CSS
for year in years:
    color = colors.get(year, '#ffffff') 
    css_code = css_code.replace(f'/* Year {year} background */', f'background-color: {color};')

# Save the updated CSS back to the file
with open(css_file_path, 'w') as file:
    file.write(css_code)

print("CSS file has been updated with the new background colors!")


