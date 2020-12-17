import threading as th
import pyaudio
import wave

form_1 = pyaudio.paInt16	#16-bit resolution
chans = 1			#1 channel
samp_rate = 44100		#44.1kHz sample rate
chunk = 4096			#2^12 samps for buffer
record_secs = 3			#seconds to record
dev_index = 2			#device index found by p.get_device_info_by_index(ii)

audio = pyaudio.PyAudio()	#create pyaudio instance
frames = []
keepRecording = True

def keyCaptureThread():
	global keepRecording
	input()
	keepRecording = False

def record():
	#create pyaudio stream
	stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index, input = True, frames_per_buffer = chunk)
	#start thread to look for Enter press
	th.Thread(target=keyCaptureThread, args=(), name='keyCaptureThread', daemon=True).start()
	#loop through stream and append audio chunks to frame list
	while keepRecording:
		noise = stream.read(chunk, exception_on_overflow = False)
		frames.append(noise)

	#stop and close stream.
	stream.stop_stream()
	stream.close()
	audio.terminate()

def saveAudio(fileName):
#save audio frames as .wav file
	wavefile = wave.open(fileName,'wb')
	wavefile.setnchannels(chans)
	wavefile.setsampwidth(audio.get_sample_size(form_1))
	wavefile.setframerate(samp_rate)
	wavefile.writeframes(b''.join(frames))
	wavefile.close
