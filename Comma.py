def comma(spam):
    for x in range(len(spam)):
        if x == (len(spam) - 2):
            print(spam[x], end = ' and ')
        elif x == (len(spam) -1):
            print(spam[x])
        else:
            print(spam[x], end = ', ')
spam=['apples','bananas','tofu','cats']
comma(spam)
