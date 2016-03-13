import yelp_academic_dataset_review
import requests


def some_action(post):
     print(post['created_time'])



access_token = 'CAACEdEose0cBAJWAUXodZB7pGUdZBkZBnOPOvEylGPaUUXvjr7pZC6V7ieZCU6CzCZBRgfJxz28SzOQ5H63L2qQvCnFFV2r7j7CsZCVdryqCtnUdZAD4ofhaE6uZB8so2A92b6JxE39iZCC5iInrLLZBTlOhkqdMRsFZBsp9retr46NjPLxRbrJqyHLhwz5QsVNup4xBsDXg0A40wGbVjbsG1z73iIuwsJpmzj0ZD'
user = 'StephanieP'

graph = yelp_academic_dataset_review.GraphAPI(access_token)
profile = graph.get(user)
posts = graph.get(profile['id'], 'posts')

while True:
    try:
        [some_action(post=post) for post in posts['data']]

        posts = requests.get(posts['paging']['next']).json()
    except KeyError:

        break

