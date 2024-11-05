import os
from livekit import rtc, api

async def handle_audio(track: rtc.Track):
    audio_stream = rtc.AudioStream(track)
    async for frame in audio_stream:
        # Received a video frame from the track, process it here
        print(frame)

async def test():
    token = (
        api.AccessToken(os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_API_SECRET"))
        .with_identity("agent")
        .with_name("agent")
        .with_grants(
            api.VideoGrants(
                room_join=True,
                room="test_room",
            )
        )
        .to_jwt()
    )
    url = os.getenv("LIVEKIT_URL")
    room = rtc.Room()
    await room.connect(url, token)

    print(room.local_participant)
    print(room.remote_participants)

    @room.on("track_subscribed")
    def on_track_subscribed(track: rtc.Track, publication: rtc.RemoteTrackPublication, participant: rtc.RemoteParticipant):
        if track.kind == rtc.TrackKind.KIND_AUDIO:
            loop.create_task(handle_audio(track))

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(test())
    loop.run_forever()

