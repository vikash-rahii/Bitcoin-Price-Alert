# Bitcoin-Price-Alert
set up-

This project makes use of HTTP requests and how to send them appropriately using the 'requests' package.

We also make use of webhooks and how we can use them to connect our application to external services, such as phone notifications or Telegram messages.

With relatively little code i am going to arrive at a fully-fledged Bitcoin price notification service that will be easily extendable to other cryptocurrencies and services.

Bitcoin price is a fickle thing. You never know where it's going to be at the end of the day. So, instead of checking various sites for the latest updates, I’ll make a python app to do the work for us.

For this, we're going to use the popular automation website IFTTT. IFTTT ("if this, then that") is a web service that bridges the gap between different apps and devices.

We're going to create two IFTTT applets:
- One for emergency notification when Bitcoin price falls under a certain threshold; and
- another for regular Telegram updates on the Bitcoin price.

Both will be triggered by our Python app which will consume data from the Coinmarketcap API.

An IFTTT applet is composed of two parts:
1. a trigger and
2. an action.

In our case, the trigger will be a webhook service provided by IFTTT.

Our app will make an HTTP request to the webhook URL which will trigger an action. The action could be almost anything we want. IFTTT offers a multitude of actions like sending an email, updating a Google Spreadsheet and even calling your phone.

Project Setup.
Python 3 virtual environment:

$ mkvirtualenv -p $(which python3) bitcoin_notifications

Activating the virtual environment and installing the required dependencies:

$ workon bitcoin_notifications 		# To activate the virtual environment
$ pip install requests 		        # We only need the requests package

what is Bitcoin?
1.Bitcoin uses peer-to-peer technology to operate with no central authority or banks; managing transactions and the issuing of bitcoins is carried out collectively by the network. Bitcoin is open-source; its design is public, nobody owns or controls Bitcoin and everyone can take part. Through many of its unique properties, Bitcoin allows exciting uses that could not be covered by any previous payment system.
Bitcoin emerged out of the 2008 global economic crisis when big banks were caught misusing borrowers' money, manipulating the system, and charging exorbitant fees. To address such issues, Bitcoin creators wanted to put the owners of bitcoins in-charge of the transactions, eliminate the middleman, cut high interest rates and transaction fees, and make transactions transparent. They created a distributed network system, where people could control their funds in a transparent way. Bitcoin has grown rapidly and spread far in a relatively short period of time. Across the world, companies from a large jewellery chain in the US, to a private hospital in Poland, accept bitcoin currency. Multi-billion-dollar corporations such as Dell, PayPal, Microsoft, Expedia, etc., are dealing in bitcoins. Websites promote bitcoins, magazines are publishing bitcoin news, and forums are discussing cryptocurrencies and trading in bitcoins. Bitcoin has its own Application Programming Interface (API), price index, trading exchanges and exchange rate. However, there are issues with bitcoins such as hackers breaking into accounts, high volatility of bitcoins, and long transaction delays. Elsewhere, particularly people in third world countries find Bitcoins as a reliable channel for transacting money bypassing pesky intermediaries.

2.What is IFTTT?
f This Then That, also known as IFTTT (/ɪft/),is a freeware web-based service that creates chains of simple conditional statements, called applets.

An applet is triggered by changes that occur within other web services such as Gmail, Facebook, Telegram, Instagram, or Pinterest

IFTTT employs the following concepts:

Services (formerly known as channels) are the basic building blocks of IFTTT. They mainly describe a series of data from a certain web service such as YouTube or eBay. Services can also describe actions controlled with certain APIs, like SMS. Sometimes, they can represent information in terms of weather or stocks. Each service has a particular set of triggers and actions.
Triggers are the "this" part of an applet. They are the items that trigger the action. For example, from an RSS feed, you can receive a notification based on a keyword or phrase.
Actions are the "that" part of an applet. They are the output that results from the input of the trigger.
Applets (formerly known as recipes) are the predicates made from Triggers and Actions. For example, if you like a picture on Instagram (trigger), an IFTTT app can send the photo to your Dropbox account (action).
Ingredients are basic data available from a trigger—from the email trigger, for example; subject, body, attachment, received date, and sender’s address.

HOW DOES WORK IFTTT?

IFTTT helps you connect all of your different apps and devices. When you sign up for a free account, you can turn on Applets that help your apps and devices work together to do specific things they couldn't do otherwise. For example, you can back up your Instagram photos to Dropbox, have your lights turn on when you enter your home, or automatically remind a Slack channel about a meeting. There are millions of Applets to explore.
Here's how it works:

Create a free account.
Browse the IFTTT website or app to find an Applet that interests you.
Click into the Applet and turn it on.
Connect the services that are involved in the Applet — this is only so we can use them to run Applets on your behalf. IFTTT provides a layer between different services to only allow them to do what you specifically tell them to do.
Find more Applets, and repeat! 
I AM USING TELEGRAM APP IN IFTTT.
step by step:

1.Sign up for an IFTTT account

2.To get started with IFTTT, you'll need an account. Go to https://ifttt.com/user/new and sign up for a free account.

3.Install the mobile app and log in.

Since we're going to send a notification to your phone, we'll need to install the IFTTT app and log in.

4.Create a new Applet

5.Choose the "webhooks" service

6.Set up the trigger

7.Choose the action

8.Configure the "notifications" action
Now we're going to configure our action. We have two options at present: regular notifications or rich notifications. We're going to use normal notifications, so click Send a notification from the IFTTT app.

9.then,Get your IFTTT API key.
In order to send the web request to trigger the notification, we'll need to authenticate. To authenticate, we'll use an IFTTT secret key.
To find your key, click this link, and then click documentation. This page should show your key. Make sure to use key (not my fake one) in the script later on.9:59 PM 27-Mar-20

10.Create the price alert config.
There are many ways this step could be accomplished, but since this tutorial is primarily about getting started with IFTTT, I'm going to use the absolute simplest method.

11.then,Create a script to monitor the Bitcoin price .
This is where things get fun. I’ll write a Python script that will be executed every minute (using cron). This script will ping the coinmarketcap API, check the Bitcoin price, then send a notification if any of our price rules are met.

12.Run our script every minute
