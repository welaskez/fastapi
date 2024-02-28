from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId
from typing import Annotated

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('')
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
