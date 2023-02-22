from random import randint
import strawberry
from strawberry.fastapi import GraphQLRouter
from collections import Counter
from typing import Optional

from app_data import Item, Review, items

@strawberry.input
class ItemInput:
    name: str
    description: str
    image: str

@strawberry.input
class ReviewDetails:
    author: str
    title: str
    description: str
    rating: int

@strawberry.input
class ReviewInput:
    itemId: int
    reviewDetails: ReviewDetails

@strawberry.type
class ItemDoesNotExist:
    itemId: int 
    message: str
    

def items_resolvers(name: str | None = None) -> list[Item]:
    if name:
        return [i for i in list(items.values()) if name.lower() in i.name.lower()]

    return list(items.values())


Response = strawberry.union(
    "AddReviewResponse", [Item, ItemDoesNotExist]
)


def leave_review(input: ReviewInput) -> Response:  # type: ignore
    if item := items.get(input.itemId):
        newReview = Review(
            author= input.reviewDetails.author,
            title=input.reviewDetails.title,
            description=input.reviewDetails.description,
            rating=input.reviewDetails.rating
        )
        item.reviews.append(newReview)
        return item

    return ItemDoesNotExist(itemId=input.itemId, message="No item with that ID found")

def add_item(input: ItemInput) -> Item:
    item = Item(
        itemId=randint(1000,9999),   
        name= input.name,
        description=input.description,
        image=input.image,
        reviews=[],
        )
    
    items[item.itemId] = item
    return item


@strawberry.type
class Query:
    items: list[Item] = strawberry.field(resolver=items_resolvers)


@strawberry.type
class Mutation:
    leave_review: Item | ItemDoesNotExist = strawberry.field(resolver=leave_review)
    add_item: Item = strawberry.field(resolver=add_item)

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)