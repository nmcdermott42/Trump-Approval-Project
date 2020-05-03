# Trump Approval Project

***

##### This project was put together during a college course I took using python libraries like pandas and numpy as well as statistical methods to analyze data sets. In this project I used a the twitter api as well as python and tableau to try and create script that could get an in the moment approval rating of the president by assigning values to tweets that had mention of certain keywords related to him. Included in the repo are the .py files used to gather the tweet sample as well as the one used for anlysis. There is also a tableau workbook used to get generate some visualizations for the report

***

American politics have seemed increasingly divisive and polarized since the election of President Trump, and depending on the news coverage you watch the opinion given on him can vary dramatically. In order to have a more accurate public image of Trump this project created an approval rating for the President based off of Twitter data. 

To gather the dataset 10,000 tweets were collected based on them containing the text ‘Trump’. After these tweets were gathered they were cleaned to remove entries that did not contain actual data. Once an appropriate data set was finished the contents were compared to a lexicon containing words categorized into four groups based on their polarity; strongly negative, negative, positive, and strongly positive. Each category received a point value, and if a tweet contained a word from a category the corresponding point value was added and the final sum of all points for each tweet was calculated to create a net point value for each tweet. Based on the total value for each tweet, the overall polarity of each tweet was found and these overall polarities were averaged across the entire dataset to determine the average approval rating of President Trump.

The sample ended up giving President Trump an approval rating of 0.718. With how close this is to zero this shows that the President has a slightly positive approval rating, but it is almost a net-neutral rating. Most net point values for a given tweet were zero which indicated that extremely strong opinions were less frequent from users in both the negative and positive direction. Overall these results indicate that although there are extremely polarized opinions often presented through news stories, based on a sample of recent tweets related to him the President seems to have a more neutral overall opinion from individuals.

When seeking out the data for this project one of the biggest concerns was collecting tweets in a way that would not impart a bias on the data. To do this without selecting individual tweets, a very general keyword of ‘Trump’ was used and 10,000 recent tweets were gathered. This insured that the sample would be large enough to contain both positive and negative tweets. In order to run analysis, some tweets which ended up containing no twitter data had to be removed from the data set, leaving a total of 9,875 tweets in the sample. 

To categorize the tweets there needed to be further data which contained categories of words based on their subjective polarity. To do this a dictionary containing 6,602 unstemmed words was found which contained polarity ratings falling into four categories; strongly negative, negative, positive, and strongly positive. Point values were assigned to each category to quantify polarity, with strongly positive being worth 10 points, positive worth 5, negative worth -5, and strongly negative worth -10. To apply these values to tweets, the words in each tweet were referenced against the dictionary to determine if any words were included in both. If a tweet contained a word then the corresponding point value was utilized, and once all words had been checked these point values were summed into a final net point value for the tweet. This meant that a tweet could be classified based on overall polarity to use for the approval rating creation. 

The results of this can be seen in the graph titled Net Tweet Point Totals, which shows that a majority of tweets ended with a net neutral polarity. This also shows that extremely polarized tweets were less common than slightly positive or negative tweets. After this point total was calculated for each tweet, they were average together in order to determine the average approval rating for Trump in the sample, which ended up being 0.718. 
***
![Image](https://github.com/nmcdermott42/Trump-Approval-Project/blob/master/tweetpoints.png)

The table Top 25 Hashtags and Mentions gives both the top 25 hashtags and mentions pulled from the sample used. Some of the key issues discussed were QAnon, White House Correspondents Dinner, Iran, Kanye West, and the Indigenous People of Biafra. The variety displayed shows that the public is concerned with Trump’s involvements in many different directions from international issues to social media gossip. It also showed that the tweets collected were not focused on a specific issue, which could have served to bias the tweets in either a positive or negative direction based on the issue.
***
|		    |     Hashtags      | # of Uses |    Mentions      | # of Uses |
| :---: |     --------      | --------: |    --------      | --------: |
|   1   | #trump            |   158     | @realdonaldtrump |   328     |
|   2   | #maga             |   111     | @rvawonk         |   167     |
|   3   | #whcd             |   75      | @krassenstein    |   160     |
|   4   | #qanon            |   49      | @ryanafournier   |   153     |
|   5   | #mondaymotivation |   35      | @mikel_jollett   |   145     |
|   6   | #thebrooksbr      |   29      | @keithboykin     |   137     |
|   7   | #michellewolf     |   25      | @hoarsewhisperer |   136     |
|   8   | #whcd.            |   24      | @michelleisawolf |   130     |
|   9   | #whca             |   24      | @kanyewest  	   |   117     |
|  10   | #resist  		      |   22	  	| @potus		       |   104     |
|  11   | #theresistance  	|   21	  	| @funder		       |   99      |
|  12   | #iran			      	|   17		  | @sayshummingbird |   97 	   |
|  13   | #trump'		      	|   17		  | @tonyposnanski   |   94	     |
|  14   | #fakenews	     		|   17		  | @sarahkendzior   |   92 	   |
|  15   | #veteransunited	  |   16		  | @presssec		     |   88	     |
|  16 	| #veterans 	     	|   16		  | @tribelaw	  	   |   87 	   |
|  17 	| #impeachtrump	   	|   16		  | @edkrassen	     |   80      |
|  18 	| #magaveterans	  	|   16		  | @proudresister   |   71	     |
|  19   | #morningjoe	    	|   15		  | @kathygriffin	   |   68	     |
|  20   | #foxnews		    	|   15		  | @amy_siskind	   |   68      |
|  21 	| #kanyewest	    	|   15		  | @teapainusa	     |   59	     |
|  22   | #ipob				      |   14		  | @cnn			       |   55	     |
|  23   | #whcd18			      |   13		  | @olivermcgee	   |   55	     |
|  24 	| #kag 			      	|   12 		  | @theplumlinegs   |   52	     |
|  25 	| #coup			      	|   12		  | @thehill		     |   48	     |

One of the main conclusions is that Trump’s approval rating is significantly higher than his approval rating in polls conducted by firms like Rasmussen or Reuters. This difference in approval could be due to the medium by which we were measuring opinion because Trump has a very active Twitter presence. Another key conclusion from the data is that the public is focused on a wide variety of issues and Trump’s involvement in each of them. This points towards confirmation that the sample has a diverse set of opinions, giving a more accurate estimate of approval. 
