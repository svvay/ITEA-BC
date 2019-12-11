# HW

* Write test with 3-4 cases


1. The third person singular verb form in English is distinguished 
    by the suffix -s, which is added to the stem of the infinitive form: 
    run -> runs. A simple set of rules can be given as follows:
    
    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s
    Your task in this exercise is to define a function make_3sg_form() 
    which given a verb in infinitive form returns its third person singular 
    form. Test your function with words like try, brush, run and fix. 
    Note however that the rules must be regarded as heuristic, in the 
    sense that you must not expect them to work for all cases. Tip: Check 
    out the string method endswith().

2. In English, the present participle is formed by adding the suffix -ing 
    to the infinite form: go -> going. A simple set of heuristic rules can be 
    given as follows:
    
    If the verb ends in e, drop the e and add ing (if not exception: be, see, 
      flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter 
    before adding ing
    By default just add ing
    Your task in this exercise is to define a function make_ing_form() which 
    given a verb in infinitive form returns its present participle form. Test 
    your function with words such as lie, see, move and hug. However, you must 
    not expect such simple rules to work for all cases.

3. Create decorator which print the execution time of function.
Use time or timeit module for it.
