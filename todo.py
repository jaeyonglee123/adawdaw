from fastapi import APIRouter,Path
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
import uvicorn

todo_router = APIRouter()


origins = []



todo_list = []
todo_counter = 0

@todo_router.post("/todo")
async def add_todo(todo : Todo) -> dict:
    global todo_counter
    todo.id = todo_counter = todo_counter + 1  #todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return { "msg" : "todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return { "todos" : todo_list}

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id : int = Path(..., title = "the id of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo" : todo}
    return{"msg : there is no task with the id"}

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
    return {"msg": f"Todo with ID {todo_id} deleted successfully"}
    return {"msg": "Todo with supplied ID doesn't exist"}