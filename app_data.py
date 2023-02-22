import strawberry

@strawberry.type
class Review:
    author: str
    title: str
    description: str
    rating: int


@strawberry.type
class Item:
    itemId: int
    name: str
    description: str
    image: str
    reviews: list[Review]

items: dict[int, Item] = {
    10001: Item(
        itemId= 10001,
        name= "Super Mario 64",
        description="A fun 3-D Adventure",
        image= "https://upload.wikimedia.org/wikipedia/en/6/6a/Super_Mario_64_box_cover.jpg",
        reviews= [
            Review(
                author="Mario",
                title="My favorite Game",
                description="The variety of levels and scale each world is simply breathtaking. The game consists of 15 massive courses in which Mario can attain seven stars per course, with numerous secret areas and bonuses, including 15 extra stars (for a total or 120 stars). It'll surely take the average gamer 60 hours to reach the third and final Bowser and free the princess (not to mention find Yoshi), so the game's replay value is bountiful.",
                rating=10
            ),
            Review(
                author="Wario",
                title="My least favorite Game",
                description="If I could give this game a 0, I would. There is no Wario in this game!",
                rating=1
            ),
            Review(
                author="Luigi",
                title="It's pretty good",
                description="Pretty fun but no Luigi :(",
                rating=6
            ),
        ]
    ),
    10002: Item(
        itemId= 10002,
        name= "The Legend of Zelda: Ocarina of Time",
        description="A fun adventure through Hyrule",
        image= "https://assets-prd.ignimgs.com/2021/12/07/zeldaoot-ignart-1638901927766.jpg",
        reviews= [
            Review(
                author="Link",
                title="Hyah",
                description="HUT HUT HUT HYAAAAAAAAAAAAAAAAAAAAAAAAAAAH HUT HYAH",
                rating=7
            ),
            Review(
                author="Zelda",
                title="Not fun... for me",
                description="Seriously, I was stuck in a castle for the first half of the game...",
                rating=3
            ),
            Review(
                author="Ganandorf",
                title="More Power",
                description="Fun game... I didn't like the ending.",
                rating=9
            ),
        ]
    ),
    10003: Item(
        itemId= 10003,
        name= "Mario Kart",
        description="The best racing game ever!",
        image= "https://m.media-amazon.com/images/M/MV5BNzNhZDg2ODctOGZkZi00OTJmLWJiMDYtMDM5YmMxMTQ4ODRjXkEyXkFqcGdeQXVyMTA3NjAwMDc4._V1_FMjpg_UX1000_.jpg",
        reviews= [
            Review(
                author="Koopa Troppa",
                title="Eh it's alright",
                description="Eh... not enough levels for my liking. I'm more of a fan of diddy kong racing",
                rating=5
            ),
            Review(
                author="Donkey Kong",
                title="Fun Fun Fun",
                description="You guys should play Diddy Kong Racing. this game is still fun though",
                rating=8
            ),
        ]
    )
}

