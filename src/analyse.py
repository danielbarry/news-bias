import sys

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
      process_method(args[x])
    if args[x] == "-v" or args[x] == "--version" :
      process_arg = True
      process_version()
    if process_arg == True :
      data = args[x]
  # Check if we have a file
  if len(data) > 0 :
    print("Method\t" + method)
    # Load the file
    with open(data) as f :
      x = 0
      # Iterate over the lines in the file
      for line in f :
        # Process the file
        if method == "d" :
          print(str(x) + "\t" + str(analyse_dictionary()))
        # Increment our counter
        x += 1
  return

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
