from fastapi import FastAPI
from library_management.presentation.routes.books import router as books_router
from library_management.presentation.routes.members import router as members_router
from library_management.presentation.routes.borrowing import router as borrowing_router

app = FastAPI()



app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(members_router, prefix="/members", tags=["Members"])
app.include_router(borrowing_router, prefix="/borrow", tags=["Borrowing"])


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}