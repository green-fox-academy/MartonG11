# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class PostIt(object):
    background_color = ""
    text = ""
    text_color= ""

postit1 = PostIt()
postit2 = PostIt()
postit3 = PostIt()

postit1.background_color = "orange"
postit1.text = "Idea 1"
postit1.text_color = "blue"
postit2.background_color = "pink"
postit2.text = "Superb"
postit2.text_color = "black"
postit3.background_color = "yellow"
postit3.text = "Superb!"
postit3.text_color = "green"

print("Post-it object: " + postit1.text + ", text color: " + postit1.text_color + ", background color: " + postit1.background_color )
print("Post-it object: " + postit2.text + ", text color: " + postit2.text_color + ", background color: " + postit2.background_color )
print("Post-it object: " + postit3.text + ", text color: " + postit3.text_color + ", background color: " + postit3.background_color )