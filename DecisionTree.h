
int predict(float *x) {
    if (x[28] <= -1.199500024318695) {
        return 1;
    }

    else {
        if (x[10] <= -0.0005000000237487257) {
            if (x[11] <= -0.0005000000237487257) {
                if (x[10] <= -0.0035000001080334187) {
                    if (x[23] <= -0.0005000000237487257) {
                        if (x[4] <= -0.005499999970197678) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }

                    else {
                        if (x[20] <= 0.0035000001080334187) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }
                }

                else {
                    if (x[7] <= -0.0005000000237487257) {
                        if (x[0] <= -0.0025000000605359674) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }

                    else {
                        if (x[11] <= -0.001500000071246177) {
                            return 2;
                        }

                        else {
                            return 2;
                        }
                    }
                }
            }

            else {
                if (x[20] <= -0.001500000071246177) {
                    if (x[12] <= -0.012500000651925802) {
                        return 0;
                    }

                    else {
                        if (x[21] <= 0.001500000071246177) {
                            return 2;
                        }

                        else {
                            return 0;
                        }
                    }
                }

                else {
                    if (x[20] <= 0.0005000000237487257) {
                        if (x[0] <= -0.0005000000237487257) {
                            return 2;
                        }

                        else {
                            return 0;
                        }
                    }

                    else {
                        if (x[21] <= 0.0005000000237487257) {
                            return 2;
                        }

                        else {
                            return 2;
                        }
                    }
                }
            }
        }

        else {
            if (x[10] <= 4.5000000682193786e-05) {
                if (x[20] <= -0.001500000071246177) {
                    if (x[8] <= -0.009499999694526196) {
                        if (x[20] <= -0.04200000036507845) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }

                    else {
                        if (x[4] <= -0.004500000039115548) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }
                }

                else {
                    if (x[20] <= 0.001500000071246177) {
                        if (x[11] <= 0.0005000000237487257) {
                            return 0;
                        }

                        else {
                            return 0;
                        }
                    }

                    else {
                        if (x[12] <= 0.0005000000237487257) {
                            return 2;
                        }

                        else {
                            return 2;
                        }
                    }
                }
            }

            else {
                if (x[7] <= 4.845000148634426e-06) {
                    if (x[19] <= 0.0035000001080334187) {
                        if (x[11] <= 0.0005000000237487257) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }

                    else {
                        if (x[8] <= 0.005499999970197678) {
                            return 0;
                        }

                        else {
                            return 2;
                        }
                    }
                }

                else {
                    if (x[7] <= 0.001500000071246177) {
                        if (x[11] <= 3.555000148480758e-05) {
                            return 2;
                        }

                        else {
                            return 2;
                        }
                    }

                    else {
                        if (x[9] <= 0.0025000000605359674) {
                            return 2;
                        }

                        else {
                            return 2;
                        }
                    }
                }
            }
        }
    }
}
