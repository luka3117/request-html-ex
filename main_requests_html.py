from requests_html import HTML

with open("simple.html") as f:
    source = f.read()
    html = HTML(html=source)

# print(html.html)
# print(html.text)

print(html.find("h2")[0].text) # Returns a list of elements    )
print(html.find("h2")[0].html) # Returns a list of elements    )
print(html.find("h2")[0].find("a")[0].text) # Returns a list of elements    )


matches=html.find("#footer", first=True) # Returns the first element that matches the selector

print(matches.text)


articles= html.find("div.article") 
for article in articles:
    print(article.find("h2", first=True).text)
    print(article.find("p", first=True).text)
    print(article.find("a", first=True).attrs["href"])
    print()  # Print a newline for better readability

links=list(html.absolute_links)

for link in links:
    print(link)
    print()

with open("potepan.html") as f:
    source = f.read()
    html_potepan = HTML(html=source)


print()
for link in html_potepan.links:
    # if "potepan" in link:   # Filter links that contain "potepan"
    print(link)