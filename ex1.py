from requests_html import HTML

with open("simple.html") as f:
    source = f.read()
    html = HTML(html=source)


# print(html.html)

match=html.find(".article", first=True)
matches=html.find(".article")   


print(match.find("p", first=True).text)  # Find the first p element within the first article element

for match in matches:  # Iterate through all article elements
    print("===============Article Element:==============")
    # print(match.html)  # Print the HTML content of each article element
    print(match.text)  # Print the text content of each article element   
    # print(match.find("h2", first=True).text)  # Print the text of the first h2 element within each article
    # print(match.find("p", first=True).text)  # Print the text of the first p element within each article
    # print(match.find("a", first=True).attrs["href"])  # Print the href attribute of the first a element
    print()  # Print a newline for better readability           

# print("===============First Div Element:==============")
# print(match.text)  # Print the text content of the first div element
# print(match.html)  # Print the HTML content
#  of the first div element
# print()  # Print a newline for better readability



# matches=html.find("div")  
# for match in matches:   # Find all div elements
#     print("===============Div Element:==============")
#     print(match.text)  # Print the text content of each div element
#     print(match.html)  # Print the HTML content of each div element
#     print()  # Print a newline for better readability


# anchor=html.find('a')
# # print(html.text)
# print(anchor)  # Print the text of the first anchor tag

