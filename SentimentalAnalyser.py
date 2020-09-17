
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    x=''
    for i in punctuation_chars:
        if i in word:
            word=word.replace(i,'')
    return word

def get_pos(texts):
    words=texts.split(' ')
    count=0
    for word in words:
        x=strip_punctuation(word.lower())
        if x in positive_words:
            count=count+1
    return count

def get_neg(texts):
    words=texts.split(' ')
    c=0
    x=''
    for word in words:
        x=strip_punctuation(word.lower())
        if x in negative_words:
            c=c+1
    return c

twitter_data=open('project_twitter_data.csv')
#print(twitter_data.read())
retweet=0
replies=0
p_score=0
n_score=0
net_score=0
cl=0
sent=[]
result=open('resulting_data.csv','a')
#print(result_data)
#result_data=result.read()
result_data=""
result_data=result_data + 'Number of Retweets, '+'Number of Replies, '+'Positive Score, '+'Negative Score, '+'Net Score'+'\n'
for line in twitter_data:
    if cl==0:
        cl=1
        continue
    sent=line.split(',')
    retweet=retweet+int(sent[1])
    replies=replies+int(sent[2])
    p_score=p_score+get_pos(sent[0])
    n_score=n_score+get_neg(sent[0])
    net_score=p_score-n_score
    result_data=result_data+str(retweet)+','+str(replies)+','+str(p_score)+','+str(n_score)+','+str(net_score)+'\n'
    retweet=0
    replies=0
    p_score=0
    n_score=0
    net_score=0
result.write(result_data)
result.close()
