# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

print(email_one)
def censor_words(content):
  new = content.replace("learning algorithms", "new technological techniques")
  return new

email_one = censor_words(email_one)
print(email_one)

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

print(email_one)
def censor_words(content, word = "learning algorithms", repl =  "**/censored/**"):
  new = content.replace(word, repl)
  return new

email_one = censor_words(email_one)
print(email_one)

print(email_two)
def censor_list(content, lst):
  for i in lst:
    content = censor_words(content,i)
  return content

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

email_two = censor_list(email_two, proprietary_terms)
print(email_two)

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "HELP!", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"] + proprietary_terms

print(email_three)
email_three = censor_list(email_three, negative_words)
print(email_three)

def censor_words_spec(content, word = "learning algorithms", repl =  "**/censored/**"):
  lst = content.split(" ")
  for i in range(len(lst)):
    if lst[i] is word:
      new = content.replace(lst[i-1], repl)
      new = content.replace(lst[i], repl)
      new = content.replace(lst[i+1], repl)
  return new

def special_censoring(content, lst):
  for i in lst:
    content = censor_words_spec(content,i)
  return content
    


print(email_four)
email_four = censor_list(email_four, negative_words)
print(email_four)


