story = input ('''Type a story:''')

the = "ermagherd "
a = "ayyyyyy "
period = "." + "\a"

story = story.replace("the",the)
story = story.replace("The",the)
story = story.replace(" a ",a)
story = story.replace("A ",a)
story = story.replace(".",period)
print(story)
