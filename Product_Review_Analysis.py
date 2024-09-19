#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as 
# "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review with the keywords in uppercase.

#reviews = [
    #     "This product is really good. I'm impressed with its quality.",
    #     "The performance of this product is excellent. Highly recommended!",
    #     "I had a bad experience with this product. It didn't meet my expectations.",
    #     "Poor quality product. Wouldn't recommend it to anyone.",
    #     "The product was average. Nothing extraordinary about it."
    # ]

#So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        print(keyword)
        if keyword in review:
            new_review = review.replace(keyword, keyword.upper())
            print(new_review)

# def tally_count(reviews):
#     pos_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#     neg_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
#     pos_count = 0
#     neg_count = 0
#     for review in reviews:
#         for pos_word in pos_words:
#             pos_count += review.count(pos_word)
#         for neg_word in neg_words:
#             neg_count += review.count(neg_word)
#     print(f"The number of positive words is: {pos_count}. The number of negative words is: {neg_count}") #make look pretty)

# tally_count(reviews)
        
# limit = 30
# for review in reviews:
#     summ_review = review[:limit]
#     for character in review[limit:]:
#         if character != " ":
#             summ_review += character
#         else:
#             break
#     print(summ_review + "...")
