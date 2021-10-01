
# function parameters list of all possible outcomes and query entered by user
def search(main_data_list, user_query):
    user_list = user_query.split()
    sorted_score_list=[]
    # iterating through the elements in main data list
    for i in main_data_list:
        counts = 0
        # iterating through the words in user's query
        for a in user_list:
            if a in i.lower():
                # if words from users query matches statements in main list score increases
                counts+=i.lower().count(a)
            else:
                continue
        sorted_score_list.append((counts,i))
    # the list is sorted to give results that matches user's query more
    sorted_score_list= sorted(sorted_score_list, reverse=True)
    # the results are printed with number of words that matches with the query
    for score,sentence in sorted_score_list:
        print(f"{sentence}: with score {score}")

if __name__ == "__main__":
    # query set
    sentences=[ "python is good","this is good","this is written in python"]

    user_q = input("Enter your query: ").lower()
    search(sentences,user_q)