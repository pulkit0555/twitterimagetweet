from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import tweepy
import os
#tweepy is used to post to twitter
#pillow library for converting string to image
# Consumer keys and access tokens, used for OAuth
from config import *
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth) 
#set tweet status
status = "Hi!=)"
#array of quotes from which a new quote is selected randomly
quotes = [
    '"The path to success is to take massive, determined action." ~ Tony Robbins',
    '"Kicking ass takes getting your ass kicked" ~ Jason Calacanis',
    '"The perfect is the enemy of the good." ~ Voltaire',
    '"Words may show a man\'s wit but actions his meaning." ~ Benjamin Franklin',
    '"If you love life, don\'t waste time, for time is what life is made up of." ~ Bruce Lee',
    '"In essence, if we want to direct our lives, we must take control of our consistent actions. It\'s not what we do once in a while that shapes our lives, but what we do consistently." ~ Tony Robbins',
    '"Success comes from taking the initiative and following up persisting eloquently expressing the depth of your love. What simple action could you take today to produce a new momentum toward success in your life?" ~ Tony Robbins',
    '"If you spend too much time thinking about a thing, you\'ll never get it done. " ~ Bruce Lee',
    '"The less effort, the faster and more powerful you will be. " ~ Bruce Lee',
    '"Most people have no idea of the giant capacity we can immediately command when we focus all of our resources on mastering a single area of our lives." ~ Tony Robbins',
    '"Focus is a matter of deciding what things you are not going to do" ~ John Carmack',
    '"In order to succeed, people need a sense of self-efficacy, to struggle together with resilience to meet the inevitable obstacles and inequities of life." ~ Albert Bandura',
    '"Only to the extent that we expose ourselves over and over to annihilation can that which is indestructible in us be found." ~ Pema Chodron',
    '"The vision must be followed by the venture. It is not enough to stare up the steps - we must step up the stairs." ~ Vance Havner',
    '"Whatever you can do, or dream you can do, begin it. Boldness has genius, power and magic in it. Begin it now." ~ Goethe',
    ]
pattern = Image.open("input.jpg", "r").convert('RGBA')
size = width, height = pattern.size
draw = ImageDraw.Draw(pattern,'RGBA')
#takes a random quote and draw on the given image or background
draw.text((0,0), random.choice(quotes), (0, 0, 0, 0))#,font=font)
pattern.save('sample-out.jpg')
# load image
imagePath = "sample-out.jpg"
# Send the tweet with imagepath and status
api.update_with_media(imagePath, status)

