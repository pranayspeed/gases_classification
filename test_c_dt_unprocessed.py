


from sklearn.metrics import confusion_matrix
import os
import sys

from sklearn.linear_model import LogisticRegression

def show_validation_results(C):
        #C = C_board
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

def read_test_and_pred(test_file, pred_file):
    labelList=[]
    predlist=[]
    with open(pred_file) as pred_f:
        for line in pred_f:
            val = line.strip()
            if len(val)>0:
                predlist.append(val)
    size_of_data = len(predlist)
    with open(test_file) as test_f:
        List=[]
        for line in test_f:
            #List.append(line)
            labelList.append(line.split(',')[-1].strip())
            if len(labelList) == size_of_data:
                break

    print(len(labelList), len(predlist))
    #print(labelList[0:5])
    #print(predlist[0:5])
    return confusion_matrix(labelList, predlist)  

import argparse

if __name__ == "__main__":

    argparser = argparse.ArgumentParser()

    argparser.add_argument('--test_data', type=str, help='test_data', default='../../tinyml_contest_data_training')
    argparser.add_argument('--eval_data', type=str, help='eval_data', default='../../tinyml_contest2022_demo_evaluation')

    args = argparser.parse_args()

    os.system('g++ -g dt_test.c -o dt_test.bin')
    os.system('./dt_test.bin ') #+str(sample_size))
    conf_mat_v1 = read_test_and_pred("./test_output_unprocessed.csv", "./test_results.txt")
    #print("sample_size = ", sample_size)
    show_validation_results(conf_mat_v1)