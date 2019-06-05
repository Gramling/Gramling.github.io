domain = "http.//walshbr.com/"
pages = ["about", "blog", "pedagogy", "projects", "cv"]

#need to create new list combining domain with each individual webpage
#need new list
new_list = []

#need loop to combine domain with each webpage and then enter into new_list
#need to create webpage

#loop to combinne domain with each webpage
for page in pages:
    webpage = domain + page
#enter into new_list
    new_list.append(webpage)

print(new_list)
