from livekit.agents import llm
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import cartesia, deepgram, openai, silero

initial_ctx = llm.ChatContext().append(
    role="system",
    text="<your prompt>",
)

agent = VoicePipelineAgent(
    vad=silero.VAD.load(),
    # flexibility to use any models
    stt=deepgram.STT(model="nova-2-general"),
    llm=openai.LLM(),
    tts=cartesia.TTS(),
    # intial ChatContext with system prompt
    chat_ctx=initial_ctx,
    # whether the agent can be interrupted
    allow_interruptions=True,
    # sensitivity of when to interrupt
    interrupt_speech_duration=0.5,
    interrupt_min_words=0,
    # minimal silence duration to consider end of turn
    min_endpointing_delay=0.5,
    # callback to run before LLM is called, can be used to modify chat context
    before_llm_cb=None,
    # callback to run before TTS is called, can be used to customize pronounciation
    before_tts_cb=None,
)

# start the participant for a particular room, taking audio input from a single participant
agent.start(room, participant)