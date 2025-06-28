
## Inspiration
Firstly, we believed there was a lot of utility in writing a wrapper for spotify. Spotify is a software utilized by millions of people for hours every day; one effect of this is that it is a service that has achieved a particularly intimate knowledge of peoples preferences, and we believe, their mental state. Some of our cited research has shown the unmistakable effect of the music one listen's to on their mental state. Therefore, a product that can better suggest music tailored to a person's mental state absolutely has utility for the world as a whole.
Furthermore, we believed this project was an exciting opportunity to explore many facets of programming that were completely new to us, like the Spotify API, natural language processing, and the Taipy library.

## What It Does
At a high level, our product seeks to turn intangible, qualitative, subjective concept, like mood, or emotion, and with the might of our algorithm, convert it into a quantifiable metric from which we can song recommendations. Specifically, we have created an extensive natural language processing algorithm that seeks to derive the emotional sentiment attached to each word in the lyrics of a song, and assigns a happiness value to it, from which similar songs can be parsed and studied. Using this metric, we also attempt to study the average happiness of chart topping songs in countries around the world, to see if there exists any tendencies towards certain countries having a preference towards sadder or happier music. Ultimately, the product is an attempt at tailoring music to a user's mood, which studies find to be beneficial for a number of reasons.

## How We Built It
We wrote a comprehensive front end to our app in the Taipy library, while we analyzed our song data and applied our algorithms using jupyter notebook, and we used Spotify API to link our accounts and gain unique insights.

## Accomplishments
We are very proud of being able to create such a comprehensive and useable web app within the time frame that we have, creating a whole new algorithm to explicitly study the happiness level of a song, something that should theoretically be subjective and unquantifiable. We hope to gather more data to see how actual user sentiment reflects the perceived sentiment of our algorithm.
We also learned the entire Taipy library in relatively short order for composing a deployable front end, something that was not easy given the lack of documentation online.
