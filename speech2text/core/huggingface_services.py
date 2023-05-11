# from transformers import WhisperProcessor, WhisperForConditionalGeneration, WhisperTokenizerFast
# from datasets import load_dataset, Audio, Dataset
# import soundfile as sf
# from ninja.files import UploadedFile
# from core.models import SpeechModel

# def map_to_array(batch, file):
#     try:
#         # speech_array1, _ = sf.read(batch)   # batch["file"]
#         # print(speech_array1)
#         speech_array2, _ = sf.read(file)
#         print(speech_array2)
#     except Exception as e:
#         print(e)
#     return batch

# # load model and processor
# processor = WhisperProcessor.from_pretrained("openai/whisper-medium")
# tokenizer = WhisperTokenizerFast.from_pretrained("openai/whisper-medium")

# model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium")
# model.config.forced_decoder_ids = None

# # # load dummy dataset and read audio files
# # ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")

# # sample = ds[0]["audio"]
# # input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt").input_features

# # # generate token ids
# # predicted_ids = model.generate(input_features)
# # # decode token ids to text
# # transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)

# # transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)


# def speech2text_serivce(us_file: str, uploaded_file: UploadedFile):
#     # TODO: Create audio from imported file
#     audio_dataset = Dataset.from_dict({
#         "audio": [us_file]
#     }).cast_column("audio", Audio(sampling_rate=16000))
#     audio_entry = audio_dataset[0]["audio"]
#     print(audio_dataset[0])
#     input_features = processor(
#         audio_entry["array"],
#         audio_entry["sampling_rate"],
#         return_tensors="pt").input_features
#     # generate token ids
#     predicted_ids = model.generate(input_features)
#     # decode token ids to text
#     transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)
#     transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
#     # TODO: Save model and audio file
#     instance = SpeechModel.objects.create(
#         transcription=transcription,
#         audio_file=us_file
#     )
#     print(transcription)
#     return transcription
