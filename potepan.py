from requests_html import HTML, HTMLSession

# -----------------
with open('./pote/potepan.html') as f:
    source = f.read()
    html = HTML(html=source)
# -----------------
# or 
# # -----------------
# addr='https://www.youtube.com/playlist?list=PLNk_DuZHWW79R_nB_OiwSqmbE7h35oUOr'
# session = HTMLSession()
# r = session.get(addr)

# vids=r.html.find("#video-title")
# for vid in vids:
#     title = vid.attrs.get('title')
#     link = vid.attrs.get('href')
#     if title and link:
#         link = "https://youtube.com" + link
#         print(f"Title: {title}")
#         print(f"Link: {link}")
#         print()
      
# # -----------------

# for vid in html.find("#video-title"):
#     title = vid.attrs.get('title')
#     link = vid.attrs.get('href')
#     if title and link:
#         link = "https://youtube.com" + link
#         print(f"Title: {title}")
#         print(f"Link: {link}")
#         print()


for vid in [html.find("#video-title", first=True)]:
    title = vid.attrs.get('title')
    link = vid.attrs.get('href')
    if title and link:
        link = "https://youtube.com" + link
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()

print("==========================")


