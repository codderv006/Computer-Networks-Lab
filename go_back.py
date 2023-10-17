import random

def simul_GoBack(numframes, windSize, LossProb):
    sender_frames = list(range(numframes))
    receiver_buffer= [None]* numframes
    base = 0
    frame_counter = 0

    while frame_counter < numframes:
        for i in range(base, min(base+windSize, numframes)):
            if frame_counter < numframes:
                print(f"Sender: Sending frame {sender_frames[i]}")
                if random.random() >= LossProb:
                    frame_counter += 1

        for i in range(base, min(base+windSize, numframes)):
            if receiver_buffer[i] is None and random.random() >= LossProb:
                receiver_buffer[i] = sender_frames[i]
                print(f"Channel: received frame {receiver_buffer[i]}")

        while receiver_buffer[base] is not None:
            print(f"Receiver: acknowledging frame {receiver_buffer[base]}")
            base += 1

    print("Simul complete")

simul_GoBack(10, 3, 0.2)
