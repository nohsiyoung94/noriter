two = dex = zwei =2 

a= 200
a /= 3
print(a)

a = "q"
b = "z"

#c = a ** b
#print(c)

print('' == False)

letter = 'o'
vowel_set = {'a','e','i','o','u'}
print(letter in vowel_set)

#바다 코끼리 연산자
tweet_limit = 280
tweet_str = "Blah" * 50
diff = tweet_limit - len(tweet_str)
if  diff>=0:
    print("asd")
else:
    print("zxc")

###########################
tweet_limit = 200
tweet_str = "bbb" * 350
if (diff := tweet_limit - len(tweet_str)) >=0:
    print("A fitting Tweet")
else:
    print("Went Over by",abs(diff))
#############################
tweet_limit = 200
tweet_str = "bbb" * 300
if  tweet_limit - len(tweet_str) >=0:
    print("A fitting Tweet")
else:
    print("Went Over by",abs(tweet_limit - len(tweet_str)))
