from fastapi import APIRouter, Body, HTTPException, status
from models.sample import Sample
from typing import List

sample_router = APIRouter(
    tags=["Samples"]
)

samples = []


@sample_router.get("/", response_model=List[Sample])
async def retrieve_all_samples() -> List[Sample]:
    return samples


@sample_router.get("/{id_sample}", response_model=Sample)
async def retrieve_sample(id_sample: int) -> Sample:
    for sample in samples:
        if sample.id_sample == id_sample:
            return sample

    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Sample with supplied ID does not exist"
    )


@ sample_router.post("/new")
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
