# One Piece TCG Format Converter
This is a very quick project to automate the process of converting the differing text formats of decks used for the One Piece Trading Card Game.<br>
The main problem stems from the fact that [cardmarket](https://www.cardmarket.com/en/OnePiece), a website where you can buy cards, uses a different format for One Piece decks than all of the established deck sourcing services.<br>
## Main Problem
Let's say you got into the One Piece TCG and started building your own deck online. Now you want to export your deck into [cardmarket](https://www.cardmarket.com/en/OnePiece) so you can start buying physical versions of those cards to start playing for real, but when you create a wants list on [cardmarket](https://www.cardmarket.com/en/OnePiece), you realise that they require a specific format for mass importing cards.
### The formatting
You may have already realized, but a lot of the existing online deck sourcing options ([limitless](https://onepiece.limitlesstcg.com/decks) or [onepiece.gg](https://onepiece.gg/decks/)) use a very simple format, based on the [OPTCGSim](https://optcgsim.com):<br>
<i style="color: turquoise">quantity</i>x<i style="color: lightblue">card_set_id</i><br>
So a complete deck may look like this:<br>
```Deck
1xOP13-079
4xOP13-086
2xOP05-082
3xOP13-092
1xOP13-087
4xOP13-083
4xOP13-089
4xOP13-080
4xOP13-091
4xOP13-084
4xOP13-082
4xOP13-096
4xOP13-098
3xOP11-097
3xOP14-096
1xOP05-097
1xOP13-099
```
But [cardmarket](https://www.cardmarket.com/en/OnePiece) wanted to be special and use their own format, where they require further information.<br>
[cardmarket's](https://www.cardmarket.com/en/OnePiece) formatting looks like this:<br>
<i style="color: turquoise">quantity</i>x <i style="color: violet">card_name</i> <i style="color: lightblue">card_set_id</i> <i style="color: pink">(card_set_name)</i><br>
So the same deck has to look like this:
```Deck
1x Imu OP13-079 (Carrying On His Will)
4x Saint Shalria OP13-086 (Carrying On His Will)
2x Shirahoshi OP05-082 (Premium Booster -The Best-)
3x Saint Mjosgard OP13-092 (Carrying On His Will)
1x Saint Charlos OP13-087 (Carrying On His Will)
4x St. Jaygarcia Saturn OP13-083 (Carrying On His Will)
4x St. Topman Warcury OP13-089 (Carrying On His Will)
4x St. Ethanbaron V. Nusjuro OP13-080 (Carrying On His Will)
4x St. Marcus Mars OP13-091 (Carrying On His Will)
4x St. Shepherd Ju Peter OP13-084 (Carrying On His Will)
4x Five Elders OP13-082 (Carrying On His Will)
4x The Five Elders Are at Your Service!!! OP13-096 (Carrying On His Will)
4x Never Existed... in the First Place... OP13-098 (Carrying On His Will)
3x After All These Years I'm Losing My Edge!!! OP11-097 (A Fist of Divine Speed)
3x Ground Death OP14-096 (The Azure Sea's Seven)
1x Mary Geoise OP05-097 (Premium Booster -The Best- Vol. 2)
1x The Empty Throne OP13-099 (Carrying On His Will)
```

## Use-Case
Normally, you'd have like 15 different cards in your One Piece deck, so having to search for each card on their own can be very tiring and redundant, especially when you have the deck list right there.<br>
When you create a wants list on [cardmarket](https://www.cardmarket.com/en/OnePiece), you can theoretically paste a whole deck list. If you do, you may also be able to use their shopping wizard so they can instantly put your whole deck in a shopping cart.<br>
Normally, if you'd paste your deck list it wouldn't work due to [cardmarket](https://www.cardmarket.com/en/OnePiece) having their own formatting rules for deck imports, but with this simple converter this step is taken care of.<br>
Simply put in your One Piece decklist in the format of [OPTCGSim](https://optcgsim.com) and it will convert the text and automatically copy it to your clipboard so you can paste it into your wants list on [cardmarket](https://www.cardmarket.com/en/OnePiece) and use their shopping wizard to instantly order your whole deck!