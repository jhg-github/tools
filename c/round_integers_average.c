  /* to round an average of integers
   * - sum all elementes
   * - add number of elements/2 to the total sum
   * - divide by the number or elements
   */
  
  int32_t flowF3 = 0UL;
  for (int i = 0; i < AFE_SAMPLES_PER_BLOCK; i++)
  {
    flowF3 += block->fltrPass3[i].value_int32;
  }
  flowF3 += (((int32_t)AFE_SAMPLES_PER_BLOCK) / 2); /* this is a step in rounding up or down with ints */
  flowF3 /= (int32_t)AFE_SAMPLES_PER_BLOCK;