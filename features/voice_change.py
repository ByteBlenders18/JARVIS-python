import librosa
import soundfile


def male_voice(audio_path):

    y, sr = librosa.load(rf"{audio_path}")
    steps = -1.7
    new_y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=steps)
    soundfile.write(r"pitchShifted.wav", new_y, sr)


def female_voice(audio):

    y, sr = librosa.load(rf"{audio}")
    steps = 4
    new_y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=steps)
    soundfile.write(r"D:\python projects\Project JARVIS\features\change voice\pitchShifted_female.wav", new_y, sr)
