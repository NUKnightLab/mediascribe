import random
from starlite import Controller, Request, Response, get, post, put, patch, delete


def enqueue_av_job(media_url, model):
    """placeholder for job creation TBD."""
    return random.randint(0, 100)


class ASRController(Controller):
    """Automatic speech recognition of A/V media. Currently supports ASR of YouTube
    videos with openai whisper models.

    Enqueues a download+transcription job and returns a structure which includes the
    job ID.
    """

    tags = ["Tasks: ASR"]
    path = "/asr"

    @get(path="/transcribe", name="transcribe")
    async def transcribe(
        self,
        mediaUrl: str,
        request: Request,
        model: str = "WhisperTiny_en",
    ) -> Response[dict]:
        job_id = enqueue_av_job(media_url=mediaUrl, model=model)
        return Response(
            {
                "jobId": job_id,
                "resultsEndpoint": request.url_for("asr_results", job_id=job_id),
            },
        )

    @get(path="/results", name="asr_results")
    async def results(self, jobId: str, request: Request) -> dict:
        return {"jobId": jobId, "data": "TBD"}
