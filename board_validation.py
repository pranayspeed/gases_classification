import argparse
import serial

from tqdm import tqdm
import time 
import import_data



def main(args):

    data = import_data.get_data()

    data = data.head(1500)
    port = args.com  # set port number
    ser = serial.Serial(port=port, baudrate=args.baudrate)  # open the serial
    print(ser)
    while ser.in_waiting < 5:
        print(ser.in_waiting, end='\r')
        pass
        time.sleep(0.01)

    # when receiving the code "begin", send the test data cyclically
    recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
    # clear the input buffer
    ser.reset_input_buffer()
    if recv.strip() == 'begin':

        pbar = tqdm(range(0, len(data)))
        
        for idx in pbar:
            pbar.set_description("%d -> Sending data -]"  % (idx))

            for val in data.iloc[idx]:
                send_str = str(val) + ' '
                ser.write(send_str.encode(encoding='utf8'))
            ser.write('\n'.encode(encoding='utf8'))
        print("Done")
        while ser.in_waiting < 2:
            print("waiting ...", ser.in_waiting, end='\r')
            pass
            time.sleep(0.01)
  
        time.sleep(0.01)
        recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
        ser.reset_input_buffer()

        print("Recieved msg ", recv)
        if recv.strip() == 'ok':
            time.sleep(0.02)
            # send status 200 to the board
            send_str = '200 '
            ser.write(send_str.encode(encoding='utf8'))
            print("Msg 200 sent")
            time.sleep(0.01)
        # receive results from the board, which is a string separated by commas
        while ser.in_waiting < 10:
            pass
        
        recv = ser.read(size=10).decode(encoding='utf8')
        ser.reset_input_buffer()
        # the format of recv is ['<result>','<dutation>']
        result = recv.split(',')[0]
        inference_latency = recv.split(',')[1]
        print(result)
        print(inference_latency)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--com', type=str, default='com5')
    argparser.add_argument('--baudrate', type=int, default=115200)
    argparser.add_argument('--path_data', type=str,default='../../tinyml_contest_data_training/')
    args = argparser.parse_args()

    main(args)
