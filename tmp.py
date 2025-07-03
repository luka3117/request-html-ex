from requests_html import HTML, HTMLSession

# with open('simple.html', 'r') as f:
#     source = f.read()
#     html = HTML(html=source)

# session=HTMLSession()
# # r=session.get("https://google.com")
# r=session.get("https://www.youtube.com/watch?v=kbGu60QBx2o")
# r.html.render()
# print(r.html.text)


# session = HTMLSession()
# r = session.get('https://store.steampowered.com/search/?sort_by=Released_DESC&page=1914&os=win')
# r.html.render()

# with open("output.html", "w", encoding="utf-8") as f:
#     f.write(r.html.html)



from requests_html import HTMLSession

# Create an HTMLSession
session = HTMLSession()

# Get the URL
r = session.get("https://www.youtube.com/watch?v=kbGu60QBx2o")

# Render the page
r.html.render()

# Save the rendered HTML content to a file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(r.html.html)

print("HTML content saved to 'output.html'")
