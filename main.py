from deepgram import DeepgramClient, SpeakOptions

DEEPGRAM_API_KEY = "cb3a0b2ab40ab54da6ab5ab182d81608ef61c226"

TEXT = {
    "text": "Let's test it out: Hi! I'm calling to let you know your prescription for Ondansetron is ready for pickup. Please contact us at (321) 654-7902 or support@example.com if you have any questions. Did you notice the accuracy when I read the phone number, email and a complex drug name?"
}
FILENAME = "audio.mp3"


def main():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = SpeakOptions(
            model="aura-asteria-en",
        )

        response = deepgram.speak.v("1").save(FILENAME, TEXT, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()