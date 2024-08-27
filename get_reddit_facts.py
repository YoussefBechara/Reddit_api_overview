import praw
import regex as re

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def gather_reddit_facts(num_of_facts, num_of_facts_to_skip, timeout=60):

    reddit = praw.Reddit(
        client_id='your client id',
        client_secret='your client secret',
        user_agent='you user agent'
    )

    subreddit = reddit.subreddit('facts')
    facts_list = []

    for i, submission in enumerate(subreddit.top(time_filter ='all')):
        if i < num_of_facts_to_skip:
            continue

        try:
            content = submission.selftext
        except praw.exceptions.RequestException as e:
            print(f"Error fetching content for submission {submission.id}: {e}")
            continue

        content_without_emojis = remove_emojis(content)
        facts_list.append({
            'title': submission.title,
            'content': content_without_emojis,
        })

        if len(facts_list) >= num_of_facts:
            break

    return facts_list

if __name__ == '__main__':
    facts = gather_reddit_facts(1)
    for fact in facts:
        print(f"Fact: {fact['title']}\nSource: {fact['content']}\n")
