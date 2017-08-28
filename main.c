//
//  main.c
//  2d_convolution
//
//  Created by Bowen Wei on 8/29/17.
//  Copyright © 2017 bowen wei. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>

int main(int argc, const char * argv[]) {
    int N_i;
    int in_channel=3;
    int o_channel;
    int kernel_size=3;
    int stride=1;
    int half_size=kernel_size/2;
    int image_size_x=119;
    int image_size_y=119;
    int o_size_x=(image_size_x-half_size*2)/stride;
    int o_size_y=(image_size_y-half_size*2)/stride;
    int image[image_size_x][image_size_y][in_channel];
    int i,j,k,i1,i2,j1,j2,x_c,y_c,sum;
    
    for (i=0;i<image_size_x;i++){
        for (j=0;j<image_size_y;j++){
            for (k=0;k<in_channel;k++){
                image[i][j][k]=rand()%256;
            }
        }
    }
    struct timeval t1, t2;
    int kernel[kernel_size][kernel_size];
    for (N_i=0;N_i<12;N_i++){
        int o_channel_max=pow(2,N_i);
        //int o_image[o_size_x][o_size_y][o_channel_max];
        gettimeofday(&t1, NULL);
        for (o_channel=0;o_channel<o_channel_max;o_channel++){
            for (i=0;i<kernel_size;i++){
                for (j=0;j<kernel_size;j++){
                    kernel[i][j]=rand()%256;
                }
            }
            for (i1=0;i1<o_size_x;i1++){
                for (j1=0;j1<o_size_y;j1++){
                    x_c=half_size+i1*stride;
                    y_c=half_size+j1*stride;
                    sum=0;
                    for (i2=0;i2<kernel_size;i2++){
                        for (j2=0;j2<kernel_size;j2++){
                            for(k=0;k<in_channel;k++){
                                sum+=kernel[i2][j2]*image[x_c-half_size+i2][y_c-half_size+j2][k];
                            }
                        }
                    }
                    //o_image[i1][j1][o_channel]=sum;
                }
            }
        }
        gettimeofday(&t2, NULL);
        double time_spent = (double)(t2.tv_sec - t1.tv_sec);
        time_spent+=(t2.tv_usec - t1.tv_usec) / 1000000.0;
        printf("i=%d,time_taken:%f\n",N_i,time_spent);
    }
    return 0;
}
