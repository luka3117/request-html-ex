from requests_html import HTML 

with open("simple.html", "r") as f:
    source = f.read()
    html=HTML(html=source) 

anchor=html.find('a')
# print(html.text)
print(anchor)  # Print the text of the first anchor tag

