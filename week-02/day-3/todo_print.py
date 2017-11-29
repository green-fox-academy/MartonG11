# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"

def adding(toText):
    new_todo= "My todo:\n" + toText + " - Download games\n   - Diablo"
    return(new_todo)

print(adding(todoText))