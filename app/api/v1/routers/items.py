from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/items", tags=["Items"])


# Pydantic model for request/response validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True
    created_at: Optional[datetime] = None


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None


# Mock database
items_db = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop",
        "price": 999.99,
        "is_available": True,
        "created_at": datetime.now()
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "description": "Ergonomic wireless mouse",
        "price": 29.99,
        "is_available": False,
        "created_at": datetime.now()
    },
    {
        "id": 3,
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard",
        "price": 79.99,
        "is_available": True,
        "created_at": datetime.now()
    }
]


@router.get("/", response_model=List[Item])
async def get_items():
    """Get all items"""
    return items_db


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a single item by ID"""
    item = next((item for item in items_db if item["id"] == item_id), None)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item"""
    # Generate new ID
    new_id = max([item["id"] for item in items_db]) + 1 if items_db else 1

    # Create new item
    new_item = {
        "id": new_id,
        **item.model_dump(),
        "created_at": datetime.now()
    }
    items_db.append(new_item)
    return new_item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    for index, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            # Update only fields that are provided
            update_data = item.model_dump(exclude_unset=True)
            items_db[index].update(update_data)
            return items_db[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item"""
    for index, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            items_db.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with id {item_id} not found"
    )


@router.get("/search/")
async def search_items(q: str = ""):
    """Search items by name"""
    if not q:
        return items_db

    results = [item for item in items_db if q.lower() in item["name"].lower()]
    return results