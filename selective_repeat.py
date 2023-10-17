import random

def simul_selectiveRep(numFrames, windSize, LossProb):
    sender_frames = list(range(numFrames))
    receiver_buffer = [None]* numFrames
    ack_frames = [False]*numFrames

    def send_frame(frame_num):
        if random.random() >= LossProb:
            print(f"Sender: Sending frame {frame_num}")
            return True
        else:
            print(f"Sender: lost frame {frame_num}")
            return False

    def receive_frame(frame_num):
        if random.random() >= LossProb:
            print(f"Channel: received frame {frame_num}")
            return True
        else:
            print(f"Channel: lost frame {frame_num}")
            return False

    frame_counter = 0
    while frame_counter < numFrames:
        for i in range(frame_counter, min(frame_counter+windSize, numFrames)):
            if send_frame(sender_frames[i]):
                frame_counter +=1

        for i in range(numFrames):
            if not ack_frames and receiver_buffer is None:
                if receive_frame([sender_frames[i]]):
                    receiver_buffer = sender_frames[i]
                    print(f"Receiver: acknowledging frame: {receiver_buffer[i]}")
                    ack_frames = True

    print("Simul complete")

simul_selectiveRep(10,3,0.2)