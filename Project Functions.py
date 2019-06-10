
# coding: utf-8

# # Functions for chatbot

# In[1]:


###Taken from A3
def is_in_list(list_one, list_two):
    ### if element is in list one, it should return list two
    
    for element in list_one:
        if element in list_two:
            return list_two
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_one:
            return list_two
    return None

def remove_punctuation(input_string):
    out_string = ''
    for character in input_string:
        if character in string.punctuation:
            continue
        else:
            out_string = out_string + character
    return out_string

def prepare_text(input_string):
    temp_string = ''
    out_list = ''
    temp_string = input_string.lower()
    temp_string = remove_punctuation (temp_string)
    out_list = temp_string.split()
    return out_list

def is_question(input_string):
    if '?'  in input_string:
        output = True
    else:
        output = False
    return output

def string_concatenator(string1, string2, separator):
    x = string1 + separator + string2
    return x

def selector(input_list, check_list, return_list):
    output = None
    for element in input_list:
        if element in check_list:
            output = random.choice(return_list)
            break
        else:
            continue
    return output

def end_chat (input_list):
    if 'quit' in input_list:
        return True
    else:
        return False


# # Function for chatbot

# In[2]:


##Most code is referenced from A3

def Potato():
    """Main function to run the chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)
        
###Code below this is my unique code

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Thanks for talking to me! \n I hope to hear from you again, bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output 
            if is_in_list(msg, GREETINGS_IN):
                outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            # Check if the input looks like a negative mood, add negative mood output
            if is_in_list(msg, MOODS_NEGATIVE_IN):
                outs.append(selector(msg, MOODS_NEGATIVE_IN, MOODS_NEGATIVE_OUT))

           
         #checks if message has danger words
            if is_in_list(msg, DANGER_IN):
                # and has yes, it'll give output with numbers to contact and end chat
                if is_in_list(msg, YES):
                    outs.append(DANGER_YES_OUT)
                    chat = False
                #and has no, it will ask why they're sad
                elif is_in_list(msg,NO):
                    outs.append(DANGER_NO_OUT)
                #if only has danger words, will ask if they are in danger
                else:
                    outs.append(selector(msg, DANGER_IN, DANGER_OUT))

                
            # if message is unsure, it'll tell them to do something fun and ask if they have free time
            if is_in_list(msg, MOODS_ODD_IN):
                outs.append(selector(msg, MOODS_ODD_IN, MOODS_ODD_OUT))
            
            #checks if it has free time in the message
            if is_in_list(msg,FREETIME_IN):
                #and has yes, it will suggest them to do an activity and end chat
                if is_in_list(msg,YES):
                    outs.append(MOODS_YES_OUT)
                    chat = False
                # will tell them to try to do the activity later and end chat
                else: 
                    outs.append(FREETIME_OUT)
                    chat = False
    
            #Check if input looks like a positive mood, add positive mood output and ends chat
            if is_in_list(msg, MOODS_POSITIVE_IN):
                outs.append(selector(msg, MOODS_POSITIVE_IN, MOODS_POSITIVE_OUT))
                chat = False
             
            # mention food or eating, will give reply about eating potatoes
            if is_in_list(msg,EATING_IN):
                outs.append(EATING_OUT)
            
            #if you mention potatoes or any form of potatoes it will end the chat
            if is_in_list(msg, POTATO_IN):
                outs.append(POTATO_OUT)
                chat = False

                
###My unique code stops here

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)

