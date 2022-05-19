import pandas as pd
dataset = pd.read_csv("./csv/USvideos.csv")
# print(dataset)
# print(dataset.head(5))
# thumbnail_link,video_id,trending_date,publish_time,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed
# dataset.drop(columns=["thumbnail_link","video_id","trending_date","publish_time","comments_disabled","ratings_disabled","video_error_or_removed"],inplace=True)
# print(dataset)
# print(len(dataset.index))
# print(len(dataset.columns))
# print(dataset["likes"].mean())
# print(dataset["dislikes"].mean())
# print(dataset[dataset["views"].max() == dataset["views"]]["title"].iloc[0])
# print(dataset[dataset["views"].min() == dataset["views"]]["title"].iloc[0])
# print(dataset.groupby("category_id").mean()[["comment_count"]])
# print(dataset["category_id"].value_counts())
# def countTitleCount(title):
#     return len(title)
# dataset["title_length"] = dataset["title"].apply(countTitleCount)
# def countTag(tags):
#     tagList = tags.split("|")
#     return len(tagList)
# dataset["tag_count"] = dataset["tags"].apply(countTag)
 
# def likesAnddislikes(likes,dislikes):
#     likesList = list()
#     dislikesList = list()
#     for key,value in likes.iteritems():
#         likesList.append(value)
#     for key,value in dislikes.iteritems():
#         dislikesList.append(value)
    
#     likeanddislikeratio = list()
#     for like,dislike in zip(likesList,dislikesList): 
#         if like + dislike == 0:
#             likeanddislikeratio.append(0)
#         else:
#             likeanddislikeratio.append(like/(like + dislike))
#     return likeanddislikeratio
        
# dataset["likes_dislikes"] = likesAnddislikes(dataset["likes"],dataset["dislikes"])

# print(dataset)