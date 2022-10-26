import argparse
import serial

from tqdm import tqdm
import time 
import import_data



from sklearn.metrics import confusion_matrix

def show_validation_results(labelList, predlist):
        #C = C_board
        C = confusion_matrix(labelList, predlist) 
        print(C)

        total_time = 0#sum(timeList)
        avg_time = 0#np.mean(timeList)
        acc = (C[0][0] + C[1][1]) / (C[0][0] + C[0][1] + C[1][0] + C[1][1])
        precision = C[1][1] / (C[1][1] + C[0][1])
        sensitivity = C[1][1] / (C[1][1] + C[1][0])
        FP_rate = C[0][1] / (C[0][1] + C[0][0])
        PPV = C[1][1] / (C[1][1] + C[1][0])
        NPV = C[0][0] / (C[0][0] + C[0][1])
        F1_score = (2 * precision * sensitivity) / (precision + sensitivity)
        F_beta_score = (1+2**2) * (precision * sensitivity) / ((2**2)*precision + sensitivity)

        print("\nacc: {},\nprecision: {},\nsensitivity: {},\nFP_rate: {},\nPPV: {},\nNPV: {},\nF1_score: {}, "
                "\ntotal_time: {},\n average_time: {}".format(acc, precision, sensitivity, FP_rate, PPV, NPV, F1_score,
                                                        total_time, avg_time))

        print("F_best_score : ", F_beta_score)
        
        
def main(args):

    resultList = []
    labelList = []
    last_pred = -1
    last_label = -1
    
    data = import_data.get_data(args.path_data)

    data = data.head(args.limit)
    port = args.com  # set port number
    ser = serial.Serial(port=port, baudrate=args.baudrate)  # open the serial
    print(ser)

    pbar = tqdm(range(0, len(data)))
    
    for idx in pbar:
        pbar.set_description("%d -> Sending data -]"  % (idx))
        pbar.set_description("%d -> Inference started - [label|pred: %s|%s]"  % (idx, last_label, last_pred))
        
        while ser.in_waiting < 5:
            #print(ser.in_waiting, end='\r')
            pass
            time.sleep(0.01)

        # when receiving the code "begin", send the test data cyclically
        recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
        # clear the input buffer
        ser.reset_input_buffer()
        if recv.strip() == 'begin':
        
            i_col=0
            for val in data.iloc[idx]:
                if i_col==32:
                    intres = int(val)
                    labelList.append(str(intres))
                    break
                send_str = str(val) + ' '
                ser.write(send_str.encode(encoding='utf8'))
                i_col+=1

            #ser.write('\n'.encode(encoding='utf8'))
            #print("Done")
            while ser.in_waiting < 2:
                #print("waiting ...", ser.in_waiting, end='\r')
                pass
                time.sleep(0.01)

            time.sleep(0.01)
            recv = ser.read(size=ser.in_waiting).decode(encoding='utf8')
            ser.reset_input_buffer()

            #print("Recieved msg ", recv)
            if recv.strip() == 'ok':
                time.sleep(0.02)
                # send status 200 to the board
                send_str = '200 '
                ser.write(send_str.encode(encoding='utf8'))
                #print("Msg 200 sent")
                time.sleep(0.01)
            # receive results from the board, which is a string separated by commas
            while ser.in_waiting < 10:
                pass
            
            recv = ser.read(size=10).decode(encoding='utf8')
            ser.reset_input_buffer()
            # the format of recv is ['<result>','<dutation>']
            result = recv.split(',')[0]
            inference_latency = recv.split(',')[1]
            #print("Inference result ", recv)
            #print("Result: ", result)
            #print(inference_latency)
            resultList.append(result)
            last_pred = resultList[-1]
            last_label = labelList[-1]
            
    show_validation_results(labelList, resultList)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--com', type=str, default='com5')
    argparser.add_argument('--baudrate', type=int, default=115200)
    argparser.add_argument('--limit', type=int, default=50)
    argparser.add_argument('--path_data', type=str,default="test_output_unprocessed.csv")
    args = argparser.parse_args()

    main(args)
