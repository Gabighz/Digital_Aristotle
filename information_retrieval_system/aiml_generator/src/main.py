##################################################
# Main program which writes AIML patterns and    #
# templates in .aiml format based on the outputs #
# of the Keyword and Keyphrase extractors        #
#                                                #
# Author: Gabriel Ghiuzan                        #
##################################################

import os
from information_retrieval_system.keyphrase_extractor.src.keyword_output import keyword_output
from information_retrieval_system.keyphrase_extractor.src.input_path import input_path


def main():

    # Stores the name of the input file
    filename = input_path()

    # Creates and array in which the first index is the name of the file
    # and the second index is the extension of the file (typically 'xml')
    filename_and_extension = filename.split('.')

    # Takes only the name of the file and adds the .aiml extension
    output_filename = filename_and_extension[0] + '.aiml'

    # An array which contains all the keywords generated by the Keyword extractor
    keywords = keyword_output(filename)

    # Stores an example of a keyphrase
    keyphrase = "A multiplexer is a special circuit that does this and that."

    # Stores the path of the file which will contain AIML rules
    output_path = "../../../AIML files/first-year/CS-150/" + output_filename

    # Enables us to create directories from within the program
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Opens a writeable File object
    aiml_file = open(output_path, "w")

    # Header information
    aiml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n")
    aiml_file.write("<aiml version=\"2.0\">" + "\n")

    # Writes categories. A category is made up of a pattern and a template.
    # The keywords will be used for patterns. The keyphrases for templates
    for keyword in keywords:
        aiml_file.write("\n   <category>")
        aiml_file.write("\n        <pattern>WHAT IS * %s </pattern> \n" % keyword)
        aiml_file.write("\n        <template> %s </template> \n" % keyphrase)
        aiml_file.write("\n   </category>")

    aiml_file.write("\n</aiml>")

    aiml_file.close()


main()
