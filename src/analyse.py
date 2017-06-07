import re
import sys
# Source: https://textblob.readthedocs.io/en/latest/quickstart.html#quickstart
from textblob import TextBlob

# main()
#
# The main entry method into the program.
#
# @param args The arguments to the program.
def main(args) :
  # Initialise the variables
  data = ""
  method = "d"
  # Iterate over the arguments
  for x in range(0, len(args)) :
    process_arg = False
    # Process the arguments
    if args[x] == "-a" or args[x] == "--about" :
      process_arg = True
      process_about()
    if args[x] == "-h" or args[x] == "--help" or len(args) <= 0 :
      process_arg = True
      process_help()
    if args[x] == "-m" or args[x] == "--method" :
      process_arg = True
      x += 1
      method = process_method(args[x])
    if args[x] == "-v" or args[x] == "--version" :
      process_arg = True
      process_version()
    if process_arg == False :
      data = args[x]
  pos_words = []
  neg_words = []
  # Check if we have a file
  if len(data) > 0 :
    # Initialise sentiment analysis
    if method == "d" :
      with open("../dat/dictionary-positive.txt") as f :
        for line in f :
          pos_words += [line]
      with open("../dat/dictionary-negative.txt") as f :
        for line in f :
          neg_words += [line]
    print("Method\t" + method)
    # Load the file
    with open(data) as f :
      x = 0
      # Iterate over the lines in the file
      for line in f :
        # Process the file
        if method == "d" :
          print(
            str(x) +
            "\t" +
            str(analyse_dictionary(line, pos_words, neg_words))
          )
        if method == "p" :
          print(
            str(x) +
            "\t" +
            str(TextBlob(sanitize(line)).sentiment.polarity)
          )
        if method == "s" :
          print(
            str(x) +
            "\t" +
            str(TextBlob(sanitize(line)).sentiment.subjectivity)
          )
        # Increment our counter
        x += 1
  return

# analyse_dictionary()
#
# Analyse the words based on a dictionary lookup.
#
# @param sentence The string data to be analysed.
# @param pos_words Positive word list.
# @param neg_words Negative word list.
# @return Minus number if negative, positive number of positive.
def analyse_dictionary(sentence, pos_words, neg_words) :
  # Create word list
  words = sanitize(sentence).split(" ")
  val = 0
  # Check each of the words
  for x in range(0, len(words)) :
    # Check word against positive list
    for y in range(0, len(pos_words)) :
      if words[x] == unicode(pos_words[y], "latin-1") :
        val += 1
    # Check word against negative list
    for y in range(0, len(neg_words)) :
      if words[x] == unicode(neg_words[y], "latin-1") :
        val -= 1
  return val

# sanitize()
#
# Sanitize the input string.
#
# @param raw The raw input data to be sanitized.
# @return The sanitized string.
def sanitize(raw) :
  raw = unicode(raw, "latin-1")
  raw = raw.lower()
  raw = raw.replace("[", " ")
  raw = raw.replace("]", " ")
  raw = re.sub("[!@#$%^&*()_+<>./'`{}+=,\"\\:]", " ", raw)
  return raw

# process_about()
#
# Display the about for this program.
def process_about() :
  print("Written by B[]")
  return

# process_help()
#
# Display the help for this program.
def process_help() :
  print("analyse.py [OPT] [FILE]")
  print("")
  print("  OPTions")
  print("")
  print("    -a  --about      Information about program")
  print("    -h  --help       Display program help")
  print("    -m  --method     Set the program method")
  print("                       <CHAR> The mode to be set")
  print("                         'd' Dictionary matching")
  print("                         'p' Sentiment polarity")
  print("                         's' Sentiment subjectivity")
  print("    -v  --version    Display version information")
  print("")
  print("  FILE")
  print("")
  print("    The input file to analyse, line by line.")
  return

# process_method()
#
# Set the method for this program.
#
# @param method The method to be set.
# @return The method that is set.
def process_method(method) :
  return method

# process_version()
#
# Display the version for this program.
def process_version() :
  print("Version 0.0.1")
  return

# Start the main method if not already started
if __name__ == "__main__" :
  main(sys.argv[1:])
