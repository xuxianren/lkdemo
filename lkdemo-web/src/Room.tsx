import {
    ControlBar,
    GridLayout,
    LiveKitRoom,
    ParticipantTile,
    RoomAudioRenderer,
    useTracks,
} from '@livekit/components-react';

import '@livekit/components-styles';

import { Track } from 'livekit-client';
import { useState } from 'react';

const serverUrl = import.meta.env.VITE_LIVEKIT_URL;
console.log(import.meta.env)
console.log("serverUrl", import.meta.env.VITE_LIVEKIT_URL)


export default function ChatApp() {
    const [token, setToken] = useState("")
    const handleInput = (e:any)=>{
        setToken(e.target.value)
    }
    return (
        <>
            <label>
                token: <input type="text" value={token} onChange={handleInput}></input>
            </label>
            {token && <LiveKitRoom
                video={false}
                audio={true}
                token={token}
                serverUrl={serverUrl}
                // Use the default LiveKit theme for nice styles.
                data-lk-theme="default"
                style={{ height: '50vh' }}
            >
                {/* Your custom component with basic video conferencing functionality. */}
                {/* <MyVideoConference /> */}
                {/* The RoomAudioRenderer takes care of room-wide audio for you. */}
                <RoomAudioRenderer />
                {/* Controls for the user to start/stop audio, video, and screen
        share tracks and to leave the room. */}
                <ControlBar />
            </LiveKitRoom>}
        </>

    );
}

function MyVideoConference() {
    // `useTracks` returns all camera and screen share tracks. If a user
    // joins without a published camera track, a placeholder track is returned.
    const tracks = useTracks(
        [
            { source: Track.Source.Camera, withPlaceholder: true },
            { source: Track.Source.ScreenShare, withPlaceholder: false },
        ],
        { onlySubscribed: false },
    );
    return (
        <GridLayout tracks={tracks} style={{ height: 'calc(100vh - var(--lk-control-bar-height))' }}>
            {/* The GridLayout accepts zero or one child. The child is used
        as a template to render all passed in tracks. */}
            <ParticipantTile />
        </GridLayout>
    );
}