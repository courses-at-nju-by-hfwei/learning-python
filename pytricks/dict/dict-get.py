# PyTricks 2023-01-15
# The get() method on dicts and its "default" argument

name_for_userid = {
    382: "Alice",
    550: "Bob",
    951: "Dilbert",
}

def greeting(userid: int) -> str:
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))

print(greeting(333333))
