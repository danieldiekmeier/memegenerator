# -*- coding: utf-8 -*-

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import sys

args_len = len(sys.argv)
if args_len == 1:
	# no args except the launch of the script
	print 'args plz'
elif args_len == 2:
	# only one argument, use standard meme
	topString = ''
	bottomString = sys.argv[-1].decode("utf-8").upper()
	meme = 'standard'
elif args_len == 3:
	# args give meme and one line
	topString = ''
	bottomString = sys.argv[-1].decode("utf-8").upper()
	meme = sys.argv[1].lower()
elif args_len == 4:
	# args give meme and two lines
	topString = sys.argv[-2].decode("utf-8").upper()
	bottomString = sys.argv[-1].decode("utf-8").upper()
	meme = sys.argv[1].lower()
else:
	# so many args
	# what do they mean
	# too intense
	print 'to many argz'

print meme

img = Image.open(str(meme)+'.jpg')
imageSize = img.size

# find biggest font size that works
fontSize = imageSize[1]/5
font = ImageFont.truetype("/Library/Fonts/Impact.ttf", fontSize)
topTextSize = font.getsize(topString)
bottomTextSize = font.getsize(bottomString)
while topTextSize[0] > imageSize[0]-20 or bottomTextSize[0] > imageSize[0]-20:
	fontSize = fontSize - 1
	font = ImageFont.truetype("/Library/Fonts/Impact.ttf", fontSize)
	topTextSize = font.getsize(topString)
	bottomTextSize = font.getsize(bottomString)

# find top centered position for top text
topTextPositionX = (imageSize[0]/2) - (topTextSize[0]/2)
topTextPositionY = 0
topTextPosition = (topTextPositionX, topTextPositionY)

# find bottom centered position for bottom text
bottomTextPositionX = (imageSize[0]/2) - (bottomTextSize[0]/2)
bottomTextPositionY = imageSize[1] - bottomTextSize[1]
bottomTextPosition = (bottomTextPositionX, bottomTextPositionY)

draw = ImageDraw.Draw(img)

# draw outlines
# there may be a better way
outlineRange = fontSize/15
for x in range(-outlineRange, outlineRange+1):
	for y in range(-outlineRange, outlineRange+1):
		draw.text((topTextPosition[0]+x, topTextPosition[1]+y), topString, (0,0,0), font=font)
		draw.text((bottomTextPosition[0]+x, bottomTextPosition[1]+y), bottomString, (0,0,0), font=font)

draw.text(topTextPosition, topString, (255,255,255), font=font)
draw.text(bottomTextPosition, bottomString, (255,255,255), font=font)

img.save("temp.png")