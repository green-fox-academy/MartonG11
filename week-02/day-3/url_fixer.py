# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!
# https://www.reddit.com/r/nevertellmetheodds/

url = "https//www.reddit.com/r/nevertellmethebots"

def fixer(wrong):
    new_wrong = wrong.replace("https", "https:")
    new_wrong = wrong.replace("nevertellmethebots", "nevertellmetheodds")
    return(new_wrong)


print(fixer(url))