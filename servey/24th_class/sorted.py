# 1. সংখ্যা ছোট থেকে বড় সাজানো
numbers = [2, 1, 4, 1, 5]
print(sorted(numbers))
# Output: [1, 1, 2, 4, 5]


# 2. সংখ্যা বড় থেকে ছোট সাজানো
print(sorted([4, 1, 5], reverse=True))
# Output: [5, 4, 1]


# 3. শব্দগুলোকে দৈর্ঘ্য (length) অনুযায়ী সাজানো
words = ["banana", "fig", "apple", "kiwi"]
print(sorted(words, key=len))
# Output: ['fig', 'kiwi', 'apple', 'banana']

# ভিতরে ভিতরে Python এভাবে ভাবছে:
# banana -> len = 6
# fig    -> len = 3
# apple  -> len = 5
# kiwi   -> len = 4
# তাই length অনুযায়ী sort হয়েছে।


# 4. শব্দগুলোকে শেষ অক্ষর (last character) অনুযায়ী সাজানো
print(sorted(words, key=lambda p: p[-1]))
# Output: ['banana', 'apple', 'fig', 'kiwi']

# ভিতরে ভিতরে Python এভাবে ভাবছে:
# banana -> a
# fig    -> g
# apple  -> e
# kiwi   -> i
# a < e < g < i
# তাই এই ক্রমে sort হয়েছে।