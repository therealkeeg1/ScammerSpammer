# ScammerSpammer

This is a script to randomly generate fake info to send to scammers and fill their databases with useless garbage! 
After receiving tons of text messages saying I won a free iPad, I felt like I was obligated to do something about it. So I decided to create my own little spam program to solve this small inconvenience; really it was just an excuse to write another python script :)

## How does it work
First we generate random fake names along with fake credit card info.
Throw everything into our payload variable, and send a post request to their totally "legit" website. 

## But why credit card info?
Most payment processors charge a fee to the scammers to process a declined transaction. 
On top of filling their databases with lots of useless info we can also cost them a tiny fee, hopefully making them rethink their decisions. 

## Did it work?
YES! Well at least for me, maybe they just choose a different group of phone numbers. Although I did notice all javascript looked very familiar across many different scam texts. This would make me think this was performed by the same group.


This is purely meant for entertainment purposes only. USE AT YOUR OWN RISK
