from fastapi import APIRouter, Body, HTTPException, status, Depends
from sqlmodel import select
from model.sample import Sample
from config.db import get_session
from typing import List
from auth.authenticate import authenticate

sample_router = APIRouter(
    tags=["Samples"]
)

samples = []


@sample_router.get("/", response_model=List[Sample])
async def retrieve_all_samples(session=Depends(get_session)) -> List[Sample]:
    statement = select(Sample)
    result = await session.execute(statement)
    sample_list = result.scalars().all()

    return sample_list


@sample_router.get("/{id_sample}", response_model=Sample)
async def retrieve_sample(id_sample: int, session=Depends(get_session)) -> Sample:
    sample = await session.get(Sample, id_sample)
    if not sample:
        raise HTTPException(
            status_code=status. HTTP_404_NOT_FOUND,
            detail="Sample with supplied ID does not exist"
        )
    return sample


@ sample_router.post("/")
async def create_sample(body:  Sample = Body(...)) -> dict:
    samples.append(body)
    return {
        "message": " Sample created successfully"
    }


@sample_router.delete("/{id_sample}")
async def delete_sample(id_sample: int) -> dict:
    for sample in samples:
        if sample.id_sample == id_sample:
            samples.remove(sample)
            return {
                "message": " Sample deleted successfully"
            }

    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail=" Sample with supplied ID does not exist"
    )


@sample_router.delete("/")
async def delete_all_samples() -> dict:
    samples.clear()
    return {
        "message": " Samples deleted successfully"
    }
